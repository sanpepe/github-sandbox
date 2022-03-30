class Router:
    def __init__(self):
        self.routes = {}

    def addPath(self, path, controller):
        self.routes[path] = controller

    def route(self, request):
        parts = request.path.split("/")
        controllerKey = parts[1] if len(parts) > 1 else ""
        controller = self.routes.get(controllerKey, None)

        if controller is None:
            return "HTTP/1.1 404 ERROR\n"
        else:
            return controller.handle(request)