#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib.request


def main():
    url = "http://www.gnz48.com"
    gnzRequest = urllib.request.Request(url)
    connection = urllib.request.urlopen(gnzRequest)
    # connection.read()

    print(connection.geturl())
    print(connection.info())
    print(connection.getcode())
    print(connection.msg)
'''
    data = dict()
    data["url"] = connection.geturl()
    data["info"] = connection.info()
    data["code"] = connection.getcode()
    # data["reason"] = connection.msg

    for k, v in data.items():
        print(k + ":" + v)
'''


if __name__ == '__main__':
    main()