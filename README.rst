HpEnsem - An experiment in HPO-driven ensembles
###############################################
|Build-Status|

.. code-block:: python

  from hpensem import TBA


.. contents::

.. section-numbering::


Installation
============


To install, clone the repository and run the ``pip install`` command pointing to the repository directory. For example:

.. code-block:: bash

  git clone git@github.com:shaypal5/hpensem.git
  cd hpensem
  pip install .

Or:

.. code-block:: bash

  git clone git@github.com:shaypal5/hpensem.git
  pip install hpensem


Use
===

TBA

Contributing
============

Package author and current maintainer is `Shay Palachy <www.shaypalachy.com>`_ (shay.palachy@gmail.com); You are more than welcome to approach him for help. Contributions are very welcomed.


Installing for development
--------------------------

Clone:

.. code-block:: bash

  git clone git@github.com:shaypal5/hpensem.git


Install in development mode, including test dependencies:

.. code-block:: bash

  cd hpensem
  pip install -e '.[test]'


Running the tests
-----------------

To run all tests use (possibly inside your Python ``virtualenv`` or the project's ``pipenv``):

.. code-block:: bash

  cd hpensem
  pytest

Read ``pytest.ini`` to understand the command line options automatically added to this call (see the ``addopts`` section).

Almost all tests reside in the ``tests`` folder, with the exception of doc tests, which reside inside docstrings, and are also tested.


Adding documentation
--------------------

The project is documented using the `numpy docstring conventions`_, which were chosen as they are perhaps the most widely-spread conventions that are both supported by common tools such as Sphinx and result in human-readable docstrings. When documenting code you add to this project, follow `these conventions`_.

.. _`numpy docstring conventions`: https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt
.. _`these conventions`: https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt

Additionally, if you update this ``README.rst`` file,  use ``python setup.py checkdocs`` to validate it compiles.


.. |Build-Status| image:: https://github.com/shaypal5/hpensem/actions/workflows/test.yml/badge.svg
  :target: https://github.com/shaypal5/hpensem/actions/workflows/test.yml
