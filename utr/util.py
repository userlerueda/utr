"""Utility module"""

__author__ = "Luis Rueda"
__email__ = "userlerueda@gmail.com"
__maintainer__ = "Luis Rueda <userlerueda@gmail.com>"


import re

import daiquiri
import pytz
from dateutil.parser import parse

LOGGER = daiquiri.getLogger(__name__)


def convert_to_utr_date(
    date: str, time: str = None, timezone: str = "-0500"
) -> str:
    """Convert CCP Date to UTR Date."""
    LOGGER.debug(
        "Converting the following date: '%s' and time: '%s'", date, time
    )
    if time:
        date_time = f"{date}T{time} {timezone}"
    else:
        date_time = f"{date} {timezone}"
    date_obj = parse(date_time, dayfirst=True)
    date_str = date_obj.astimezone(pytz.timezone("UTC")).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )
    LOGGER.debug(
        "Date: '%s', Time: '%s', was converted to: '%s'", date, time, date_str
    )

    return date_str


def get_set_score(set_score: str):
    """Get set score."""
    LOGGER.debug("Parsing the following set score: %s", set_score)
    parsed_set_score = []

    if len(set_score) == 2:
        LOGGER.debug("Set is regular set: %s", set_score)
        parsed_set_score.append(int(set_score[0]))
        parsed_set_score.append(int(set_score[1]))
    elif len(set_score) > 2:
        LOGGER.debug("Set is tiebreak set or match tiebreak: %s", set_score)
        tiebreak_score_regex = r"(\d)(\d)\s*\(\s*(\d+)\s*\)"
        matchtiebreak_score_regex = r"\d{2,}\-\d+|\d{2,}\-\d{2,}"

        if re.search(tiebreak_score_regex, set_score):
            LOGGER.debug("Set is tiebreak set: %s", set_score)
            parsed_tiebreak_set_score = re.match(
                tiebreak_score_regex, set_score
            )
            LOGGER.debug(
                "Parsed tiebreak score: %s", parsed_tiebreak_set_score.groups()
            )
            parsed_set_score = [
                int(parsed_score)
                for parsed_score in parsed_tiebreak_set_score.groups()
            ]

        elif re.search(matchtiebreak_score_regex, set_score):
            LOGGER.debug("Set is matchtiebreak set: %s", set_score)
            parsed_matchtiebreak_score = set_score.split("-")
            parsed_set_score.append(int(parsed_matchtiebreak_score[0]))
            parsed_set_score.append(int(parsed_matchtiebreak_score[1]))

    return parsed_set_score


def from_club_results(result: dict) -> str:
    """Convert from Club Results Object."""
    score_list = []
    if result["outcome"] is None:
        for set_number, value in result["score"].items():
            if value["tiebreak"] is None:
                set_score = "{}-{}".format(value["winner"], value["loser"])
            else:
                if set_number == "3" and value["winner"] == 1:
                    set_score = "{}-{}".format(
                        value["winnerTiebreak"], value["tiebreak"]
                    )
                else:
                    set_score = "{}-{} ({})".format(
                        value["winner"], value["loser"], value["tiebreak"]
                    )

            score_list.append(set_score)
    else:
        return result["outcome"]
    return " ".join(score_list)


def from_string_score(string_score: str) -> str:
    """Convert String Score to Score Array."""
    score = []
    regular_set = r"[467][0-5]|[0-5][467]"
    tiebreak_set = r"[6-7][6-7]\s*\(\d+\)"
    matchtiebreak = r"\d{2,}\-\d+|\d\-\d{2,}"

    regex = rf"({regular_set}|{tiebreak_set}|{matchtiebreak})"
    score_list = re.findall(regex, string_score)

    score = [get_set_score(set_score) for set_score in score_list]

    return score


def to_utr_score(score_array) -> dict:
    """Convert Score Array to UTR Score."""
    LOGGER.debug("Processing the following score: '%s'", score_array)
    score = {
        "isWinner": True,
        "winnerSet1": "",
        "loserSet1": "",
        "winnerSet2": "",
        "loserSet2": "",
        "winnerSet3": "",
        "loserSet3": "",
    }

    if len(score_array) == 0:
        # Process Walkover
        score["matchOutcome"] = "withdrew"
        return score

    set_number = 1
    for set_score in score_array:
        if not isinstance(set_score, list):
            return score
        if len(set_score) == 2:
            if set_score[0] >= 10:
                score[f"winnerSet{set_number}"] = 1
                score[f"loserSet{set_number}"] = 0
                score[f"tiebreakerSet{set_number}"] = set_score[1]
            else:
                score[f"winnerSet{set_number}"] = set_score[0]
                score[f"loserSet{set_number}"] = set_score[1]
        elif len(set_score) == 3:
            score[f"winnerSet{set_number}"] = set_score[0]
            score[f"loserSet{set_number}"] = set_score[1]
            score[f"tiebreakerSet{set_number}"] = set_score[2]
        else:
            return score
        set_number += 1
    return score
