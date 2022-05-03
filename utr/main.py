"""Main module"""

__author__ = "Luis Rueda"
__email__ = "userlerueda@gmail.com"
__maintainer__ = "Luis Rueda <userlerueda@gmail.com>"


import argparse

import daiquiri

from utr import club, player, search, settings

LOGGER = daiquiri.getLogger(__name__)


def main():
    """Main function."""

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-E",
        "--email",
        default=settings.UTR_EMAIL,
        help="Your UTR email address.",
    )
    parser.add_argument(
        "-P",
        "--password",
        default=settings.UTR_PASSWORD,
        help="Your UTR password.",
    )

    parser.add_argument(
        "-l",
        "--log-level",
        default=settings.LOG_LEVEL_STR,
        help="Logging level (see https://docs.python.org/3/library/logging.html#logging-levels)",
    )

    subparsers = parser.add_subparsers()

    club.add_parser(subparsers)
    player.add_subparsers(subparsers)
    search.add_subparsers(subparsers)

    args = parser.parse_args()
    args.func(args)
