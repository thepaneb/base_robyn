"""
A simple Robyn application that responds with "Hello, world!" at the root URL.
"""

from robyn import Robyn

app = Robyn(__file__)


@app.get("/")
async def get_root():
    """
    Returns "Hello, world!" string.
    """
    return "Hello, world!"


app.start()
