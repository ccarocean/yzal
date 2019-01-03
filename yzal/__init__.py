"""Lazy evaluation for Python."""

from typing import cast, Any, Generic, TypeVar, Callable  # for typing
from functools import wraps
import lazy_object_proxy  # type: ignore


__version__ = '0.0.4'

__all__ = ('Thunk', 'lazy', 'strict')


T = TypeVar('T')  # noqa


class Thunk(lazy_object_proxy.Proxy, Generic[T]):
    """A thunk, used to delay a calculation until the value is needed.

    Thunk's behave as a delegating wrapper or proxy object to the result of
    the lazy computation.  Until the strict value is asked for, either with
    the :func:`strict` function or by accessing an attribute or function
    through the Thunk.
    """

    def __strict__(self) -> T:
        """Get the strict (non lazy) value from the Thunk.

        Returns
        -------
        object
            Result of evaluating the thunk.

        """
        # relies on internal implementation of Proxy
        return cast(T, self.__wrapped__)


def lazy(wrapped: Callable[..., T]) -> Callable[..., Thunk[T]]:
    """Decorate a strict function, making it lazy.

    Lazy functions will return a :class:`Thunk` when called, delaying any
    computation until the result is needed.

    .. note::

        This will work for

    .. caution::

        When the wrapped function is not a `pure function`_ care must be
        taken to ensure that the side effects are not time dependent as
        they will not occur until the generated Thunk is evaluated.

        A common issue with this behavior is exceptions.  If the wrapped
        function raises an exception it will not be raised in the calling
        location, but where the value of the Thunk is initially requested,
        which will likely be outside of any try/except clause.  This can
        cause bugs in unexpected locations.
    ..

    .. _pure function: https://en.wikipedia.org/wiki/Pure_function

    Parameters
    ----------
    wrapped
        Function or method to decorate.

    Returns
    -------
    Callable
        Decorated function.

    """
    @wraps(wrapped)
    def wrapper(*args: Any, **kwargs: Any) -> Thunk[T]:
        def thunk() -> T:
            return wrapped(*args, **kwargs)
        return Thunk(thunk)
    return wrapper


def strict(thunk: Thunk[T]) -> T:
    """Get the strict value, from a Thunk.

    Parameters
    ----------
    thunk : Thunk
        The :class:`Thunk` like object to get a final/strict value from.

    Returns
    -------
    object
        Result of evaluating the thunk

    """
    try:
        return thunk.__strict__()
    except AttributeError:
        raise TypeError(
            "object of type '{:s}' has no strict()".format(
                type(thunk).__name__))
