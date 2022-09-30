"""player commands"""

__author__ = "Luis Rueda"
__email__ = "userlerueda@gmail.com"
__maintainer__ = "Luis Rueda <userlerueda@gmail.com>"

import json

import click
import daiquiri

from utr import UTR

LOGGER = daiquiri.getLogger(__name__)


@click.group()
def player():
    """Score command"""
    pass


@click.command()
@click.pass_context
@click.argument("player_id")
def get_info(ctx, player_id):
    """Get player info"""
    my_utr: UTR = ctx.obj["my_utr"]
    my_utr.login()
    player_stats = my_utr.get_player(player_id)
    print(json.dumps(player_stats, indent=2))


@click.command()
@click.pass_context
@click.argument("club-id")
@click.argument("player-id")
@click.option(
    "--dry-run/--no-dry-run",
    help="Simulate sending data to UTR",
    default=False,
)
def invite_to_club(ctx, club_id: int, player_id: int, dry_run: bool):
    """Invite player to club"""
    my_utr: UTR = ctx.obj["my_utr"]
    my_utr.login()
    operation = my_utr.invite_player_to_club(
        club_id, player_id, dry_run=dry_run
    )
    print(json.dumps(operation, indent=2))


player.add_command(get_info)
player.add_command(invite_to_club)
