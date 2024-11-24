import requests

def http_request(endpoint, method, headers=None, payload=None):
    headers = {k.strip(): v.strip() for k, _, v in (h.partition(':') for h in headers or [])}
    method = method.upper()

    try:
        if method == "GET":
            response = requests.get(endpoint, headers=headers)
        elif method == "POST":
            if isinstance(payload, dict):
                response = requests.post(endpoint, headers=headers, json=payload)
            else:
                response = requests.post(endpoint, headers=headers, data=payload)
        else:
            raise ValueError("Unsupported HTTP method")
        
        return {
            "status_code": response.status_code,
            "headers": dict(response.headers),
            "content": response.text
        }
    
    except ValueError as e:
        return {"error": str(e)}