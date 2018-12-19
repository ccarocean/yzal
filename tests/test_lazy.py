import yzal
from yzal import lazy


def test_lazy(mocker):
    mocker.patch('yzal.Thunk', autospec=True)

    @lazy
    def add(x, y):
        return x + y

    assert yzal.Thunk.call_count == 0
    add(5, 10)
    assert yzal.Thunk.call_count == 1
    args, _ = yzal.Thunk.call_args_list[0]
    assert len(args) == 1
    assert args[0]() == 15
