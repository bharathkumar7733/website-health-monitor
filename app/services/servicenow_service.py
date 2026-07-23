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
    # Response code to be implemented
    return None
