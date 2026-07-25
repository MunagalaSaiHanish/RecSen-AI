from typing import Any

from pydantic import BaseModel, Field


class ServiceToolInput(BaseModel):
    service: str = Field(min_length=1)


class ToolResult(BaseModel):
    success: bool
    tool_name: str
    data: dict[str, Any] | None = None
    error: str | None = None