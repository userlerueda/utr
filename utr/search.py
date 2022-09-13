from pprint import pprint

import daiquiri
from pandas import json_normalize

from utr import UTR

LOGGER = daiquiri.getLogger(__name__)


def main(args):
    """Main function."""
    daiquiri.setup(level=args.log_level)
    my_utr = UTR(args.email, args.password)
    my_utr.login()
    club = my_utr.get_club("12610")
    club_member_count = club.get("memberCount")
    members = my_utr.get_club_members("12610", count=club_member_count)
    LOGGER.debug("Got %s members", len(members))
    pd_members = json_normalize(members)
    pd_members.to_excel(args.output, sheet_name="CCP")


def players(args):
    """Players function."""
    daiquiri.setup(level=args.log_level)
    my_utr = UTR(args.email, args.password)
    my_utr.login()
    search_result = my_utr.search_player(args.query, top=args.top)
    LOGGER.debug("Got %s players", len(search_result))
    pprint(search_result)
