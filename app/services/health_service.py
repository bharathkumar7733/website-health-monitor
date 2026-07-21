import requests


def check_website(url: str):

    try:
        response = requests.get(url, timeout=5)
        status = response.status_code

        if 200 <= status < 400:
            return {
                "status": "UP",
                "status_code": status,
                "message": "Website is Healthy"
            }

        elif 400 <= status < 500:
            return {
                "status": "DOWN",
                "status_code": status,
                "message": f"Client Error ({status})"
            }

        elif 500 <= status < 600:
            return {
                "status": "DOWN",
                "status_code": status,
                "message": f"Server Error ({status})"
            }

        else:
            return {
                "status": "UNKNOWN",
                "status_code": status,
                "message": "Unexpected Status Code"
            }

    except requests.exceptions.Timeout:
        return {
            "status": "DOWN",
            "status_code": None,
            "message": "Request Timed Out"
        }

    except requests.exceptions.ConnectionError:
        return {
            "status": "DOWN",
            "status_code": None,
            "message": "Connection Failed"
        }

    except requests.exceptions.RequestException as e:
        return {
            "status": "DOWN",
            "status_code": None,
            "message": str(e)
        }
