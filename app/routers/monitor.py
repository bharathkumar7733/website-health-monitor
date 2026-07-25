from fastapi import APIRouter, HTTPException

from app.models.schemas import (
    StartMonitoringRequest,
    WebsiteRequest,
    WebsiteResponse,
)
from app.services.health_service import check_website
from app.services.monitoring_service import (
    get_monitoring_status,
    start_monitoring,
    stop_monitoring,
)
from app.services.servicenow_service import (
    create_incident,
    find_existing_incident,
)
from app.utils.logger import logger


router = APIRouter(
    prefix="/monitor",
    tags=["Website Monitor"]
)


@router.post("/check", response_model=WebsiteResponse)
def monitor_website(request: WebsiteRequest):
    result = check_website(request.url)

    if result["status"] == "UP":
        logger.info(
            f"Website: {request.url} | "
            f"Status: UP | "
            f"HTTP Status: {result['status_code']}"
        )

    elif result["status"] == "DOWN":
        existing_incident = find_existing_incident(request.url)

        if existing_incident:
            result["incident_number"] = existing_incident["incident_number"]
            result["incident_action"] = "Existing incident returned"

            logger.warning(
                f"Website: {request.url} | "
                f"Status: DOWN | "
                f"Incident: {existing_incident['incident_number']} | "
                f"Action: Existing incident returned"
            )

        else:
            incident = create_incident(
                short_description="Website Down",
                description=f"{request.url} - {result['message']}"
            )

            result["incident_number"] = incident["incident_number"]
            result["incident_action"] = "New incident created"

            logger.error(
                f"Website: {request.url} | "
                f"Status: DOWN | "
                f"Incident: {incident['incident_number']} | "
                f"Action: New incident created"
            )

    return result


@router.post("/start")
def start_monitor(request: StartMonitoringRequest):
    started = start_monitoring(
        request.url,
        request.interval
    )

    if not started:
        raise HTTPException(
            status_code=400,
            detail="Monitoring is already running"
        )

    return {
        "message": "Monitoring started",
        "url": request.url,
        "interval": request.interval
    }


@router.post("/stop")
def stop_monitor():
    stop_monitoring()

    return {
        "message": "Monitoring stopped"
    }


@router.get("/status")
def monitoring_status():
    return get_monitoring_status()
