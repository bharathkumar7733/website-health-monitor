import requests

from app.core.config import (
    SERVICENOW_INSTANCE,
    SERVICENOW_USERNAME,
    SERVICENOW_PASSWORD,
)

def find_existing_incident(website_url: str):
    url = f"{SERVICENOW_INSTANCE}/api/now/table/incident"

    headers = {
        "Accept": "application/json"
    }

    params = {
        "sysparm_query": (
            f"active=true"
            f"^short_description=Website Down"
            f"^descriptionLIKE{website_url}"
        ),
        "sysparm_fields": "number,sys_id",
        "sysparm_limit": "1"
    }

    response = requests.get(
        url,
        auth=(SERVICENOW_USERNAME, SERVICENOW_PASSWORD),
        headers=headers,
        params=params,
        timeout=10
    )

    response.raise_for_status()

    incidents = response.json()["result"]

    if incidents:
        return {
            "incident_number": incidents[0]["number"],
            "sys_id": incidents[0]["sys_id"]
        }

    return None

def create_incident(short_description: str, description: str):
    url = f"{SERVICENOW_INSTANCE}/api/now/table/incident"

    payload = {
        "short_description": short_description,
        "description": description,
        "impact": "2",
        "urgency": "2",
    }

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    # POST execution to be implemented
    return {"incident_number": "INC0000000", "sys_id": "dummy"}
