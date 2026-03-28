"""
Redoc module routes.
"""
import os

from robyn import Response

from modules.redoc.router import router


@router.get("", openapi_name="Redoc", openapi_tags=["redoc"])
async def get_root():
    """
    Returns the Redoc documentation.
    """
    x = os.path.dirname(__file__).split("modules")[0]

    print(x)
    
    with open(f"{x}/static/redoc.html", "r") as f:
        html = f.read()
        
    return Response(
        status_code=200,
        description=html,
        headers={"Content-Type": "text/html"}
    )
