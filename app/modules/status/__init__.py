"""
Status module initialization.
"""
import importlib.util
import os

from api import Robyn

from modules.status.router import router


def init_routes():
    """
    Initialize routes for the status module.
    """
    routes_dir = os.path.join(os.path.dirname(__file__), "routes")

    for module_name in [
        name
        for name in os.listdir(routes_dir)
        if name.endswith(".py")
        and not name.startswith("__")
        and os.path.isfile(os.path.join(routes_dir, name))
    ]:
        route_file = os.path.join(routes_dir, module_name)
        spec = importlib.util.spec_from_file_location(module_name, route_file)
        module = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(module)
        except Exception as e:  # pylint: disable=broad-except
            print(f"Failed to load route {module_name}: {e}")


def init_module(robyn_app: Robyn):
    """
    Initialize the status module.
    """
    init_routes()
    robyn_app.include_router(router)
