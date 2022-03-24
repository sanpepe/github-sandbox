from websand.src.http.ParsedRequest import ParsedRequest

class RequestParser:
    def __init__(self):
        pass

    def parse(self, requestString):
        request = ParsedRequest()
        if requestString:
            parts = requestString.split()
            if len(parts) >= 1:
                request.method = parts[0]

            if len(parts) >= 2:
                request.path = parts[1]

        return request