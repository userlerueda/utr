"""results commands"""

__author__ = "Luis Rueda"
__email__ = "userlerueda@gmail.com"
__maintainer__ = "Luis Rueda <userlerueda@gmail.com>"

import click
import daiquiri

from utr import UTR
from utr.cli.event.commands import event
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
@click.option(
    "-U",
    "--username",
    default=Settings().dict().get("username"),
    help="Username (e-mail) to be used to log into UTR.",
)
@click.option(
    "-P",
    "--password",
    default=Settings().dict().get("password"),
    help="Password to be used to log into UTR.",
)
@click.pass_context
def cli(ctx, log_level: str, username: str, password: str):
    """UTR Command Line Interface."""
    daiquiri.setup(level=log_level.upper())
    ctx.ensure_object(dict)
    if username is None or password is None:
        raise click.ClickException(
            "Missing username or password, please set it via environment variables or specify via CLI option."
        )
    my_utr = UTR(username, password)
    ctx.obj["my_utr"] = my_utr


cli.add_command(score)
cli.add_command(results)
cli.add_command(player)
cli.add_command(event)
