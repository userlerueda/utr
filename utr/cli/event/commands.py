"""event commands"""

__author__ = "Luis Rueda"
__email__ = "userlerueda@gmail.com"
__maintainer__ = "Luis Rueda <userlerueda@gmail.com>"

from pprint import pprint

import click
import daiquiri
from tabulate import tabulate

from utr import UTR

LOGGER = daiquiri.getLogger(__name__)


@click.group()
def event():
    """event command"""
    ...


@click.command()
@click.argument("event-id")
@click.pass_context
def get_registered_players(ctx: dict, event_id: int):
    """Get registered players."""
    my_utr: UTR = ctx.obj["my_utr"]
    LOGGER.info("Getting registered players for event with id '%s'", event_id)
    registered_players = []
    my_utr.login()
    event_details = my_utr.get_event(event_id)
    breakpoint()
    for registered_player_full_details in event_details.pop(
        "registeredPlayers", []
    ):
        registered_player = {}

        for relevant_field in [
            "id",
            "displayName",
            "doublesUtr",
            "ratingProgressDoubles",
            "myUtrDoubles",
            "myUtrProgressDoubles",
            "phone",
            "email",
        ]:
            registered_player[
                relevant_field
            ] = registered_player_full_details.get(relevant_field)
        registered_player["partner"] = registered_player_full_details.get(
            "answers", []
        )[0].get("answer")
        registered_players.append(registered_player)

    print(
        tabulate(
            registered_players,
            headers="keys",
            tablefmt="psql",
        )
    )


event.add_command(get_registered_players)
