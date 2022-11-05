"""UTR module"""

__author__ = "Luis Rueda"
__email__ = "userlerueda@gmail.com"
__maintainer__ = "Luis Rueda <userlerueda@gmail.com>"

import json
from asyncio import events
from typing import List

import daiquiri
import requests

from utr.settings import Settings

LOGGER = daiquiri.getLogger(__name__)


class UTR(object):
    """A class to represent a UTR object."""

    def __init__(self, email: str, password: str) -> None:
        """Initialize the UTR object."""
        self.email = email
        self.password = password
        self.url = Settings().dict().get("url")
        self.auth_url = Settings().dict().get("auth_url")
        self.session = requests.Session()

    def login(self) -> None:
        """Login to UTR."""
        uri = "/v1/auth/login"
        url = f"{self.auth_url}{uri}"
        LOGGER.debug("Using URL: %s", url)
        headers = {"Content-Type": "application/json"}
        body = {"email": self.email, "password": self.password}
        response = self.session.post(
            url,
            headers=headers,
            json=body,
        )
        if response.ok is False:
            raise Exception(f"Error logging in: {response.text}")

    def get_club_members(self, club_id: int, count: int = 50) -> dict:
        """Get Club members."""
        uri = f"/v1/club/{club_id}/clubmembers?count={count}"
        url = f"{self.url}{uri}"
        LOGGER.debug("Using URL: %s", url)
        response = self.session.get(url)
        if response.ok is False:
            raise Exception(f"Error getting members: {response.text}")
        LOGGER.debug(response.json())
        return response.json()

    def get_club(self, club_id: int) -> dict:
        """Get Club."""
        uri = f"/v1/club/{club_id}"
        url = f"{self.url}{uri}"
        LOGGER.debug("Using URL: %s", url)
        response = self.session.get(url)
        if response.ok is False:
            raise Exception(f"Error getting club: {response.text}")
        return response.json()

    def get_event(self, event_id: int) -> dict:
        """Get event details."""
        uri = f"/v1/tms/events/{event_id}"
        url = f"{self.url}{uri}"
        response = self.session.get(url)
        if response.ok is False:
            raise Exception(
                f"Error getting details for event {event_id}: {response.text}"
            )
        return response.json()

    def get_player(self, player_id: str) -> dict:
        """Get Player."""
        uri = f"/v1/player/{player_id}"
        url = f"{self.url}{uri}"
        LOGGER.debug("Using URL: %s", url)
        response = self.session.get(url)
        if response.ok is False:
            response.raise_for_status()

        return response.json()

    def delete_score(self, score_id: int) -> dict:
        """Delete Score."""
        uri = f"/v1/score/{score_id}"
        url = f"{self.url}{uri}"
        response = self.session.delete(url)
        if response.ok is False:
            LOGGER.warning(
                "Problem while deleting score: (%s) %s",
                response.status_code,
                response.text,
            )
            response.raise_for_status()

        if response.json().get("error") is not None:
            LOGGER.warning(
                "Problem while deleting score: (%s) %s",
                score_id,
                response.json().get("error"),
            )
            return False

        return True

    def get_score(self, score_id: int) -> dict:
        """Get Score ID."""

        uri = f"/v1/score/{score_id}"
        url = f"{self.url}{uri}"
        # url = f"https://api.universaltennis.com/v1/score/{score_id}"

        response = self.session.get(url)
        if response.ok is False:
            LOGGER.warning(
                "Problem while retrieving score: (%s) %s",
                response.status_code,
                response.text,
            )
            response.raise_for_status()

        return response.json()

    def get_club_results(
        self,
        club_id: int,
        type: str = "s",
        start: int = 0,
        count: int = 1000,
        optimized: bool = True,
    ):
        """Get Club Results"""
        uri = f"/v1/club/{club_id}/clubresults"
        url = f"{self.url}{uri}"
        params = {
            "type": type,
            "start": start,
            "count": count,
            "optimized": optimized,
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_player_results(
        self,
        player_id: int,
        type: str = "singles",
    ):
        """Get Club Results"""
        uri = f"/v1/player/{player_id}/results"
        url = f"{self.url}{uri}"
        params = {
            "year": "last",
            "type": type,
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def invite_player_to_club(
        self, club_id: int, player_id: int, dry_run: bool = False
    ):
        """Invite members to club."""
        LOGGER.debug("Getting member_id for player_id: %s", player_id)
        player = self.get_player(player_id)
        member_id = player.get("memberId")
        if member_id:
            LOGGER.debug(
                "Inviting player '%s %s' with memberId: '%s' to clubId: '%s'",
                player.get("firstName"),
                player.get("lastName"),
                member_id,
                club_id,
            )
        else:
            LOGGER.error(
                "There was a problem retrieving memberId. Player details are: '%s'",
                player,
            )
        uri = f"/v1/club/{club_id}/members"
        url = f"{self.url}{uri}"
        payload = [{"memberId": member_id}]
        if dry_run:
            LOGGER.info("Would be sending '%s' to '%s'", payload, uri)
            return {}
        else:
            response = self.session.post(url, json=payload)
            response.raise_for_status()
            return response.json()

    def post_result(
        self,
        club_id: int,
        date: str,
        score: dict,
        exclude_from_rating: bool = False,
        dry_run: bool = False,
        result_id: int = None,
        verified: bool = False,
    ):
        """Post Club Match Results."""
        uri = "/v1/score/submit"
        url = f"{self.url}{uri}"
        LOGGER.info("Updating result: %s", result_id)

        payload = {
            "date": date,
            "resultSourceType": 1,
            "excludeFromRating": exclude_from_rating,
            "completed": True,
            "clubId": f"{club_id}",
        } | score

        if verified:
            payload["resultSourceType"] = 0
        if result_id:
            payload["resultId"] = result_id
        if dry_run:
            LOGGER.info(json.dumps(payload, indent=2))
        else:
            response = self.session.post(url, json=payload)
            if response.ok:
                winner1_name = "{} {}".format(
                    response.json()["result"]["players"]["winner1"][
                        "firstName"
                    ],
                    response.json()["result"]["players"]["winner1"][
                        "lastName"
                    ],
                )
                loser1_name = "{} {}".format(
                    response.json()["result"]["players"]["loser1"][
                        "firstName"
                    ],
                    response.json()["result"]["players"]["loser1"]["lastName"],
                )
                LOGGER.info(
                    "Reported date was: %s", response.json()["result"]["date"]
                )
                LOGGER.info("Reported winner was: %s", winner1_name)
                LOGGER.info("Reported loser was: %s", loser1_name)
                LOGGER.info(
                    "Reported score was: %s",
                    response.json()["result"]["score"],
                )
                LOGGER.info(
                    "Reported score was: %s",
                    response.json()["result"]["score"],
                )
                LOGGER.debug(json.dumps(response.json(), indent=2))
            else:
                LOGGER.warning(
                    "Report was not submitted: (%s )%s",
                    response.status_code,
                    response.text,
                )

    def search_clubs(self, query: str, top: int = None) -> dict:
        """Get Clubs."""
        uri = "/v2/search/clubs"
        url = f"{self.url}{uri}"
        LOGGER.debug("Using URL: %s", url)
        params = {"Query": query}
        if top is not None:
            params["Top"] = top
        response = self.session.get(url, params=params)
        if response.ok is False:
            raise Exception(f"Error getting clubs: {response.text}")
        return response.json().get("hits", [])

    def search_player(self, query: str, top: int = 20) -> dict:
        """Search Players."""
        uri = f"/v2/search/players?query={query}&top={top}"
        url = f"{self.url}{uri}"
        LOGGER.debug("Using URL: %s", url)
        response = self.session.get(url)
        if response.ok is False:
            raise Exception(f"Error getting clubs: {response.text}")
        return response.json().get("hits", [])
