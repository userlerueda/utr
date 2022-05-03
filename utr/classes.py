"""UTR module"""

__author__ = "Luis Rueda"
__email__ = "userlerueda@gmail.com"
__maintainer__ = "Luis Rueda <userlerueda@gmail.com>"

import daiquiri
import requests

from utr import settings

LOGGER = daiquiri.getLogger(__name__)


class UTR(object):
    """A class to represent a UTR object."""

    def __init__(self, email: str, password: str) -> None:
        """Initialize the UTR object."""
        self.email = email
        self.password = password
        self.url = settings.UTR_URL
        self.session = requests.Session()

    def login(self) -> None:
        """Login to UTR."""
        uri = "/v1/auth/login"
        url = f"{self.url}{uri}"
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

    def get_club_members(self, club_id: str, count: int = 50) -> dict:
        """Get Club members."""
        uri = f"/v1/club/{club_id}/clubmembers?count={count}"
        url = f"{self.url}{uri}"
        LOGGER.debug("Using URL: %s", url)
        response = self.session.get(url)
        if response.ok is False:
            raise Exception(f"Error getting members: {response.text}")
        LOGGER.debug(response.json())
        return response.json()

    def get_club(self, club_id: str) -> dict:
        """Get Club."""
        uri = f"/v1/club/{club_id}"
        url = f"{self.url}{uri}"
        LOGGER.debug("Using URL: %s", url)
        response = self.session.get(url)
        if response.ok is False:
            raise Exception(f"Error getting club: {response.text}")
        return response.json()

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
