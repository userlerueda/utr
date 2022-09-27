"""score commands"""

__author__ = "Luis Rueda"
__email__ = "userlerueda@gmail.com"
__maintainer__ = "Luis Rueda <userlerueda@gmail.com>"

import click
import daiquiri

from utr import UTR
from utr.settings import Settings
from utr.util import convert_to_utr_date, from_string_score, to_utr_score

LOGGER = daiquiri.getLogger(__name__)


@click.group()
def score():
    """Score command"""
    pass


@click.command()
@click.pass_context
@click.argument("date")
@click.argument("player1")
@click.argument("player2")
@click.argument("score")
@click.option(
    "--dry-run/--no-dry-run",
    help="Simulate sending data to UTR",
    default=True,
)
@click.option(
    "--result-id",
    help="Result ID for an existing result, this will update the results",
)
def post(
    ctx: dict,
    date: str,
    player1: str,
    player2: str,
    score: str,
    dry_run: str,
    result_id: int,
):
    """Report Club Match Score."""
    club_id = Settings().dict().get("club_id")
    my_utr: UTR = ctx.obj["my_utr"]
    my_utr.login()
    match_date = convert_to_utr_date(date)
    match_score = to_utr_score(from_string_score(score))
    LOGGER.debug("Match date is %s", match_date)
    LOGGER.debug("Match score is %s", match_score)

    try:
        my_utr.post_result(
            club_id,
            match_date,
            match_score
            | {
                "teamType": "S",
                "winner1": {"id": int(player1)},
                "loser1": {"id": int(player2)},
            },
            dry_run=dry_run,
            result_id=result_id,
        )
    except Exception as err:
        LOGGER.error("Score was not submitted: %s", err, exc_info=not dry_run)


@click.command()
@click.pass_context
@click.argument("result-id")
def get(ctx: dict, result_id: int):
    """Get Club Match Score."""
    my_utr: UTR = ctx.obj["my_utr"]
    my_utr.login()

    try:
        my_utr.get_score(result_id)
    except Exception as err:
        LOGGER.error("Score was not submitted: %s", err)


score.add_command(post)
score.add_command(get)
