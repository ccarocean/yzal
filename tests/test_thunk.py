from yzal import Thunk, strict


def test_thunk(simple_function):
    thunk = Thunk(simple_function)
    # no call before strict
    assert simple_function.call_count == 0
    assert thunk + 10 == 48
    assert simple_function.call_count == 1
    # only one call after more than one strict
    assert thunk + 10 == 48
    assert simple_function.call_count == 1


def test_internal_strict(simple_function):
    thunk = Thunk(simple_function)
    # no call before strict
    assert simple_function.call_count == 0
    assert thunk.__strict__() == 38
    assert simple_function.call_count == 1
    assert simple_function.call_count == 1
    # only one call after more than one strict
    assert thunk.__strict__() == 38
    assert simple_function.call_count == 1


def test_strict(simple_function):
    thunk = Thunk(simple_function)
    # no call before strict
    assert simple_function.call_count == 0
    assert strict(thunk) == 38
    assert simple_function.call_count == 1
    # only one call after more than one strict
    assert strict(thunk) == 38
    assert simple_function.call_count == 1
