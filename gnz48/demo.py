#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib.request


def main():
    url = "http://www.baidu.com"

    # 新的遍历方法?
    with urllib.request.urlopen(url) as f:
        print(f.read(300))



if __name__ == '__main__':
    main()