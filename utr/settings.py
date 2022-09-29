from pydantic import BaseSettings


class Settings(BaseSettings):
    """ "Settings."""

    email: str
    password: str
    url: str = "https://api.universaltennis.com"
    auth_url: str = "https://app.universaltennis.com/api"
    club_id: int = 12610
    log_level: str = "INFO"

    class Config:
        """Config."""

        env_prefix = "utr_"
        fields = {
            "utr_email": {"env": "utr_email"},
            "utr_password": {"env": "utr_password"},
        }
