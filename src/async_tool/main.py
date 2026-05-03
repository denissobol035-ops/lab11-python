import asyncio
import json
import logging
from pathlib import Path

from .cli import build_parser
from .runner import run_sync, run_async, run_limited


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    logging.basicConfig(level=getattr(logging, args.log_level))

    tasks = json.loads(Path(args.input).read_text())

    if args.mode == "sync":
        results = asyncio.run(run_sync(tasks, args.continue_on_error))

    elif args.mode == "async":
        results = asyncio.run(run_async(tasks, args.continue_on_error))

    else:
        results = asyncio.run(
            run_limited(tasks, args.limit, args.continue_on_error)
        )

    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
