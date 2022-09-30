# UTR
Universal Tennis Rating python library

![example workflow](https://github.com/userlerueda/utr/actions/workflows/on_push.yml/badge.svg?branch=main) ![GitHub](https://img.shields.io/github/license/userlerueda/utr) ![GitHub all releases](https://img.shields.io/github/downloads/userlerueda/utr/total)

## Description

## Installation

To install the latest version:

```bash
pip install utr
```

To install the library from GitHub:

```bash
pip install git+https://github.com/userlerueda/utr.git
```

## Usage Guide

### Using via CLI

#### Getting Player Information

```bash
$ utr player 909618
{
  "eventViewModel": null,
  "id": "909618",
  "firstName": "German Andres",
  "lastName": "Castillo Contreras",
  "gender": "M",
  "city": "Bogot\u00e1",
  "state": "Bogota",
  "hasYobOnly": false,
  "singlesUtr": 0.0,
  "singlesUtrDisplay": "0.xx",
  "ratingStatusSingles": "Unrated",
  "ratingProgressSingles": "0",
  "ratingStatusImgageSingles": null,
  "doublesUtr": 0.0,
  "doublesUtrDisplay": "0.xx",
  "ratingStatusDoubles": "Unrated",
  "ratingProgressDoubles": "0",
  "ratingStatusImgageDoubles": null,
  "importSource": null,
  "nationality": "COL",
  "myUtrSingles": 0.0,
  "myUtrSinglesDisplay": "0.xx",
  "myUtrStatusSingles": "Unrated",
  "myUtrDoubles": 0.0,
  "myUtrDoublesDisplay": "0.xx",
  "myUtrStatusDoubles": "Unrated",
  "finalPbr": null,
  "pbrRatingDisplay": null,
  "memberId": 91765,
  "utrRange": {
    "minUtr": 5.25,
    "maxUtr": 7.25,
    "lastReliableRating": null,
    "lastReliableRatingDate": null,
    "minUtrDisplay": "5.xx",
    "maxUtrDisplay": "7.xx",
    "lastReliableRatingDisplay": "0.xx",
    "pbrRange": null
  },
  "historicRatings": {
    "historicSinglesRating": null,
    "historicSinglesRatingReliability": null,
    "historicSinglesRatingDate": null,
    "historicDoublesRating": null,
    "historicDoublesRatingReliability": null,
    "historicDoublesRatingDate": null,
    "historicSinglesRatingDisplay": "0.xx",
    "historicDoublesRatingDisplay": "0.xx"
  }
}
```

#### Getting Results for a Club

```bash
$ utr results 12610
+--------------+------------+-------------+---------------------+----------------------------------+-------------+--------------------------------+------------+--------------+---------------------+------------------+
| event        | event_id   |   result_id | date                | winner                           |   winner_id | loser                          |   loser_id | sourceType   | excludeFromRating   | score            |
|--------------+------------+-------------+---------------------+----------------------------------+-------------+--------------------------------+------------+--------------+---------------------+------------------|
| Club Matches |            |    34601132 | 2022-09-24T21:00:00 | Pablo LEMUS                      |     2581102 | Jorge González                 |    3525582 | myutr        | False               | 6-2 6-2          |
...
...
...
| Club Matches |            |    34590366 | 2022-02-19T19:00:00 | Ana María Peláez                 |     3541392 | Pablo Rico                     |    3178932 | myutr        | False               | 2-6 6-2 10-7     |
+--------------+------------+-------------+---------------------+----------------------------------+-------------+--------------------------------+------------+--------------+---------------------+------------------+
```

#### Inviting Players to Club

```bash
❯ utr player invite-to-club 12610 2938046
[
  {
    "email": "xxxxxxx@gmail.com",
    "invited": false,
    "result": "Member Already Invited"
  }
]
```

### Using as a Library

The package can also be used directly as a library

To do so, first import utr package and then create an object from the UTR class:

```python
from utr import UTR

my_utr = UTR(email, password)
my_utr.login()
```

#### Inviting Players to Club

```python
operation = my_utr.invite_player_to_club(club_id, player_id)
```

## Credits

Credits to https://blakestevenson.github.io/utr-api-docs/ for trying to document the API.

## License

This project is covered under the terms described in [LICENSE](LICENSE).

## Contributing

See the [Contributing](CONTRIBUTING.md) if you want to contribute.

## Changes

See the [Changelog](CHANGELOG.md) for a full list of changes.
