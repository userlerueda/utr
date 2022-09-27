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
    "-F",
    "--force",
    help="Force reading information from UTR.com. Default is to read from cached file.",
    is_flag=True,
    default=False,
)
@click.option(
    "-L",
    "--log-level",
    help="Log level",
    default="INFO",
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
@click.option(
    "-O",
    "--output-file",
    help="XLS filename to dump table to.",
    default="ccp.xlsx",
)
def ccp(force: bool, log_level: str, output_file):
    """Main function."""
    email = Settings().dict().get("email")
    password = Settings().dict().get("password")
    club_id = Settings().dict().get("club_id")
    cache_file = f"{club_id}.json"
    daiquiri.setup(level=log_level.upper())
    additional_players = [1965361, 3513515, 2942293, 3566636, 1710681]
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
    if force:
        my_utr = UTR(email, password)
        my_utr.login()
        club = my_utr.get_club(club_id)
        club_member_count = club.get("memberCount")
        members = my_utr.get_club_members(club_id, count=club_member_count)
        for player_id in additional_players:
            player = my_utr.get_player(player_id)
            player_fields = list(player.keys())
            for key in player_fields:
                if key == "id":
                    LOGGER.debug("Changing id to memberId for %s", player)
                    player["playerId"] = player["id"]
                if key not in relevant_columns:
                    player.pop(key, None)
            members.append(player)
        LOGGER.debug("Got %s members", len(members))
        with open(cache_file, "w") as outfile:
            json.dump(members, outfile)
    else:
        # my_utr = UTR(email, password)
        # my_utr.login()
        with open(cache_file) as json_file:
            members = json.load(json_file)

    df = pd.json_normalize(members)
    irrelevant_columns = [
        "claimed",
        "doublesUtrDisplay",
        "isPower",
        "isPowered",
        "isPoweredByClub",
        "isPoweredBySubscription",
        "myUtrDoublesDisplay",
        "myUtrSinglesDisplay",
        "singlesUtrDisplay",
        "myUtrSinglesStatusValue",
        "myUtrDoublesStatusValue",
        "pbrRatingDisplay",
        "firstName",
        "lastName",
        "playerProfileImages.default",
        "playerProfileImages.thumbnail.oneX",
        "playerProfileImages.thumbnail.twoX",
        "playerProfileImages.thumbnail.threeX",
        "playerProfileImages.card.oneX",
        "playerProfileImages.card.twoX",
        "playerProfileImages.card.threeX",
        "playerProfileImages.profile.oneX",
        "playerProfileImages.profile.twoX",
        "playerProfileImages.profile.threeX",
        "playerProfileImages.icon.oneX",
        "playerProfileImages.icon.twoX",
        "playerProfileImages.icon.threeX",
        "utrRange",
        "pbrRatingDisplay.pbrRating",
        "pbrRatingDisplay.pbrBallColor",
        "pbrRatingDisplay.ratingDisplay",
        "pbrRatingDisplay.value",
        "utrRange.pbrRange",
        "utrRange.lastReliableRating",
        "utrRange.lastReliableRatingDate",
        "utrRange.lastReliableRatingDisplay",
        "isPro",
        "clubMemberRoleId",
    ]
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
        "myUtrDoubles",
        "myUtrStatusDoubles",
        "myUtrSinglesReliability",
        "myUtrDoublesReliability",
    ]
    if force:
        try:
            members = get_utr_data(club_id, relevant_columns)
        except Exception as err:
            LOGGER.error("Problem while retrieving UTR data: %s", err)
    else:
        try:
            with open(cache_file) as json_file:
                members = json.load(json_file)
        except Exception as err:
            members = get_utr_data(club_id, relevant_columns)
            LOGGER.error("Problem while retrieving UTR data: %s", err)

    df = pd.json_normalize(members)

    df = df[relevant_columns]
    float_columns = [
        "singlesUtr",
        "doublesUtr",
        "myUtrSingles",
        "myUtrDoubles",
    ]
    df[float_columns] = df[float_columns].apply(pd.to_numeric)
    df = df.round(
        {
            "singlesUtr": 3,
            "doublesUtr": 3,
            "myUtrSingles": 3,
            "myUtrDoubles": 3,
        }
    )
    df[float_columns] = df[float_columns].replace(0, np.nan)
    int_columns = ["playerId"]
    df[int_columns] = df[int_columns].apply(pd.to_numeric)
    df.sort_values(by=["playerId"], inplace=True)
    LOGGER.debug(f"Columns are: {df.dtypes}")
    df.to_excel(
        output_file,
        sheet_name="CCP",
    )
    print(
        tabulate(
            df,
            headers="keys",
            tablefmt="psql",
        )
    )


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

    player = my_utr.get_player(player_id, stats=stats)

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
