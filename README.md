Gitolite Manager
================

Manage [gitolite](https://github.com/sitaramc/gitolite) config and ssh keys.

*Currently in pre-alpha, not polished at all!*


## Installation

    $ sudo pip install gitolite-manager

or alternatively (you really should be using pip though):

    $ sudo easy_install gitolite-manager

From source:

    $ sudo python setup.py install

## Getting Started

### Prepare gitolite

Add the following line to gitolite configuration file (./gitolite-admin/conf/gitolite.conf)

    include "user_repos.conf"

By default, it'll use `./gitolite-admin` as gitolite directory.

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



### Add/remove ssh keys

    >>> import gitolite_manager
    >>> gitolite = gitolite_manager.Gitolite()
    >>> gitolite.addSSHKey('username', 'keyname', 'ssh key content')
    True
    >>> gitolite.getSSHKeys()
    {'username': ['keyname']}
    >>> gitolite.rmSSHKey('username','keyname')
    True
    >>> gitolite.getSSHKeys()
    {}

