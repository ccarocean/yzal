from yzal import lazy


def test_lazy(mocker):
    m = mocker.Mock()

    @lazy
    def add(x, y):
        m(x + y)
        return x + y

    result = add(30, 8)
    assert m.call_count == 0
    assert result == 38
    m.assert_called_once_with(38)
    assert m.call_count == 1
