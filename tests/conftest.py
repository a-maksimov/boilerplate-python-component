import pytest

from boilerplate_module.optimizer import Optimizer


@pytest.fixture(scope="module")
def optimizer(request) -> Optimizer:
    optimizer = Optimizer()
    return optimizer
