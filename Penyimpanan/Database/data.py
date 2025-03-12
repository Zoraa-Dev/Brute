#!/usr/bin/env python3
# -*- coding:utf-8

try:
    import os, requests, re, json, time
    import random, datetime, uuid, pytz, hmac, hashlib, urllib, shutil, binascii, struct, base64
    from Cryptodome import Random
    from Cryptodome.Cipher import AES, PKCS1_v1_5
    from nacl.public import PublicKey, SealedBox
    from rich.console import Console
    from rich.panel import Panel
    from rich.tree import Tree
    from rich import print as printz
    from concurrent.futures import ThreadPoolExecutor
except(ModuleNotFoundError) as e:
    try:
        from urllib.parse import quote
        __import__('os').system(f'xdg-open https://wa.me/6283140199711?text=INSTAGRAM%20ERROR%20%3A%20{quote(str(e))}')
        exit()
    except(Exception, KeyboardInterrupt) as e:
        from urllib.parse import quote
        __import__('os').system(f'xdg-open https://wa.me/6283140199711?text=INSTAGRAM%20ERROR%20%3A%20{quote(str(e))}')
        exit()