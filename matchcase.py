def status(n):
    match n:
        case (200):
            return "OK"
        case (404):
            return "Not Found"
        case(408):
            return "Request Timeout"
        case(503):
            return "Service Unavailable"
        case(401):
            return "unauthorized"
        case(429):
            return "Too Many Requests"
        case _:
            return "enter valid number"
        
error = int(input("enter the error number : "))
print(status(error))