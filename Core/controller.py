import importlib


class Controller:

    @staticmethod
    def controller(controller):
        module = importlib.import_module("Controller" + "." + controller)
        return module

    @staticmethod
    def view(view):
        module = importlib.import_module("View" + "." + view)
        return module

    @staticmethod
    def model(model):
        module = importlib.import_module("Model" + "." + model)
        return module
