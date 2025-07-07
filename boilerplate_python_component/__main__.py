from boilerplate_python_component.cli import parse_arguments
from boilerplate_python_component.optimizer import Optimizer


def main():
    kwargs = parse_arguments()
    optimizer = Optimizer(**vars(kwargs))
    optimizer.run()


if __name__ == "__main__":
    main()
