Splitwise Python SDK
=====================================

Release v\ |version| (:ref:`Installation <install>`)

.. image:: https://pepy.tech/badge/splitwise
    :target: https://pepy.tech/project/splitwise

.. image:: https://img.shields.io/pypi/l/splitwise.svg
    :target: https://pypi.org/project/splitwise/

.. image:: https://img.shields.io/pypi/wheel/splitwise.svg
    :target: https://pypi.org/project/splitwise/

.. image:: https://img.shields.io/pypi/pyversions/splitwise.svg
    :target: https://pypi.org/project/splitwise/

**splitwise** is a Python SDK library to automate Splitwise.

-------------------

**It's simple to use**::

      >>> s = Splitwise("consumer_key", "consumer_secret")
      >>> s.setAccessToken(access_token)
      >>> s.getCurrentUser().getId()
      78322
      >>> expense = Expense()
      >>> expense.setGroupId("19433671")
      >>> expense.setSplitEqually()
      >>> expense.setCost("10")
      >>> created_expense, errors = s.createExpense(expense)
      >>> created_expense.getId()
      897763

**Splitwise** SDK uses **requests** to make the HTTP requests to splitwise on your behalf.

Features
--------

splitwise SDK supports

- Fetching current user info
- Fetching user's friends
- Fetching user's expenses
- Fetching user's groups
- Fetching currencies
- Fetching categories
- Creating a new group
- Creating a new expense
- Deleting an existing group

Splitwise officially supports Python 2.7 & 3.4–3.7, and runs great on PyPy.

The API Documentation / Guide
-----------------------------

If you are looking for information on a specific function, class, or method,
this part of the documentation is for you.

.. toctree::
   :maxdepth: 2

   api

.. toctree::
   :maxdepth: 3
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
