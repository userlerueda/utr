# UTR
Universal Tennis Rating python library

![example workflow](https://github.com/userlerueda/utr/actions/workflows/on_push.yml/badge.svg?branch=main) ![GitHub](https://img.shields.io/github/license/userlerueda/utr) ![GitHub all releases](https://img.shields.io/github/downloads/userlerueda/utr/total)

## Description



## Installation

To install the library from Gitub:

```
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

### Using as a Library

## Credits

## License

This project is covered under the terms described in [LICENSE](LICENSE).

## Contributing

See the [Contributing](CONTRIBUTING.md) if you want to contribute.

## Changes

See the [Changelog](CHANGELOG.md) for a full list of changes.
