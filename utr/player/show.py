import daiquiri

LOGGER = daiquiri.getLogger(__name__)


def add_show_subparser(subparser):
    """Add the parser for this module to a subparsers object."""
    parser = subparser.add_parser("show")
    parser.add_argument("user_id", help="Player's user id")
    parser.set_defaults(func=show)


def show(args):
    """Show player."""
    daiquiri.setup(level=args.log_level)
    print("show")
    LOGGER.debug(args)
