import argparse


def parse_arguments() -> argparse.Namespace:
    """Parse command‑line arguments for the module’s CLI.

    Returns:
        argparse.Namespace: with attributes
          - loglevel (str): desired logging level
          - values (List[int]): list of item values
          - weights (List[int]): list of item weights
          - capacity (int): knapsack capacity
    """
    parser = argparse.ArgumentParser(description="Boilerplate Python Module CLI")
    parser.add_argument(
        "--loglevel", type=str, help="Set logging level (DEBUG, INFO, WARNING, etc.)"
    )
    parser.add_argument(
        "--values",
        type=int,
        nargs="+",
        required=True,
        help="List of item values, e.g. --values 60 100 120",
    )
    parser.add_argument(
        "--weights",
        type=int,
        nargs="+",
        required=True,
        help="List of item weights, e.g. --weights 10 20 30",
    )
    parser.add_argument(
        "--capacity",
        type=int,
        required=True,
        help="Knapsack capacity, e.g. --capacity 50",
    )
    return parser.parse_args()
