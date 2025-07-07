import json
from pathlib import Path

import pytest

from tests.config import test_config

TEST_NAME = "integration_test"


@pytest.mark.integration
@pytest.mark.parametrize("test_dataset", [TEST_NAME], indirect=True)
def test_integration(request, test_dataset, optimizer):
    test_folder = Path(request.fspath).parent
    reference_folder = test_folder / test_config[TEST_NAME]["reference_folder"]

    test_results = optimizer.run()

    reference_results_file_path = reference_folder / "reference.json"
    with open(reference_results_file_path, "r", encoding="utf-8") as file:
        reference_results = json.load(file)

    assert test_results == reference_results
