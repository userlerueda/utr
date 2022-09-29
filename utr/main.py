"""Main module"""

__author__ = "Luis Rueda"
__email__ = "userlerueda@gmail.com"
__maintainer__ = "Luis Rueda <userlerueda@gmail.com>"


import json

import click
import daiquiri
import numpy as np
import pandas as pd
from tabulate import tabulate

from utr import UTR
from utr.cli import cli
from utr.settings import Settings

LOGGER = daiquiri.getLogger(__name__)


@click.command()
@click.option(
    "-L",
    "--log-level",
    help="Log level",
    default=Settings().dict().get("log_level"),
    type=click.Choice(
        [
            "CRITICAL",
            "ERROR",
            "WARNING",
            "INFO",
            "DEBUG",
        ],
        case_sensitive=False,
    ),
)
@click.argument("player_id")
@click.option(
    "-S", "--stats/--no-stats", help="Get player stats", default=False
)
def ccp_player(log_level: str, player_id: str, stats: bool):
    """Get player function."""
    daiquiri.setup(level=log_level.upper())
    club_id = Settings().dict().get("club_id")
    cache_file = f"{player_id}.json"
    relevant_columns = [
        "playerId",
        "role",
        "location",
        "firstName",
        "lastName",
        "singlesUtr",
        "ratingStatusSingles",
        "doublesUtr",
        "ratingStatusDoubles",
        "myUtrSingles",
        "myUtrStatusSingles",
        # "myUtrSinglesReliability",
        "myUtrDoubles",
        "myUtrStatusDoubles",
        # "myUtrDoublesReliability",
    ]
    email = Settings().dict().get("email")
    password = Settings().dict().get("password")
    my_utr = UTR(email, password)
    my_utr.login()

    player = my_utr.get_player(player_id)

    # df = pd.json_normalize(members)

    print(json.dumps(player, indent=2))


def get_utr_data(club_id, relevant_columns):
    """Get data from UTR backend."""

    email = Settings().dict().get("email")
    password = Settings().dict().get("password")
    cache_file = f"{club_id}.json"
    additional_players = [
        1710681,
        1965361,
        2607480,
        2938046,
        2938462,
        2942293,
        3093904,
        3093914,
        3513515,
    ]

    my_utr = UTR(email, password)
    my_utr.login()
    club = my_utr.get_club(club_id)
    club_member_count = club.get("memberCount")
    members = my_utr.get_club_members(club_id, count=club_member_count)
    for player_id in additional_players:
        player = my_utr.get_player(player_id)
        player_fields = list(player.keys())
        LOGGER.debug("Got the following fields for player: %s", player_fields)
        for key in player_fields:
            if key == "id":
                LOGGER.debug("Changing id to memberId for %s", player)
                player["playerId"] = player["id"]
            if key not in relevant_columns:
                player.pop(key, None)
        members.append(player)
    LOGGER.info("Got %s members", len(members))
    with open(cache_file, "w") as outfile:
        json.dump(members, outfile)
    return members


if __name__ == "__main__":
    cli()
