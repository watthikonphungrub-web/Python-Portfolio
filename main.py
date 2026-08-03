def check_http_status(status_code):
    if status_code == 200:
        return "OK Service is Healthy"
    elif status_code == 404:
        return "Not Found"
    elif status_code == 500:
        return "Internal Server Error"
    else:
        return "Unknown Status Code"

result = check_http_status(200)
print(result)
