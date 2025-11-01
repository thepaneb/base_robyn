"""
Main entry point for the application.
"""

import importlib.util
import os

from api import app, Robyn


def init_modules(robyn_app: Robyn):
    """
    Initialize application modules.
    """
    modules_dir = os.path.join(os.path.dirname(__file__), "modules")

    for module_name in [
        name
        for name in os.listdir(modules_dir)
        if os.path.isdir(os.path.join(modules_dir, name))
        and not name.startswith("__")
        and os.path.isfile(os.path.join(modules_dir, name, "__init__.py"))
    ]:
        init_file = os.path.join(modules_dir, module_name, "__init__.py")
        spec = importlib.util.spec_from_file_location(module_name, init_file)
        module = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(module)
            if hasattr(module, "init_module"):
                module.init_module(robyn_app)
        except Exception as e:  # pylint: disable=broad-except
            print(f"Failed to initialize module {module_name}: {e}")


init_modules(app)


def main():
    """
    Main function to start the application.
    """
    app.start()


if __name__ == "__main__":
    main()
