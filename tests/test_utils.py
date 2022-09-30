"""Test utilty module"""

__author__ = "Luis Rueda"
__email__ = "userlerueda@gmail.com"
__maintainer__ = "Luis Rueda <userlerueda@gmail.com>"

from unittest import TestCase

import pytest

from utr.ccp import get_set_score
from utr.util import (
    convert_to_utr_date,
    from_string_score,
    get_set_score,
    to_utr_score,
)


class TestUtilities:
    """Test Utilities Class."""

    @pytest.mark.parametrize(
        "date, time, utr_date",
        [
            ("18/6/2022	9:00", None, "2022-06-18T14:00:00Z"),
            ("18/6/2022", "9:00", "2022-06-18T14:00:00Z"),
            ("Sat. 17/09/2022 5:00 PM", None, "2022-09-17T22:00:00Z"),
            ("Sat. 17/09/2022 17:00", None, "2022-09-17T22:00:00Z"),
            ("Sat. 17/09/2022", "5:00 PM", "2022-09-17T22:00:00Z"),
            ("Sat. 17/09/2022", "17:00", "2022-09-17T22:00:00Z"),
        ],
    )
    def test_convert_to_utr_date(self, date, time, utr_date):
        """
        Test convert_to_utr_date
        """
        if time:
            assert utr_date == convert_to_utr_date(date, time=time)
        else:
            assert utr_date == convert_to_utr_date(date)

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
                [[6, 3], [6, 3, 5, 6]],
                {
                    "isWinner": True,
                    "winnerSet1": 6,
                    "loserSet1": 3,
                    "winnerSet2": "",
                    "loserSet2": "",
                    "winnerSet3": "",
                    "loserSet3": "",
                },
            ),
            (
                ["Walkover"],
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
            (
                ["Not played"],
                {
                    "isWinner": False,
                    "winnerSet1": "",
                    "loserSet1": "",
                    "winnerSet2": "",
                    "loserSet2": "",
                    "winnerSet3": "",
                    "loserSet3": "",
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
