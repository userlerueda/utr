"""player commands"""

__author__ = "Luis Rueda"
__email__ = "userlerueda@gmail.com"
__maintainer__ = "Luis Rueda <userlerueda@gmail.com>"

import json

import click
import daiquiri

from utr import UTR

LOGGER = daiquiri.getLogger(__name__)


@click.command()
@click.pass_context
@click.argument("player_id")
def player(ctx, player_id):
    """Player commands"""
    my_utr: UTR = ctx.obj["my_utr"]
    my_utr.login()
    player_stats = my_utr.get_player(player_id)
    print(json.dumps(player_stats, indent=2))
