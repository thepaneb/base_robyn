"""
API initialization for the Robyn application.
"""

from robyn import Robyn
from robyn.openapi import OpenAPI, OpenAPIInfo

app = Robyn(
    file_object=__file__,
    openapi=OpenAPI(
        info=OpenAPIInfo(
            title="Basic Robyn API",
            description="A simple Robyn API application",
            version="0.1.0",
        )
    ),
)
