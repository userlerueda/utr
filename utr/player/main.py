import daiquiri

from .show import add_show_subparser

LOGGER = daiquiri.getLogger(__name__)


def add_subparsers(subparser):
    """Add the parser for this module to a subparsers object."""
    parser = subparser.add_parser("player")
    subparsers = parser.add_subparsers()
    add_show_subparser(subparsers)


def main(args):
    """Main function."""
    daiquiri.setup(level=args.log_level)
    print("main")
    # my_utr = UTR(args.email, args.password)
    # my_utr.login()
