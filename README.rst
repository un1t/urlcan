URL canonicalization library.
Parses URL and made it valid according to RFC 2396.

Features
========

- It works somehow ;)
- Python 2/3 support

Status
======

Development is at very beginning, not all tests pass.

Usage
=====
::

    >>> from urlcan import canonicalize
    >>> canonicalize("http://host.com/aaa/../../../bbb/%25%32%35%25%32%35")
    'http://host.com/bbb/%25%25'
