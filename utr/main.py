"""Main module"""

__author__ = "Luis Rueda"
__email__ = "userlerueda@gmail.com"
__maintainer__ = "Luis Rueda <userlerueda@gmail.com>"


import json
import sys

import click
import daiquiri
import numpy as np
import pandas as pd
from tabulate import tabulate

from utr import UTR
from utr.args import get_args
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
