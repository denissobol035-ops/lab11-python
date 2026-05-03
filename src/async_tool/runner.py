import asyncio
import logging
from typing import List

from .model import TaskItem, TaskResult, process_item


logger = logging.getLogger(__name__)


async def run_sync(tasks: List[TaskItem], cont: bool) -> List[TaskResult]:
    results = []

    for item in tasks:
        logger.info(f"Start task {item['id']}")

        try:
            res = await process_item(item)
            results.append(res)
        except Exception as e:
            if not cont:
                raise
            results.append({
                "id": item["id"],
                "status": "error",
                "message": str(e),
            })

    return results


async def run_async(tasks: List[TaskItem], cont: bool) -> List[TaskResult]:
    coros = [process_item(t) for t in tasks]

    if cont:
        results = await asyncio.gather(*coros, return_exceptions=True)
        final = []

        for item, res in zip(tasks, results):
            if isinstance(res, Exception):
                final.append({
                    "id": item["id"],
                    "status": "error",
                    "message": str(res),
                })
            else:
                final.append(res)

        return final

    else:
        return await asyncio.gather(*coros)


async def run_limited(tasks: List[TaskItem], limit: int, cont: bool) -> List[TaskResult]:
    sem = asyncio.Semaphore(limit)

    async def worker(item: TaskItem) -> TaskResult:
        async with sem:
            try:
                return await process_item(item)
            except Exception as e:
                if not cont:
                    raise
                return {
                    "id": item["id"],
                    "status": "error",
                    "message": str(e),
                }

    coros = [worker(t) for t in tasks]
    return await asyncio.gather(*coros)
