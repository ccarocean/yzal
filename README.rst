yzal |build-status| |coverage-status|
=======================================

WORK IN PROGRESS - This will be removed upon first release.

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

* Python 3.5 or greater


.. |build-status| image:: https://travis-ci.org/mrshannon/yazl.svg?branch=master&style=flat
   :target: https://travis-ci.org/mrshannon/yazl
   :alt: Build status
.. |coverage-status| image:: http://codecov.io/github/mrshannon/yazl/coverage.svg?branch=master
   :target: http://codecov.io/github/mrshannon/yazl?branch=master
   :alt: Test coverage
