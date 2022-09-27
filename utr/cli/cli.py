"""results commands"""

__author__ = "Luis Rueda"
__email__ = "userlerueda@gmail.com"
__maintainer__ = "Luis Rueda <userlerueda@gmail.com>"

import click
import daiquiri

from utr import UTR
from utr.cli.player.commands import player
from utr.cli.results.commands import results
from utr.cli.score.commands import score
from utr.settings import Settings


@click.group(help="UTR Command Line Interface")
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
@click.pass_context
def cli(ctx, log_level: str):
    """UTR Command Line Interface."""
    daiquiri.setup(level=log_level.upper())
    ctx.ensure_object(dict)
    email = Settings().dict().get("email")
    password = Settings().dict().get("password")
    my_utr = UTR(email, password)
    ctx.obj["my_utr"] = my_utr


cli.add_command(score)
cli.add_command(results)
cli.add_command(player)
