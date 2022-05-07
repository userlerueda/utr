import daiquiri
from pandas import json_normalize

from utr import UTR

LOGGER = daiquiri.getLogger(__name__)


def add_parser(subparsers):
    """Add the parser for this module to a subparsers object."""
    parser = subparsers.add_parser("club")
    parser.add_argument(
        "-O", "--output", default="club.xlsx", help="Output file."
    )
    parser.set_defaults(func=main)


def main(args):
    """Main function."""
    # my_args = args.get_args()
    daiquiri.setup(level=args.log_level)
    my_utr = UTR(args.email, args.password)
    my_utr.login()
    club = my_utr.get_club("12610")
    club_member_count = club.get("memberCount")
    members = my_utr.get_club_members("12610", count=club_member_count)
    LOGGER.debug("Got %s members", len(members))
    pd_members = json_normalize(members)
    pd_members.to_excel(args.output, sheet_name="CCP")
