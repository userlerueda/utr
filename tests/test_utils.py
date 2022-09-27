"""Test utilty module"""

__author__ = "Luis Rueda"
__email__ = "userlerueda@gmail.com"
__maintainer__ = "Luis Rueda <userlerueda@gmail.com>"

from unittest import TestCase

import pytest

from utr.ccp import ccp_score_to_utr_score, get_set_score
from utr.util import (
    convert_to_utr_date,
    from_string_score,
    get_set_score,
    to_utr_score,
)

p1s = "player1_score"
p2s = "player2_score"
tls = "tiebreak_low_score"
wt = "was_tiebreak"
w = "winner"


class TestUtilities:
    @pytest.mark.parametrize(
        "score_array, score",
        [
            (
                [[6, 3], [6, 2]],
                {
                    "isWinner": True,
                    "winnerSet1": 6,
                    "loserSet1": 3,
                    "winnerSet2": 6,
                    "loserSet2": 2,
                    "winnerSet3": "",
                    "loserSet3": "",
                },
            ),
            (
                [[6, 1], [6, 0]],
                {
                    "isWinner": True,
                    "winnerSet1": 6,
                    "loserSet1": 1,
                    "winnerSet2": 6,
                    "loserSet2": 0,
                    "winnerSet3": "",
                    "loserSet3": "",
                },
            ),
            (
                [[6, 3], [2, 6], [10, 6]],
                {
                    "isWinner": True,
                    "winnerSet1": 6,
                    "loserSet1": 3,
                    "winnerSet2": 2,
                    "loserSet2": 6,
                    "winnerSet3": 1,
                    "loserSet3": 0,
                    "tiebreakerSet3": 6,
                },
            ),
            (
                [[7, 6, 5], [2, 6], [10, 0]],
                {
                    "isWinner": True,
                    "winnerSet1": 7,
                    "loserSet1": 6,
                    "tiebreakerSet1": 5,
                    "winnerSet2": 2,
                    "loserSet2": 6,
                    "winnerSet3": 1,
                    "loserSet3": 0,
                    "tiebreakerSet3": 0,
                },
            ),
            (
                [],
                {
                    "isWinner": True,
                    "winnerSet1": "",
                    "loserSet1": "",
                    "winnerSet2": "",
                    "loserSet2": "",
                    "winnerSet3": "",
                    "loserSet3": "",
                    "matchOutcome": "withdrew",
                },
            ),
        ],
    )
    def test_to_utr_score(self, score_array, score):
        """
        Test to_utr_score
        """

        TestCase().assertDictEqual(score, to_utr_score(score_array))

    @pytest.mark.parametrize(
        "score, score_array",
        [
            ("60 60", [[6, 0], [6, 0]]),
            ("W/O", []),
        ],
    )
    def test_from_string_score(self, score, score_array):
        """
        Test valid from_string_score
        """

        TestCase().assertListEqual(score_array, from_string_score(score))

    @pytest.mark.parametrize(
        "set_score, parsed_score",
        [
            ("60", [6, 0]),
            ("10-4", [10, 4]),
            ("76 (5)", [7, 6, 5]),
        ],
    )
    def test_get_set_score(self, set_score, parsed_score):
        """
        Test valid get_set_score
        """

        TestCase().assertListEqual(parsed_score, get_set_score(set_score))


class TestConvertToUTRScore:
    @pytest.mark.parametrize(
        "score, player1, player2, winner, loser, winnerSet1,loserSet1, winnerSet2, loserSet2, winnerSet3, loserSet3",
        [
            ("60 60", 1, 2, 1, 2, 6, 0, 6, 0, "", ""),
            ("75 60", 1, 2, 1, 2, 7, 5, 6, 0, "", ""),
            ("76 (5) 60", 1, 2, 1, 2, 7, 5, 6, 0, "", ""),
        ],
    )
    def test_valid_ccp_score_to_utr_score(
        self,
        score,
        player1,
        player2,
        winner,
        loser,
        winnerSet1,
        loserSet1,
        winnerSet2,
        loserSet2,
        winnerSet3,
        loserSet3,
    ):
        """
        Test valid ccp_score_to_utr_score
        """

        utr_score = {
            "teamType": "S",
            "isWinner": True,
            "winner1": {"id": winner},
            "loser1": {"id": loser},
            "winnerSet1": winnerSet1,
            "loserSet1": loserSet1,
            "winnerSet2": winnerSet2,
            "loserSet2": loserSet2,
            "winnerSet3": winnerSet3,
            "loserSet3": loserSet3,
        }
        TestCase().assertDictEqual(
            utr_score, ccp_score_to_utr_score(player1, player2, score)
        )
