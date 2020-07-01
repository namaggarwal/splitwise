.. _install:

Installation of splitwise
=========================

This covers the installation of splitwise

Using pip
---------

To install splitwise, simply run this simple command in your terminal of choice::

        $ pip install splitwise

Get the source code
-------------------

Splitwise is actively developed on GitHub, where the code is
`always available <https://github.com/namaggarwal/splitwise>`_.

You can either clone the public repository::

    $ git clone git://github.com/namaggarwal/splitwise.git

Or, download the `tarball <https://github.com/namaggarwal/splitwise/tarball/master>`_::

    $ curl -OL https://github.com/namaggarwal/splitwise/tarball/master
    # optionally, zipball is also available (for Windows users).

Once you have a copy of the source, you can embed it in your own Python
package, or install it into your site-packages easily::

    $ cd splitwise
    $ pip install .