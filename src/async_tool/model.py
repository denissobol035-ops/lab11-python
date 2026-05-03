import asyncio
from typing import TypedDict


class TaskItem(TypedDict):
    id: int
    delay: float
    good: bool


class TaskResult(TypedDict, total=False):
    id: int
    status: str
    message: str


async def process_item(item: TaskItem) -> TaskResult:
    await asyncio.sleep(item["delay"])

    if not item["good"]:
        raise ValueError(f"Task {item['id']} failed")

    return {
        "id": item["id"],
        "status": "done",
    }
