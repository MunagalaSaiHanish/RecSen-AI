from app.schemas.agent import (
    MemoryEntry,
    StepExecution,
    WorkingMemory,
)


def add_execution_to_memory(
    memory: WorkingMemory,
    execution: StepExecution,
) -> None:
    if not execution.success:
        return

    if execution.tool_name is None:
        return

    if execution.observation is None:
        return

    entry = MemoryEntry(
        source=execution.tool_name,
        content=execution.observation,
    )

    memory.entries.append(entry)


def get_memory_entries(
    memory: WorkingMemory,
) -> list[MemoryEntry]:
    return memory.entries