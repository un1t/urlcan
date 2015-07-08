import os.path
from six.moves.urllib.parse import (
    ParseResult, urlunparse, urldefrag,
    urlparse, parse_qsl, urlencode,
    quote, unquote
)

# https://developers.google.com/safe-browsing/developers_guide_v2#Canonicalization

def canonicalize(url):
    scheme, netloc, path, params, query, fragment = urlparse(url)

    scheme, netloc, path, params, query, fragment = urlparse(url)
    netloc = netloc.strip('.')
    path = canonicalize_path(path)

    fragment = ''
    return urlunparse((scheme, netloc.lower(), path, params, query, fragment))


def canonicalize_path(path):
    prev_path = path
    while True:
        path = unquote(path)
        if path == prev_path:
            break
        prev_path = path
    path = os.path.normpath(path)
    path = quote(path)
    return path

