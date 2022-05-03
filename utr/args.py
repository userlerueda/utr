import argparse

import daiquiri

from utr import settings

LOGGER = daiquiri.getLogger(__name__)


def get_args() -> argparse.ArgumentParser:
    """Get arguments from command line."""
    parser = argparse.ArgumentParser(
        description="A script to consume information from Universal Tennis Ratings."
    )
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
        "-O", "--output", default="utr.xlsx", help="Output file."
    )
    parser.add_argument(
        "-l",
        "--log-level",
        default=settings.LOG_LEVEL_STR,
        help="Logging level (see https://docs.python.org/3/library/logging.html#logging-levels)",
    )
    args = parser.parse_args()
    return args
