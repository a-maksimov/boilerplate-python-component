import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description="Boilerplate Python Module CLI")
    parser.add_argument("--loglevel", type=str, help="Set logging level")
    parser.add_argument(
        "--nosave", action="store_true", help="Do not save results to DB"
    )
    parser.add_argument("--savetocsv", action="store_true", help="Save results to CSV")

    return parser.parse_args()
