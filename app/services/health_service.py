import requests


def check_website(url: str):

    try:
        response = requests.get(url, timeout=5)
        status = response.status_code
        
        # Skeleton check logic placeholder
        return {
            "status": "UNKNOWN",
            "status_code": status,
            "message": "Response received"
        }
    except requests.exceptions.Timeout:
        return {
            "status": "DOWN",
            "status_code": None,
            "message": "Request Timed Out"
        }
