.. _api:

Developer Interface
===================

.. module:: splitwise

This part of the documentation covers all the interfaces of Splitwise.

Main Interface
--------------

splitwise has a main class **Splitwise**. All the functionality is provided
via this class.

.. autoclass:: splitwise.Splitwise
   :members:

Modals
------

There are several modal objects in this SDK

User
^^^^

.. autoclass:: splitwise.user.User
   :members:

.. autoclass:: splitwise.user.CurrentUser
   :members:

.. autoclass:: splitwise.user.Friend
   :members:

.. autoclass:: splitwise.user.ExpenseUser
   :members:

Group
^^^^^

.. autoclass:: splitwise.group.Group
   :members:

.. autoclass:: splitwise.group.FriendGroup
   :members:

Expense
^^^^^^^

.. autoclass:: splitwise.expense.Expense
   :members:

Balance
^^^^^^^

.. autoclass:: splitwise.balance.Balance
   :members:

Debt
^^^^

.. autoclass:: splitwise.debt.Debt
   :members:

Picture
^^^^^^^

.. autoclass:: splitwise.picture.Picture
   :members:


Receipt
^^^^^^^

.. autoclass:: splitwise.receipt.Receipt
   :members:

Category
^^^^^^^^

.. autoclass:: splitwise.category.Category
   :members:

Currency
^^^^^^^^

.. autoclass:: splitwise.currency.Currency
   :members:


Errors
------

.. autoclass:: splitwise.error.SplitwiseError
   :members:


Exceptions
----------

SplitwiseBaseException
^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: splitwise.exception.SplitwiseBaseException
   :members:

SplitwiseException
^^^^^^^^^^^^^^^^^^

.. autoclass:: splitwise.exception.SplitwiseException
   :members:

SplitwiseUnauthorizedException
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: splitwise.exception.SplitwiseUnauthorizedException
   :members:

SplitwiseNotAllowedException
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: splitwise.exception.SplitwiseNotAllowedException
   :members:

SplitwiseNotFoundException
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: splitwise.exception.SplitwiseNotFoundException
   :members: