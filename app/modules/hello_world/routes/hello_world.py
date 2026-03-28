"""
Hello world module routes.
"""

from robyn import Request

from modules.hello_world.models.hello_world import HelloModel
from modules.hello_world.router import router


@router.post("", openapi_name="Hello world", openapi_tags=["hello_world"])
async def get_root(body: HelloModel, request: Request) -> str:
    """
    Returns "Hello, world!" string.
    """
    return "Hello, world!"
