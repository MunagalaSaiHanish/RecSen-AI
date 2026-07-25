from collections.abc import Callable

from pydantic import BaseModel


class Tool:
    def __init__(
        self,
        name: str,
        description: str,
        input_model: type[BaseModel],
        function: Callable,
    ):
        self.name = name
        self.description = description
        self.input_model = input_model
        self.function = function

    def to_llm_definition(self) -> dict:
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.description,
                "parameters": self.input_model.model_json_schema(),
            },
        }