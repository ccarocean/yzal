yzal |build-status| |coverage-status|
=====================================

|version|
|supported-implementations|
|supported-versions|
|wheel|


Lazy evaluation for Python.



Usage
-----

To use yzal:

.. code-block:: python

    from yzal import lazy, strict

    @lazy
    def add(x, y):
        sum = x + y
        print('Adding {:d} + {:d} = {:d}', x, y, sum)

The following only creates a Thunk, it does not run the lazy function above.

.. code-block:: python

    >>> sum = add(3, 7)

There are two ways to get the result of the lazy evaluation.  The first is
simply to perform an operation that requires a strict value.

.. code-block:: python

    >>> 5 + sum
    Adding 3 + 7 = 10
    15

The second way is to explicitly request a strict value.

.. code-block:: python

    >>> sum = add(3, 7)
    >>> strict(sum)
    Adding 3 + 7 = 10
    10

.. note::

    If we did not recreate the Thunk the side effect string would not have
    displayed again.  This is because Thunk's will only evaluate the lazy
    expression they contain once.  Further requests for a strict value will
    return a cached result.  It is important to remember this when the lazy
    function is not pure.


Requirements
------------

* Python 3.4 or greater
* lazy_object_proxy_

.. note::

    Python 3.4 support requires mypy_.


Installation
------------

yzal is on PyPI_ so the best way to install it is:

.. code-block:: text

    $ pip install yzal


Thanks
------

We wish to thank the following projects, without which yzal would have been
much harder to write:

* lazy_object_proxy_ - A fast and thorough lazy object proxy.


.. _lazy_object_proxy: https://python-lazy-object-proxy.readthedocs.io/en/latest/
.. _mypy: http://mypy-lang.org/
.. _PyPI: https://pypi.org/

.. |build-status| image:: https://travis-ci.com/ccarocean/yzal.svg?branch=master&style=flat
   :target: https://travis-ci.com/ccarocean/yzal
   :alt: Build status

.. |coverage-status| image:: http://codecov.io/gh/ccarocean/yzal/coverage.svg?branch=master
   :target: http://codecov.io/gh/ccarocean/yzal?branch=master
   :alt: Test coverage

.. |version| image:: https://img.shields.io/pypi/v/yzal.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/yzal

.. |wheel| image:: https://img.shields.io/pypi/wheel/yzal.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/yzal

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/yzal.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/yzal

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/yzal.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/yzal

