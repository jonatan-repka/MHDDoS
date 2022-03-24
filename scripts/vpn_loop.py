#!/usr/bin/env python3

import random
import subprocess
from contextlib import contextmanager

from utils import setup_logger, get_my_ip, run_mhddos


LOW_TRAFFIC_RETRIES = 10

VPN_LOCATIONS = [
    "is", "no", "dk", "be", "fi", "gr", "pt", "at", "am", "pl", "lt", "ee", "cz", "ad", "me", "ba", "lu", "hu", "bg",
    "by", "mt", "li", "cy", "al", "hr", "si", "sk", "mc", "je", "mk", "md", "rs", "ge", "za", "il", "eg", "ke", "dz",
]


@contextmanager
def vpn(location):
    logger.info("Connecting to: %s", location)
    subprocess.check_call(["expressvpn", "connect", location], stderr=subprocess.STDOUT)
    logger.info("Connected! My IP: %s", get_my_ip())
    yield
    logger.info("Disconnecting from: %s", location)
    subprocess.check_call(["expressvpn", "disconnect"], stderr=subprocess.STDOUT)


def vpn_loop(args):
    random.shuffle(VPN_LOCATIONS)
    for location in VPN_LOCATIONS[:LOW_TRAFFIC_RETRIES]:
        with vpn(location):
            run_mhddos(logger, args)


ARGS_LIST = list({

})


def main():
    random.shuffle(ARGS_LIST)
    for args in ARGS_LIST:
        vpn_loop(args)


if __name__ == "__main__":
    logger = setup_logger("VPNLoop")
    logger.info("Here already!")
    try:
        main()
    except Exception:
        logger.exception("Shooting down vpn loop")
        raise
