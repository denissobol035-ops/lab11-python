import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Async Batch Processor")

    parser.add_argument("input", help="Path to JSON file")

    parser.add_argument(
        "--mode",
        choices=["sync", "async", "limited"],
        default="sync",
    )

    parser.add_argument("--limit", type=int, default=5)

    parser.add_argument("--continue-on-error", action="store_true")

    parser.add_argument(
        "--log-level",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        default="WARNING",
    )

    return parser
