"""results commands"""

__author__ = "Luis Rueda"
__email__ = "userlerueda@gmail.com"
__maintainer__ = "Luis Rueda <userlerueda@gmail.com>"

import click
import daiquiri
from tabulate import tabulate

from utr import UTR
from utr.util import from_club_results

LOGGER = daiquiri.getLogger(__name__)


@click.command()
@click.pass_context
@click.argument("club_id")
@click.option("--player-id", help="Filter results that include this player ID")
def results(ctx, club_id: int, player_id: int):
    """Results command"""
    my_utr: UTR = ctx.obj["my_utr"]
    my_utr.login()
    results = my_utr.get_club_results(club_id)
    formatted_results = []
    for event in results["events"]:
        for result in event["results"]:

            if player_id is None:

                formatted_results.append(
                    {
                        "event": event["name"],
                        "event_id": event["id"],
                        "result_id": result["id"],
                        "date": result["date"],
                        "winner": "{} {}".format(
                            result["players"]["winner1"]["firstName"],
                            result["players"]["winner1"]["lastName"],
                        ),
                        "winner_id": result["players"]["winner1"]["id"],
                        "loser": "{} {}".format(
                            result["players"]["loser1"]["firstName"],
                            result["players"]["loser1"]["lastName"],
                        ),
                        "loser_id": result["players"]["loser1"]["id"],
                        "sourceType": result["sourceType"],
                        "excludeFromRating": result["excludeFromRating"],
                        "score": from_club_results(result),
                    }
                )

            elif (
                result["players"]["winner1"]["id"] == player_id
                or result["players"]["loser1"]["id"] == player_id
            ):
                formatted_results.append(
                    {
                        "event": event["name"],
                        "event_id": event["id"],
                        "result_id": result["id"],
                        "date": result["date"],
                        "winner": "{} {}".format(
                            result["players"]["winner1"]["firstName"],
                            result["players"]["winner1"]["lastName"],
                        ),
                        "winner_id": result["players"]["winner1"]["id"],
                        "loser": "{} {}".format(
                            result["players"]["loser1"]["firstName"],
                            result["players"]["loser1"]["lastName"],
                        ),
                        "loser_id": result["players"]["loser1"]["id"],
                        "sourceType": result["sourceType"],
                        "excludeFromRating": result["excludeFromRating"],
                        "score": from_club_results(result),
                    }
                )

    print(
        tabulate(
            formatted_results,
            headers="keys",
            tablefmt="psql",
        )
    )
