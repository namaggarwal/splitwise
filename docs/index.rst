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

- :ref:`Fetching current user info <exCurrentUser>`
- :ref:`Fetching user's friends <exFriends>`
- :ref:`Updating a user <exUpdateUser>`
- :ref:`Fetching user's expenses <exExpenses>`
- :ref:`Creating a new expense <exNExpense>`
- :ref:`Delete an expense <exDExpense>`
- :ref:`Fetching user's groups <exGroups>`
- :ref:`Creating a new group <exNGroup>`
- :ref:`Adding user to group <exAGroup>`
- :ref:`Deleting an existing group <exDGroup>`
- :ref:`Fetching currencies <exCurrencies>`
- :ref:`Fetching categories <exCategories>`
- :ref:`Fetching comments <exComments>`

Splitwise officially supports Python 2.7 & 3.4–3.7, and runs great on PyPy.

The User Documentation / Guide
------------------------------

If you are looking information on how to use this SDK. This part of documentation
explains that

.. toctree::
   :maxdepth: 3

   user/intro
   user/install
   user/authenticate
   user/example



The API Documentation / Guide
-----------------------------

If you are looking for information on a specific function, class, or method,
this part of the documentation is for you.

.. toctree::
   :maxdepth: 3

   api


Contributing Guide
------------------

If you are looking to contribute to this SDK, this part is for you.

.. toctree::
   :maxdepth: 3

   contri

Donate
------

.. toctree::
   :maxdepth: 3

   donate

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
