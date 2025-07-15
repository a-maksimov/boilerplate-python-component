from boilerplate_python_component.cli import parse_arguments
from boilerplate_python_component.optimizer import Optimizer


def main():
    """Parse the CLI arguments, construct an Optimizer, and execute its run() method.

    Main CLI entry point for the boilerplate_python_component.
    """
    kwargs = parse_arguments()
    optimizer = Optimizer(**vars(kwargs))
    optimizer.run()


if __name__ == "__main__":
    main()
