from temp import *
import sys
sys.path.append('./src')
from src.temp2 import *
import pytest


@pytest.fixture
def mock_requests_post(mocker):
    mock_response = {"status" : "success"}
    mocker.patch('requests.post', return_value=mocker.Mock(json=lambda: mock_response))


def test_temp_function(mock_requests_post):
    data = None
    with pytest.raises(CustomError) as e:
        my_function(data)
    print("error: ", e.value)
    assert str(e.value)=="1001"

# def test_temp_function():
#     assert func() == "hello world"

# def test_temp2_function():
#     assert func2() == "hello"