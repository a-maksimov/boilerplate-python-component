import json
from pathlib import Path

import pytest

from boilerplate_module.optimizer import Optimizer
from tests.config import test_config


@pytest.fixture(scope="module")
def test_dataset(request) -> dict:
    test_folder = Path(request.fspath).parent
    test_name = request.param
    mock_folder = test_folder / test_config[test_name]["mock_folder"]
    test_dataset_path = mock_folder / "test_dataset.json"

    with test_dataset_path.open(encoding="utf-8") as file:
        return json.load(file)


@pytest.fixture(scope="module")
def optimizer(request, test_dataset: dict) -> Optimizer:
    optimizer = Optimizer(**test_dataset)
    return optimizer
