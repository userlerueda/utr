"""Main module"""

__author__ = "Luis Rueda"
__email__ = "userlerueda@gmail.com"
__maintainer__ = "Luis Rueda <userlerueda@gmail.com>"

import re

import daiquiri

LOGGER = daiquiri.getLogger(__name__)


def convert_to_utr_score(score: dict) -> dict:
    """Convert interim score to UTR score."""
    winner = score["winner"]
    loser = score["loser"]
    if score["player1"]["id"] == winner:
        winner_player = "player1"
        loser_player = "player2"
    else:
        winner_player = "player2"
        loser_player = "player1"

    utr_score = {
        "teamType": "S",
        "isWinner": True,
        "winner1": {"id": winner},
        "loser1": {"id": loser},
        "winnerSet1": "",
        "loserSet1": "",
        "winnerSet2": "",
        "loserSet2": "",
        "winnerSet3": "",
        "loserSet3": "",
    }

    for set_number in range(1, score["total_sets"] + 1):
        if score["score"][set_number]["winner"] == winner_player:
            utr_score[f"winnerSet{set_number}"] = score["score"][set_number][
                f"{winner_player}_score"
            ]
            utr_score[f"loserSet{set_number}"] = score["score"][set_number][
                f"{loser_player}_score"
            ]
        else:
            utr_score[f"winnerSet{set_number}"] = score["score"][set_number][
                f"{loser_player}_score"
            ]
            utr_score[f"loserSet{set_number}"] = score["score"][set_number][
                f"{winner_player}_score"
            ]
        if score["score"][set_number]["was_tiebreak"]:
            utr_score[f"tiebreakerSet{set_number}"] = score["score"][
                set_number
            ]["tiebreak_low_score"]

    return utr_score


def get_set_score(set_score: str):
    """Get set score."""
    parsed_set_score = {
        "winner": None,
        "player1_score": None,
        "player2_score": None,
        "was_tiebreak": False,
        "tiebreak_low_score": None,
    }

    if len(set_score) == 2:
        LOGGER.debug("Set is regular set: %s", set_score)
        if abs(int(set_score[0]) - int(set_score[1])) >= 2:
            if int(set_score[0]) > int(set_score[1]):
                parsed_set_score["winner"] = "player1"
                parsed_set_score["player1_score"] = int(set_score[0])
                parsed_set_score["player2_score"] = int(set_score[1])
            else:
                parsed_set_score["winner"] = "player2"
                parsed_set_score["player1_score"] = int(set_score[1])
                parsed_set_score["player2_score"] = int(set_score[0])
        else:
            LOGGER.error("Invalid score: %s", set_score)
            raise Exception("Invalid score: %s", set_score)
    elif len(set_score) > 2:
        LOGGER.debug("Set is tiebreak set or match tiebreak: %s", set_score)
        tiebreak_score_regex_set = r"[6-7][6-7]"
        tiebreak_score_regex = rf"({tiebreak_score_regex_set})\s\((\d+)\)"

        matchtiebreak_score_regex = r"\d{2,}\-\d+|\d\-\d{2,}"

        if re.search(tiebreak_score_regex, set_score):
            LOGGER.debug("Set is tiebreak set: %s", set_score)
            parsed_tiebreak_set_score = re.match(
                tiebreak_score_regex, set_score
            )
            if len(parsed_tiebreak_set_score.groups()) == 2:
                tiebreak_set_score = parsed_tiebreak_set_score.groups()[0]
                tiebreak_score = parsed_tiebreak_set_score.groups()[1]
                if (
                    abs(
                        int(tiebreak_set_score[0]) - int(tiebreak_set_score[1])
                    )
                    == 1
                ):
                    if int(tiebreak_set_score[0]) > int(tiebreak_set_score[1]):
                        parsed_set_score["winner"] = "player1"
                        parsed_set_score["player1_score"] = int(
                            tiebreak_set_score[0]
                        )
                        parsed_set_score["player2_score"] = int(
                            tiebreak_set_score[1]
                        )
                    else:
                        parsed_set_score["winner"] = "player2"
                        parsed_set_score["player1_score"] = int(
                            tiebreak_set_score[1]
                        )
                        parsed_set_score["player2_score"] = int(
                            tiebreak_set_score[0]
                        )
                    parsed_set_score["tiebreak_low_score"] = int(
                        tiebreak_score
                    )
                    parsed_set_score["was_tiebreak"] = True
                else:
                    LOGGER.error("Invalid score: %s", set_score)
                    raise Exception("Invalid score: %s", set_score)

        elif re.search(matchtiebreak_score_regex, set_score):
            LOGGER.debug("Set is matchtiebreak set: %s", set_score)
            parsed_matchtiebreak_score = set_score.split("-")
            points_diff = abs(
                int(parsed_matchtiebreak_score[0])
                - int(parsed_matchtiebreak_score[1])
            )
            points_total = int(parsed_matchtiebreak_score[0]) + int(
                parsed_matchtiebreak_score[1]
            )
            if points_diff >= 2 and points_total >= 10:
                if int(parsed_matchtiebreak_score[0]) > int(
                    parsed_matchtiebreak_score[1]
                ):
                    parsed_set_score["winner"] = "player1"
                    parsed_set_score["player1_score"] = 1
                    parsed_set_score["player2_score"] = 0
                else:
                    parsed_set_score["winner"] = "player2"
                    parsed_set_score["player2_score"] = 1
                    parsed_set_score["player1_score"] = 0
                parsed_set_score["was_tiebreak"] = True
                parsed_set_score["tiebreak_low_score"] = min(
                    [
                        int(parsed_matchtiebreak_score[0]),
                        int(parsed_matchtiebreak_score[1]),
                    ]
                )
            else:
                LOGGER.error("Invalid score: %s", set_score)
                raise Exception("Invalid score: %s", set_score)

    else:
        LOGGER.error("Invalid score: %s", set_score)
        raise Exception("Invalid score: %s", set_score)

    return parsed_set_score


def populate_winner(results: dict):
    """Populate winner and looser."""
    player1_id = results["player1"]["id"]
    player2_id = results["player2"]["id"]
    if results["player1"]["sets_won"] / results["total_sets"] > 0.5:
        results["winner"] = player1_id
        results["loser"] = player2_id
    elif results["player2"]["sets_won"] / results["total_sets"] > 0.5:
        results["winner"] = player2_id
        results["loser"] = player1_id
    else:
        raise Exception("Invalid winner: %s", results)
