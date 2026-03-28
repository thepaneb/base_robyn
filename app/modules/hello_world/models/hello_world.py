from typing import Annotated

from pydantic import BaseModel, Field
from robyn.types import Body


class HelloModel(BaseModel, Body):
    name: Annotated[str | None, Field(description="The name of the person to greet", max_length=5, default="Hello World", pattern=r"^[a-zA-Z ]{1,5}$")]
