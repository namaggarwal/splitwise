.. _example:

Examples
========

This part of the documentation lists down the examples. Make sure you have read on
how to :ref:`authenticate <authenticate>`.

Authenticated APIs
------------------

All the examples below require authenticated splitwise object. This means you
should have `consumer key`, `consumer secret` and an access token from the user.

Then you can create an splitwise object like

        >>> from splitwise import splitwise
        >>> s = Splitwise(consumer_key, consumer_secret, access_token)

.. _exCurrentUser:

Getting current user
^^^^^^^^^^^^^^^^^^^^
        >>> u = s.getCurrentUser()
        >>> print(u.getId())
            1234
        >>> print(u.getFirstName())
            Naman

.. _exFriends:

Fetching user's friends
^^^^^^^^^^^^^^^^^^^^^^^

        >>> friends = s.getFriends()
        >>> print(friends[0].getId())
            2234
        >>> print(friends[0].getFirstName())
            Atul

.. _exUpdateUser:

Updating a user
^^^^^^^^^^^^^^^
        >>> u = User()
        >>> u.setId(10)
        >>> u.setFirstName("Naman")
        >>> updatedU, error = s.updateUser(u)
        >>> print(updatedU.getFirstName())
            10
        >>> print(u.getFirstName())
            Naman

.. _exExpenses:

Fetching user's expenses
^^^^^^^^^^^^^^^^^^^^^^^^

        >>> expenses = s.getExpenses(offset=2, limit=10, group_id=10)
        >>> print(expenses[0].getCost())
            20.0

Fetching expense with id
^^^^^^^^^^^^^^^^^^^^^^^^
        >>> expense = s.getExpense(2242)
        >>> print(expense.getCost())
            30.0

.. _exGroups:

Fetching user's groups
^^^^^^^^^^^^^^^^^^^^^^
        >>> groups = s.getGroups()
        >>> print(groups[0].getName())
            Manali

Fetching group with id
^^^^^^^^^^^^^^^^^^^^^^
        >>> group = s.getGroup(99876)
        >>> print(group.getName())
            Manali

.. _exNGroup:

Creating a new group
^^^^^^^^^^^^^^^^^^^^
        >>> from splitwise.group import Group
        >>> group = Group()
        >>> group.setName("testGroup")
        >>> nGroup, errors = s.createGroup(group)
        >>> print(nGroup.getId())
            988773

.. _exAGroup:

Add user to existing group
^^^^^^^^^^^^^^^^^^^^^^^^^^

        >>> from splitwise.user import User
        >>> u = User()
        >>> u.setFirstName("naman")
        >>> u.setLastName("aggarwal")
        >>> u.setEmail("abc@def.com")
        >>> success, user, errors = s.addUserToGroup(u,1234)
        >>> print(success)
            True

.. _exDGroup:

Deleting an existing group
^^^^^^^^^^^^^^^^^^^^^^^^^^
        >>> success, errors = s.deleteGroup(123445)
        >>> print(success)
            True

.. _exNExpense:

Creating a new expense
^^^^^^^^^^^^^^^^^^^^^^

        >>> from splitwise.expense import Expense
        >>> expense = Expense()
        >>> expense.setCost("10.0")
        >>> expense.setDescription("testing")
        >>> user1 = ExpenseUser()
        >>> user1.setId(79774)
        >>> user1.setPaidShare('10.00')
        >>> user1.setOwedShare('2.0')
        >>> user2 = ExpenseUser()
        >>> user2.setId(281236)
        >>> user2.setPaidShare('0.00')
        >>> user2.setOwedShare('8.00')
        >>> expense.addUser(user1)
        >>> expense.addUser(user2)
        >>> nExpense, errors = s.createExpense(expense)
        >>> print(nExpense.getId())
            123332

.. _exDExpense:

Delete an Expense
^^^^^^^^^^^^^^^^^

        >>> success, errors = s.deleteExpense(123445)
        >>> print(success)
            True


UnAuthenticated APIs
--------------------

Following apis don't require access token. They still require a consumer_key and consumer_secret

        >>> from splitwise import Splitwise
        >>> s = Splitwise(consumer_key, consumer_secret)

.. _exCurrencies:

Fetching currencies
^^^^^^^^^^^^^^^^^^^

        >>> currencies = s.getCurrencies()
        >>> print(currencies[0].getCode())
            SGD

.. _exCategories:

Fetching categories
^^^^^^^^^^^^^^^^^^^

        >>> categories = s.getcategories()
        >>> print(categories[0].getName())
            Groceries

.. _exComments:

Fetching comments
^^^^^^^^^^^^^^^^^

        >>> comments = s.getComments(982430660)
        >>> print(comments[0].getContent())
            I copied this from hangout

.. _exNComment:

Creating a new comment
^^^^^^^^^^^^^^^^^^^^^^

        >>> expense_id = 982430660
        >>> content = "Test for create comment"
        >>> comment, errors = s.createComment(expense_id,content)
        >>> print("content:", comment.getContent())
            content: Test for create comment
