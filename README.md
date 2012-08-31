Gitolite Manager
================

Manage gitolite config and ssh keys.


## Installation

    $ sudo pip install gitolite-manager

or alternatively (you really should be using pip though):

    $ sudo easy_install gitolite-manager

From source:

    $ sudo python setup.py install


## Getting Started

### Add/remove repositories

    >>> import gitolite_manager
    >>> gitolite = gitolite_manager.Gitolite()
    >>> gitolite.addRepo('username', 'reponame')
    True
    >>> gitolite.getRepos()
    {'username/reponame': [('RW+', 'username')]}
    >>> gitolite.rmRepo('username', 'reponame')
    True
    >>> gitolite.getRepos()
    {}


