from pulp import LpMinimize, LpProblem, LpVariable, lpSum

from boilerplate_module.logger import get_logger


def knapsack(values: list[int], weights: list[int], capacity: int) -> dict[str, int]:
    """Solve the 0/1 knapsack problem using linear programming.

    Args:
        values (list[int]): List of item values.
        weights (list[int]): List of item weights.
        capacity (int): Maximum allowed total weight.

    Returns:
        list[int]: Binary selection list indicating which items are chosen.
    """
    n = len(values)
    model = LpProblem("Knapsack", LpMinimize)
    x = [LpVariable(f"x_{i}", cat="Binary") for i in range(n)]

    model += lpSum(-values[i] * x[i] for i in range(n))
    model += lpSum(weights[i] * x[i] for i in range(n)) <= capacity

    model.solve()

    return {str(var): int(var.value() or 0) for var in x}


class Optimizer:
    def __init__(
        self,
        values: list[int],
        weights: list[int],
        capacity: int,
        **kwargs,
    ) -> None:
        self._logger = get_logger(kwargs.get("loglevel"))

        self._values = values
        self._weights = weights
        self._capacity = capacity

        self._logger.info(f"{self} was successfully initialized.")

    def run(self) -> dict[str, int]:
        self._logger.info(f"{self} is running...")

        solution = knapsack(self._values, self._weights, self._capacity)

        self._logger.info("Solution:")
        for var_name, var_value in solution.items():
            self._logger.info(f"{var_name}: {var_value}")

        return solution
