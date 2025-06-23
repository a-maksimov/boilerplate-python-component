import pytest

TEST_NAME = "integration_test"


@pytest.mark.integration
def test_integration(request, optimizer):
    optimizer.run()
