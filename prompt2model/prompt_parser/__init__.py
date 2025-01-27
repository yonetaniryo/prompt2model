"""Import PromptSpec classes."""
from prompt2model.prompt_parser.base import PromptSpec, TaskType
from prompt2model.prompt_parser.instr_parser import OpenAIInstructionParser
from prompt2model.prompt_parser.mock import MockPromptSpec

__all__ = (
    "PromptSpec",
    "TaskType",
    "MockPromptSpec",
    "OpenAIInstructionParser",
)
