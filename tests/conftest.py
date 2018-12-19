import pytest
from yzal import Thunk


@pytest.fixture
def simple_function(mocker):
    m = mocker.Mock()
    m.return_value = 38
    return m


@pytest.fixture
def thunk(mocker):
    m = mocker.Mock(Thunk)
    m.__strict__.return_value = 4
    return m


@pytest.fixture
def not_thunk(mocker):
    m = mocker.Mock(Thunk)
    m.__strict__.side_effect = AttributeError()
    return m
