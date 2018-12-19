import pytest
from yzal import strict


def test_strict(thunk):
    assert thunk.__strict__.call_count == 0
    assert strict(thunk) == 4
    assert thunk.__strict__.call_count == 1
    assert strict(thunk) == 4
    assert thunk.__strict__.call_count == 2


def test_strict_error(not_thunk):
    """Throws TypeError if __strict__ method does not exist."""
    with pytest.raises(TypeError):
        strict(not_thunk)
