import yaml
from typing import Dict
from pathlib import Path

import pyotp
from tabulate import tabulate

CONFIG_FOLDER = ".2fa"
CONFIG_FILE = "codes.yaml"


def main() -> None:
    try:
        codes = _get_codes()
    except Exception:
        _show_config_error()
    else:
        _print_2fauth(codes)


def _print_2fauth(codes: Dict[str, str]) -> None:
    print(tabulate(_get_otp_dict(codes).items(), headers=["Service", "Code"],))


def _get_otp_dict(codes: Dict[str, str]) -> Dict[str, str]:
    return {service: pyotp.TOTP(code).now() for service, code in codes.items()}


def _get_codes() -> Dict[str, str]:
    with open(_get_config_file_path(), "r") as stream:
        codes = yaml.safe_load(stream)
    return codes


def _get_config_file_path() -> Path:
    return Path.home() / CONFIG_FOLDER / CONFIG_FILE


def _show_config_error() -> None:
    print(
        f"""You need to create {_get_config_file_path()} with something like:

google: URW6SAFBQPVZUXQY
aws: AQXYE4DJ6QL6P2BZ
github: YF7SUHESY65IU4SS"""
    )
