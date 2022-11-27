import argparse

def make_parser() -> argparse.ArgumentParser:
    """Make parser"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-n",
        "--number",
        type=str,
        required=True,
        help="Number to consult, between 1 and 99",
    )
    return parser


