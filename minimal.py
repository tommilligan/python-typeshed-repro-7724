#!/usr/bin/env python

import requests


def upload() -> str:
    """
    Copied verbatim from
    https://requests.readthedocs.io/en/latest/user/advanced/#post-multiple-multipart-encoded-files
    """
    url = 'https://httpbin.org/post'
    multiple_files = [
        ('images', ('foo.png', open('foo.png', 'rb'), 'image/png')),
        ('images', ('bar.png', open('bar.png', 'rb'), 'image/png'))]
    r = requests.post(url, files=multiple_files)
    return r.text


if __name__ == "__main__":
    print(upload())
