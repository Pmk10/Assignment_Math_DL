import rmse
import pytest
def test_rmse():
    predictions = [1, 2, 3, 4, 5]
    targets = [1, 2, 3, 4, 5]

    assert rmse.rmse(predictions, targets) == 0

    predictions = [2, 3, 4, 5, 6]
    targets = [1, 2, 3, 4, 5]

    assert rmse.rmse(predictions, targets) == 1


if __name__ == "__main__":
    pytest.main(["-v", "rmse_test.py"])