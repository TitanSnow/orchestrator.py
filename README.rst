=============
sequencify.py
=============
sequencify port for python

A module for sequencing tasks and dependencies

.. image:: https://api.travis-ci.org/TitanSnow/sequencify.py.svg
  :target: https://travis-ci.org/TitanSnow/sequencify.py
  :alt: build status

Usage
=====
.. code-block:: python

  from sequencify import sequencify

  items = {
    'a': {
      'name': 'a',
      'dep': []
      # other properties as needed
    },
    'b': {
      'name': 'b',
      'dep': ['a']
    },
    'c': {
      'name': 'c',
      'dep': ['a']
    },
    'd': {
      'name': 'd',
      'dep': ['c']
    },
  }

  names = ['d', 'b', 'c', 'a'] # The names of the items you want arranged, need not be all

  results = sequencify(items, names)

  print(results['sequence'])
  # [ 'a', 'c', 'd', 'b' ]
