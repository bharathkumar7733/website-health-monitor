from pydantic import BaseModel


class WebsiteRequest(BaseModel):
    url: str


class WebsiteResponse(BaseModel):
    status: str
    status_code: int | None
    message: str
    incident_number: str | None = None
    incident_action: str | None = None

class StartMonitoringRequest(BaseModel):
    url: str
    interval: int
