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

#### Getting Results for a Club

```bash
$ utr results 12610
+--------------+------------+-------------+---------------------+----------------------------------+-------------+--------------------------------+------------+--------------+---------------------+------------------+
| event        | event_id   |   result_id | date                | winner                           |   winner_id | loser                          |   loser_id | sourceType   | excludeFromRating   | score            |
|--------------+------------+-------------+---------------------+----------------------------------+-------------+--------------------------------+------------+--------------+---------------------+------------------|
| Club Matches |            |    34601132 | 2022-09-24T21:00:00 | Pablo LEMUS                      |     2581102 | Jorge González                 |    3525582 | myutr        | False               | 6-2 6-2          |
| Club Matches |            |    34601146 | 2022-09-24T21:00:00 | Pablo Solano                     |     2732603 | Carolina Vallejo               |    2742658 | myutr        | False               | 6-3 4-6 10-7     |
| Club Matches |            |    34601131 | 2022-09-24T21:00:00 | Daniel Toro Montoya              |     2802877 | Camilo Muñoz Mejia             |    2952990 | myutr        | False               | 6-1 6-0          |
| Club Matches |            |    34601162 | 2022-09-24T21:00:00 | Daniel Giraldo                   |     2814550 | Santiago DUQUE ARANGO          |    2814796 | myutr        | False               | 6-1 6-1          |
| Club Matches |            |    34601167 | 2022-09-24T21:00:00 | Juan Marulanda                   |     3073640 | Juan Pablo Gomez               |    2741663 | myutr        | False               | 2-6 6-4 10-4     |
| Club Matches |            |    34601166 | 2022-09-24T21:00:00 | Ivan Restrepo                    |     3163526 | Felipe Sanint Jaramillo        |    2957597 | myutr        | False               | 6-2 6-1          |
| Club Matches |            |    34601163 | 2022-09-24T21:00:00 | Víctor Salazar Pinillos          |     3526455 | Diego Fernando Gallego Ramirez |    2538723 | myutr        | False               | 6-4 6-3          |
| Club Matches |            |    34601153 | 2022-09-18T21:00:00 | Santiago Mora                    |     1157191 | David Aguirre                  |    3066499 | myutr        | False               | 6-1 6-3          |
| Club Matches |            |    34601139 | 2022-09-18T21:00:00 | Pablo LEMUS                      |     2581102 | Juan Pablo Salazar             |    2847759 | myutr        | False               | 6-4 6-4          |
| Club Matches |            |    34601149 | 2022-09-18T21:00:00 | Pablo Solano                     |     2732603 | Santiago Rios Jimenez          |    2790085 | myutr        | False               | 6-4 6-4          |
| Club Matches |            |    34601189 | 2022-09-18T21:00:00 | Pablo Rueda                      |     2737895 | Rafael Sanint Delgado          |    3093914 | myutr        | False               | 6-2 6-4          |
| Club Matches |            |    34601169 | 2022-09-18T21:00:00 | Juan Pablo Gomez                 |     2741663 | Natalia Londoño Paez           |    2683296 | myutr        | False               | 6-1 6-3          |
| Club Matches |            |    34601148 | 2022-09-18T21:00:00 | Pedro Cardona                    |     2785534 | Jorge Villa                    |    2820925 | myutr        | False               | 6-1 6-4          |
| Club Matches |            |    34601152 | 2022-09-18T21:00:00 | JUAN CARLOS GAVIRIA              |     2790179 | Carlos Gonzalez Bastero        |    1393658 | myutr        | False               | 3-6 6-1 10-3     |
| Club Matches |            |    34601134 | 2022-09-18T21:00:00 | Daniel Toro Montoya              |     2802877 | Jeronimo Duque Salazar         |    3067789 | myutr        | False               | 6-4 7-5          |
| Club Matches |            |    34601164 | 2022-09-18T21:00:00 | Santiago DUQUE ARANGO            |     2814796 | Juan Pablo Echeverri           |    2741519 | myutr        | False               | 6-4 3-6 10-8     |
| Club Matches |            |    34601186 | 2022-09-18T21:00:00 | Samuel Escandon                  |     2938462 | Emilio Sanint Delgado          |    3093904 | myutr        | False               | 6-2 6-2          |
| Club Matches |            |    34601136 | 2022-09-18T21:00:00 | Camilo Muñoz Mejia               |     2952990 | felipe saker                   |    2785793 | myutr        | False               | 6-2 6-4          |
| Club Matches |            |    34601170 | 2022-09-18T21:00:00 | Felipe Sanint Jaramillo          |     2957597 | Gustavo Sanchez                |    2951352 | myutr        | False               | 6-4 6-2          |
| Club Matches |            |    34601171 | 2022-09-18T21:00:00 | Juan Marulanda                   |     3073640 | Martín Vélez                   |    2745683 | myutr        | False               | 6-2 6-3          |
| Club Matches |            |    34601168 | 2022-09-18T21:00:00 | Ivan Restrepo                    |     3163526 | Andres Sossa                   |    3525605 | myutr        | False               | 6-1 6-2          |
| Club Matches |            |    34601172 | 2022-09-18T21:00:00 | Diego Gomez                      |     3523870 | Eduardo Giraldo Garcia         |    2785800 | myutr        | False               | 6-3 6-1          |
| Club Matches |            |    34601137 | 2022-09-18T21:00:00 | Jorge González                   |     3525582 | martin pinzon                  |    1524439 | myutr        | False               | 6-3 4-6 10-2     |
| Club Matches |            |    34601165 | 2022-09-18T21:00:00 | Víctor Salazar Pinillos          |     3526455 | Martin Zuluaga                 |    2585501 | myutr        | False               | 6-1 6-3          |
| Club Matches |            |    34601151 | 2022-09-18T21:00:00 | Pablo Naranjo                    |     3566513 | Rafael Gaviria Esquivel        |    2790180 | myutr        | False               | 6-2 7-5          |
| Club Matches |            |    34601176 | 2022-09-17T22:00:00 | Wilmar Orozco                    |     1357134 | Daniela Salazar Moreno         |    2743044 | myutr        | False               | 5-7 6-2 10-3     |
| Club Matches |            |    34601145 | 2022-09-17T22:00:00 | Pablo LEMUS                      |     2581102 | Simón Pineda Acevedo           |    2578005 | myutr        | False               | 6-1 6-0          |
| Club Matches |            |    34601175 | 2022-09-17T22:00:00 | Juan Pablo Gomez                 |     2741663 | Pedro Gutierrez                |    2785491 | myutr        | False               | 6-1 6-0          |
| Club Matches |            |    34601157 | 2022-09-17T22:00:00 | Carolina Vallejo                 |     2742658 | Luis Rueda                     |    1312175 | myutr        | False               | 6-3 7-6 (4)      |
| Club Matches |            |    34601178 | 2022-09-17T22:00:00 | Eduardo Giraldo Garcia           |     2785800 | Ana Rico                       |    2935240 | myutr        | False               | 3-6 6-1 10-2     |
| Club Matches |            |    34601159 | 2022-09-17T22:00:00 | JUAN CARLOS GAVIRIA              |     2790179 | Marcela Sosa                   |    2873886 | myutr        | False               | 6-2 6-1          |
| Club Matches |            |    34601177 | 2022-09-17T22:00:00 | Julian Ospina                    |     2798703 | Victor Urrea                   |    3189025 | myutr        | False               | 6-1 6-3          |
| Club Matches |            |    34601143 | 2022-09-17T22:00:00 | Alejandro Alvarez                |     2856116 | Mauricio Gonzalez Marin        |    2785794 | myutr        | False               | 6-1 6-0          |
| Club Matches |            |    34601201 | 2022-09-17T22:00:00 | Alicia Guitierrez Vargas         |     2933225 | Martín vaz                     |    3298635 | myutr        | False               | 6-3 6-2          |
| Club Matches |            |    34601173 | 2022-09-17T22:00:00 | Gustavo Sanchez                  |     2951352 | Sebastian Henao                |    2918693 | myutr        | False               | 6-2 7-6 (3)      |
| Club Matches |            |    34601141 | 2022-09-17T22:00:00 | Camilo Muñoz Mejia               |     2952990 | Ricardo Pineda Salazar         |    2787941 | myutr        | False               | 6-1 6-4          |
| Club Matches |            |    34601174 | 2022-09-17T22:00:00 | Felipe Sanint Jaramillo          |     2957597 | Julia Gonzalez Saldarriaga     |    2576435 | myutr        | False               | 6-0 6-3          |
| Club Matches |            |    34601155 | 2022-09-17T22:00:00 | Gustavo Téllez                   |     2974639 | Julian Moreno                  |    3566512 | myutr        | False               | 6-2 6-0          |
| Club Matches |            |    34601160 | 2022-09-17T22:00:00 | David Aguirre                    |     3066499 | Francisco Lanzas               |    2683342 | myutr        | False               | 1-6 6-3 10-5     |
| Club Matches |            |    34601179 | 2022-09-17T22:00:00 | Diego Gomez                      |     3523870 | Jorge Aristizabal              |    2731343 | myutr        | False               | 6-4 6-3          |
| Club Matches |            |    34601142 | 2022-09-17T22:00:00 | Alejandro Toro Montoya           |     3541345 | Juan Gutierrez                 |    2735950 | myutr        | False               | 7-6 (6) 7-5      |
| Club Matches |            |    34601158 | 2022-09-17T22:00:00 | Pablo Naranjo                    |     3566513 | VALENTINA MARIN                |    2743035 | myutr        | False               | 6-3 6-0          |
| Club Match   |            |    34421817 | 2022-09-06T05:12:36 | Luis Javier Castro               |     2932966 | Francisco Lanzas               |    2683342 | myutr        | False               | 6-3 4-6 10-8     |
| Club Match   |            |    34421816 | 2022-09-04T05:11:49 | Andres Sossa                     |     3525605 | Mariana Londoño                |    3168651 | myutr        | False               | 7-6 (2) 6-3      |
| Club Matches |            |    34421812 | 2022-09-02T10:00:00 | Luis Javier Castro               |     2932966 | VALENTINA MARIN                |    2743035 | myutr        | False               | 6-4 7-5          |
| Club Matches |            |    34421811 | 2022-09-02T10:00:00 | Margarita Velasquez              |     3526233 | Andres Gomez                   |    2730492 | myutr        | False               | 3-6 6-4 6-2      |
| Club Matches |            |    34421814 | 2022-09-02T05:10:23 | Juan Pablo Salazar               |     2847759 | Felipe Marín                   |    2848373 | myutr        | False               | 7-6 (2) 3-6 6-1  |
| Club Matches |            |    34421800 | 2022-08-29T10:00:00 | Pablo Solano                     |     2732603 | Luis Javier Castro             |    2932966 | myutr        | False               | 6-4 6-1          |
| Club Matches |            |    34421801 | 2022-08-29T10:00:00 | Andres Mauricio Caceres Arroyave |     3524912 | Daniela Salazar Moreno         |    2743044 | myutr        | True                | 6-1 6-2          |
| Club Matches |            |    34421804 | 2022-08-29T10:00:00 | Andres Sossa                     |     3525605 | Daniela Salazar Moreno         |    2743044 | myutr        | False               | 6-1 6-2          |
| Club Match   |            |    34421810 | 2022-08-27T10:00:00 | Juan Gutierrez                   |     2735950 | felipe saker                   |    2785793 | myutr        | False               | 6-3 6-3          |
| Club Match   |            |    34421805 | 2022-08-26T10:00:00 | Julian Ospina                    |     2798703 | Victor Urrea                   |    3189025 | myutr        | False               | 6-3 6-4          |
| Club Matches |            |    34421798 | 2022-08-25T10:00:00 | Juan Martin Siegel Montoya       |     2941345 | Emma Villa                     |    3071940 | myutr        | False               | 6-1 6-3          |
| Club Matches |            |    34421799 | 2022-08-25T10:00:00 | Mauricio Rendon                  |     3169174 | Juan Pablo Salazar             |    2847759 | myutr        | False               | 6-4 6-1          |
| Club Matches |            |    34421806 | 2022-08-25T10:00:00 | Andres Sossa                     |     3525605 | Victor Urrea                   |    3189025 | myutr        | False               | 6-4 6-2          |
| Club Matches |            |    34421778 | 2022-08-22T10:00:00 | Juan Pablo Echeverri             |     2741519 | Juan Pablo Salazar             |    2847759 | myutr        | False               | 6-4 6-3          |
| Club Matches |            |    34421786 | 2022-08-22T04:43:58 | Gabriel Echeverri                |     2933779 | Pamela Duque Salazar           |    2938390 | myutr        | False               | 1-6 7-6 (4) 10-2 |
| Club Match   |            |    34421780 | 2022-08-21T10:00:00 | Santiago Mora                    |     1157191 | Jorge Villa                    |    2820925 | myutr        | False               | 6-3 7-6 (6)      |
| Club Match   |            |    34421789 | 2022-08-17T10:00:00 | Migue Alejandro Chujfi           |     3172453 | Pablo Rico                     |    3178932 | myutr        | False               | 6-1 6-1          |
| Club Matches |            |    34421757 | 2022-08-09T10:00:00 | Pablo Solano                     |     2732603 | Luis Javier Castro             |    2932966 | myutr        | False               | 6-3 6-3          |
| Club Matches |            |    34421771 | 2022-08-09T04:34:22 | Wilmar Orozco                    |     1357134 | Laura Saker                    |    2748006 | myutr        | False               | 7-6 (4) 6-3      |
| Club Matches |            |    34421584 | 2022-08-09T02:49:57 | Camilo Muñoz Mejia               |     2952990 | Pablo Saker Otero              |    2737821 | myutr        | False               | 1-6 6-0 6-0      |
| Club Matches |            |    34421758 | 2022-08-08T10:00:00 | Eduardo Giraldo Garcia           |     2785800 | Victor Urrea                   |    3189025 | myutr        | False               | 6-2 1-6 6-0      |
| Club Matches |            |    34421754 | 2022-08-08T10:00:00 | Jorge Villa                      |     2820925 | Santiago Mora                  |    1157191 | myutr        | False               | 4-6 6-4 6-3      |
| Club Matches |            |    34421766 | 2022-08-08T10:00:00 | Margarita Velasquez              |     3526233 | Felipe Rios                    |    3187008 | myutr        | False               | 4-6 6-3 6-4      |
| Club Matches |            |    34421548 | 2022-08-08T02:38:12 | Juan Pablo Salazar               |     2847759 | felipe saker                   |    2785793 | myutr        | False               | 6-7 (7) 6-4 6-1  |
| Club Matches |            |    34421752 | 2022-08-06T10:00:00 | Francisco Lanzas                 |     2683342 | Santiago Rios Jimenez          |    2790085 | myutr        | False               | 1-6 6-3 6-4      |
| Club Matches |            |    34421770 | 2022-08-06T10:00:00 | Migue Alejandro Chujfi           |     3172453 | Ana María Peláez               |    3541392 | myutr        | False               | 6-3 6-1          |
| Club Matches |            |    34421767 | 2022-08-06T08:00:00 | Migue Alejandro Chujfi           |     3172453 | Ana María Peláez               |    3541392 | myutr        | False               | 6-3 6-1          |
| Club Matches |            |    34421795 | 2022-08-05T10:00:00 | Samuel Escandon                  |     2938462 | Pablo Rueda                    |    2737895 | myutr        | False               | 6-0 6-0          |
| Club Matches |            |    34421761 | 2022-08-05T10:00:00 | Maria Cristina Pinzón            |     3172448 | Adolfo Rios Gonzalez           |    2787861 | myutr        | True                | 6-3 6-3          |
| Club Matches |            |    34421762 | 2022-08-05T10:00:00 | Maria Cristina Pinzón            |     3172448 | Adriana Ossa Jaramillo         |    3169091 | myutr        | False               | 6-3 6-3          |
| Club Matches |            |    34421183 | 2022-08-05T01:54:43 | Juan felipe Obando               |     3171219 | Juan Pablo Salazar             |    2847759 | myutr        | False               | 7-5 6-2          |
| Club Matches |            |    34426483 | 2022-08-04T10:00:00 | ANA MARIA NEIRA                  |     3108237 | Natalia Londoño Paez           |    2683296 | myutr        | False               | 6-0 6-3          |
| Club Matches |            |    34421631 | 2022-08-04T03:01:32 | Santiago Rios Jimenez            |     2790085 | Pablo Naranjo                  |    3566513 | myutr        | False               | 6-2 3-6 10-4     |
| Club Matches |            |    34450343 | 2022-07-31T14:56:00 | Jorge Villa                      |     2820925 | Santiago Mora                  |    1157191 | myutr        | False               | 6-7 (7) 6-0 10-4 |
| Club Matches |            |    34450355 | 2022-07-31T14:56:00 | Felipe Rios                      |     3187008 | Natalia Ríos                   |    2951353 | myutr        | False               | 6-1 6-1          |
| Club Match   |            |    34450447 | 2022-07-29T14:56:00 | Angelica Varon                   |     3530240 | Johanna Rincón Giraldo         |    3534417 | myutr        | False               | 6-3 6-2          |
| Club Matches |            |    34450371 | 2022-07-27T14:56:00 | ANA MARIA NEIRA                  |     3108237 | Juan Marulanda                 |    3073640 | myutr        | False               | 6-3 6-3          |
| Club Matches |            |    34450467 | 2022-07-27T13:33:05 | felipe saker                     |     2785793 | Juan Gutierrez                 |    2735950 | myutr        | False               | retired          |
| Club Matches |            |    34450742 | 2022-07-26T14:56:00 | Andres Gomez                     |     2730492 | Margarita Velasquez            |    3526233 | myutr        | False               | 6-3 6-2          |
| Club Matches |            |    34450767 | 2022-07-26T14:56:00 | felipe saker                     |     2785793 | Camilo Muñoz Mejia             |    2952990 | myutr        | False               | 6-2 7-5          |
| Club Matches |            |    34450754 | 2022-07-26T14:56:00 | Juan Martin Siegel Montoya       |     2941345 | simon scazani iza              |    3071597 | myutr        | False               | 6-0 6-0          |
| Club Matches |            |    34450750 | 2022-07-26T14:56:00 | Ivan Restrepo                    |     3163526 | Martín Vélez                   |    2745683 | myutr        | False               | 6-7 (8) 6-3 6-4  |
| Club Matches |            |    34450755 | 2022-07-26T14:56:00 | Ivan Restrepo                    |     3163526 | Diego Gomez                    |    3523870 | myutr        | False               | 6-2 6-4          |
| Club Matches |            |    34450736 | 2022-07-26T14:56:00 | Mariana Londoño                  |     3168651 | Wilmar Orozco                  |    1357134 | myutr        | False               | 6-3 6-2          |
| Club Matches |            |    34450500 | 2022-07-26T14:56:00 | Mauricio Rendon                  |     3169174 | felipe saker                   |    2785793 | myutr        | False               | 6-4 6-2          |
| Club Matches |            |    34450737 | 2022-07-26T14:56:00 | Mauricio Rendon                  |     3169174 | Juan Pablo Salazar             |    2847759 | myutr        | False               | 7-5 3-6 6-4      |
| Club Match   |            |    34450739 | 2022-07-23T14:56:00 | Alejandro Alvarez                |     2856116 | Lucas Marulanda                |    2741661 | myutr        | False               | 6-3 6-4          |
| Club Matches |            |    34450843 | 2022-07-19T14:56:00 | Laura Saker                      |     2748006 | Wilmar Orozco                  |    1357134 | myutr        | False               | 6-3 7-5          |
| Club Matches |            |    34450849 | 2022-07-19T14:56:00 | Gabriel Echeverri                |     2933779 | Mariana Guerrero               |    3077538 | myutr        | False               | 6-2 6-2          |
| Club Matches |            |    34450844 | 2022-07-19T14:56:00 | Diego Gomez                      |     3523870 | Marcela Sosa                   |    2873886 | myutr        | False               | 6-2 6-1          |
| Club Match   |            |    34450848 | 2022-07-18T14:56:00 | Ricardo Pineda Salazar           |     2787941 | Mauricio Gonzalez Marin        |    2785794 | myutr        | False               | 7-5 6-0          |
| Club Match   |            |    34450846 | 2022-07-17T14:56:00 | Francisco Lanzas                 |     2683342 | Julian Moreno                  |    3566512 | myutr        | False               | 6-4 4-6 6-3      |
| Club Match   |            |    34450847 | 2022-07-16T14:56:00 | Santiago Rios Jimenez            |     2790085 | Francisco Lanzas               |    2683342 | myutr        | False               | 7-5 6-3          |
| Club Match   |            |    34450842 | 2022-07-14T14:56:00 | Juan Gutierrez                   |     2735950 | Juan Pablo Salazar             |    2847759 | myutr        | False               | 7-5 6-2          |
| Club Match   |            |    34450879 | 2022-07-02T14:56:00 | Migue Alejandro Chujfi           |     3172453 | Alonso Gómez García            |    3541366 | myutr        | False               | 6-3 6-3          |
| Club Match   |            |    34450871 | 2022-07-01T14:56:00 | Felipe Sanint Jaramillo          |     2957597 | Wilmar Orozco                  |    1357134 | myutr        | False               | 5-7 7-6 (4) 6-3  |
| Club Matches |            |    34450924 | 2022-06-27T14:56:00 | Luis Rueda                       |     1312175 | Julian Moreno                  |    3566512 | myutr        | False               | 1-6 6-3 10-4     |
| Club Matches |            |    34450935 | 2022-06-27T14:56:00 | Natalia Londoño Paez             |     2683296 | Julia Gonzalez Saldarriaga     |    2576435 | myutr        | False               | 6-1 3-6 10-6     |
| Club Matches |            |    34450932 | 2022-06-27T14:56:00 | Martín Vélez                     |     2745683 | Victor Urrea                   |    3189025 | myutr        | False               | 6-1 6-3          |
| Club Matches |            |    34450928 | 2022-06-26T14:56:00 | Ivan Restrepo                    |     3163526 | Martín Vélez                   |    2745683 | myutr        | False               | 2-6 6-4 6-3      |
| Club Matches |            |    34450912 | 2022-06-26T14:56:00 | Mauricio Rendon                  |     3169174 | Camilo Muñoz Mejia             |    2952990 | myutr        | False               | 7-5 6-1          |
| Club Match   |            |    34450926 | 2022-06-25T14:56:00 | Margarita Velasquez              |     3526233 | Felipe Estrada                 |    2962922 | myutr        | False               | 6-4 7-5          |
| Club Matches |            |    34450922 | 2022-06-23T14:56:00 | Leonardo Vaz                     |     1357040 | Natalia Ríos                   |    2951353 | myutr        | False               | 6-1 6-1          |
| Club Matches |            |    34450908 | 2022-06-23T14:56:00 | Pablo Solano                     |     2732603 | Luis Javier Castro             |    2932966 | myutr        | False               | 6-3 6-2          |
| Club Match   |            |    34454513 | 2022-06-20T15:58:33 | Martín Vélez                     |     2745683 | Laura Saker                    |    2748006 | myutr        | False               | retired          |
| Club Match   |            |    34454501 | 2022-06-18T14:00:00 | Maria Cristina Pinzón            |     3172448 | Johanna Rincón Giraldo         |    3534417 | myutr        | False               | 5-7 6-4 6-1      |
| Club Match   |            |    34454515 | 2022-06-16T15:59:55 | Pablo Saker Otero                |     2737821 | Federico Gomez                 |    2787919 | myutr        | False               | retired          |
| Club Matches |            |    34478309 | 2022-05-29T02:54:47 | Juan Marulanda                   |     3073640 | Pedro Gutierrez                |    2785491 | myutr        | False               | 6-3 6-3          |
| Club Matches |            |    34478259 | 2022-05-29T02:30:21 | Juan felipe Obando               |     3171219 | Daniel Toro Montoya            |    2802877 | myutr        | False               | 6-4 6-2          |
| Club Matches |            |    34590061 | 2022-05-28T20:00:00 | Juan Marulanda                   |     3073640 | Pedro Gutierrez                |    2785491 | myutr        | False               | 6-3 6-3          |
| Club Matches |            |    34590075 | 2022-05-28T20:00:00 | Juan felipe Obando               |     3171219 | Daniel Toro Montoya            |    2802877 | myutr        | False               | 6-4 6-2          |
| Club Matches |            |    34478308 | 2022-05-23T02:54:25 | Pedro Gutierrez                  |     2785491 | Pamela Duque Salazar           |    2938390 | myutr        | False               | 6-3 6-3          |
| Club Matches |            |    34478307 | 2022-05-23T02:53:52 | Juan Marulanda                   |     3073640 | Manuel Orozco Salazar          |    2933803 | myutr        | False               | 7-6 (3) 2-6 10-3 |
| Club Matches |            |    34478258 | 2022-05-23T02:29:52 | Juan felipe Obando               |     3171219 | Felipe Marín                   |    2848373 | myutr        | False               | 6-1 6-0          |
| Club Matches |            |    34478256 | 2022-05-23T02:29:06 | Daniel Toro Montoya              |     2802877 | Pablo LEMUS                    |    2581102 | myutr        | False               | 7-6 (5) 2-6 10-0 |
| Club Matches |            |    34590071 | 2022-05-22T20:00:00 | Daniel Toro Montoya              |     2802877 | Pablo LEMUS                    |    2581102 | myutr        | False               | 7-6 (5) 2-6 10-0 |
| Club Matches |            |    34590073 | 2022-05-22T20:00:00 | Juan felipe Obando               |     3171219 | Felipe Marín                   |    2848373 | myutr        | False               | 6-1 6-0          |
| Club Matches |            |    34590060 | 2022-05-22T19:00:00 | Pedro Gutierrez                  |     2785491 | Pamela Duque Salazar           |    2938390 | myutr        | False               | 6-3 6-3          |
| Club Matches |            |    34590058 | 2022-05-22T19:00:00 | Juan Marulanda                   |     3073640 | Manuel Orozco Salazar          |    2933803 | myutr        | False               | 7-6 (3) 2-6 10-3 |
| Club Matches |            |    34478305 | 2022-05-22T02:53:23 | Pedro Gutierrez                  |     2785491 | Matias Castro                  |    3004967 | myutr        | False               | 7-5 1-6 10-6     |
| Club Matches |            |    34478303 | 2022-05-22T02:52:58 | Pamela Duque Salazar             |     2938390 | Mariana Guerrero               |    3077538 | myutr        | False               | 6-3 6-3          |
| Club Matches |            |    34478301 | 2022-05-22T02:52:29 | Manuel Orozco Salazar            |     2933803 | simon scazani iza              |    3071597 | myutr        | False               | 6-1 6-3          |
| Club Matches |            |    34478300 | 2022-05-22T02:51:53 | Juan Marulanda                   |     3073640 | Matias Lopez Salazar           |    2932496 | myutr        | False               | 6-4 6-4          |
| Club Matches |            |    34478254 | 2022-05-22T02:28:30 | Daniel Toro Montoya              |     2802877 | Juan Gutierrez                 |    2735950 | myutr        | False               | 6-1 6-0          |
| Club Matches |            |    34590070 | 2022-05-21T20:00:00 | Daniel Toro Montoya              |     2802877 | Juan Gutierrez                 |    2735950 | myutr        | False               | 6-1 6-0          |
| Club Matches |            |    34590057 | 2022-05-21T19:00:00 | Pedro Gutierrez                  |     2785491 | Matias Castro                  |    3004967 | myutr        | False               | 7-5 1-6 10-6     |
| Club Matches |            |    34590056 | 2022-05-21T19:00:00 | Pamela Duque Salazar             |     2938390 | Mariana Guerrero               |    3077538 | myutr        | False               | 6-3 6-3          |
| Club Matches |            |    34478297 | 2022-05-16T02:51:26 | Pedro Gutierrez                  |     2785491 | Juan Martin Siegel Montoya     |    2941345 | myutr        | False               | 3-6 6-4 10-0     |
| Club Matches |            |    34478296 | 2022-05-16T02:51:01 | Matias Castro                    |     3004967 | Jacobo Castro                  |    3033290 | myutr        | False               | 6-0 6-0          |
| Club Matches |            |    34478295 | 2022-05-16T02:50:30 | Mariana Guerrero                 |     3077538 | Pablo Rueda                    |    2737895 | myutr        | False               | 6-3 4-6 10-6     |
| Club Matches |            |    34478294 | 2022-05-16T02:49:50 | Pamela Duque Salazar             |     2938390 | Emiliano Fernández             |    3486715 | myutr        | False               | 6-4 5-7 10-8     |
| Club Matches |            |    34478293 | 2022-05-16T02:48:03 | Juan Marulanda                   |     3073640 | Gabriel Echeverri              |    2933779 | myutr        | False               | 4-6 6-3 10-7     |
| Club Matches |            |    34478289 | 2022-05-16T02:45:22 | Mariana Montoya Gómez            |     3534409 | Ana Maria Alzate               |    3528654 | myutr        | False               | 6-0 6-4          |
| Club Matches |            |    34478286 | 2022-05-16T02:43:03 | CAMILA ECHEVERRI CHAPARRO        |     3525478 | Fernan Fortich Barrios         |    2787912 | myutr        | False               | 6-2 6-2          |
| Club Matches |            |    34478282 | 2022-05-16T02:39:56 | Felipe Sanint Jaramillo          |     2957597 | Laura Saker                    |    2748006 | myutr        | False               | 6-4 6-4          |
| Club Matches |            |    34478272 | 2022-05-16T02:34:56 | Simón Pineda Acevedo             |     2578005 | Mario Cesar DaSilva            |    3528676 | myutr        | False               | 4-6 6-3 10-8     |
| Club Matches |            |    34478271 | 2022-05-16T02:34:18 | Jorge Villa                      |     2820925 | Luis Rueda                     |    1312175 | myutr        | False               | 7-5 6-3          |
| Club Matches |            |    34478270 | 2022-05-16T02:33:39 | Julian Moreno                    |     3566512 | VALENTINA MARIN                |    2743035 | myutr        | False               | 7-5 6-2          |
| Club Matches |            |    34478268 | 2022-05-16T02:32:42 | Rafael Gaviria Esquivel          |     2790180 | Carolina Vallejo               |    2742658 | myutr        | False               | 5-7 6-2 10-2     |
| Club Matches |            |    34478267 | 2022-05-16T02:32:13 | Santiago Mora                    |     1157191 | Carlos Gonzalez Bastero        |    1393658 | myutr        | False               | 6-2 6-1          |
| Club Matches |            |    34478248 | 2022-05-16T02:27:49 | Daniel Toro Montoya              |     2802877 | Ricardo Pineda Salazar         |    2787941 | myutr        | False               | 6-2 6-3          |
| Club Matches |            |    34478229 | 2022-05-16T02:21:14 | Víctor Salazar Pinillos          |     3526455 | Santiago Rico Gaviria          |    3325141 | myutr        | False               | 7-6 (5) 4-6 10-6 |
| Club Matches |            |    34590087 | 2022-05-15T21:00:00 | Simón Pineda Acevedo             |     2578005 | Mario Cesar DaSilva            |    3528676 | myutr        | False               | 4-6 6-3 10-8     |
| Club Matches |            |    34590055 | 2022-05-15T21:00:00 | Pedro Gutierrez                  |     2785491 | Juan Martin Siegel Montoya     |    2941345 | myutr        | False               | 3-6 6-4 10-0     |
| Club Matches |            |    34590051 | 2022-05-15T21:00:00 | Pamela Duque Salazar             |     2938390 | Emiliano Fernández             |    3486715 | myutr        | False               | 6-4 5-7 10-8     |
| Club Matches |            |    34590054 | 2022-05-15T21:00:00 | Matias Castro                    |     3004967 | Jacobo Castro                  |    3033290 | myutr        | False               | 6-0 6-0          |
| Club Matches |            |    34590052 | 2022-05-15T21:00:00 | Mariana Guerrero                 |     3077538 | Pablo Rueda                    |    2737895 | myutr        | False               | 6-3 4-6 10-6     |
| Club Matches |            |    34590088 | 2022-05-15T21:00:00 | Víctor Salazar Pinillos          |     3526455 | Santiago Rico Gaviria          |    3325141 | myutr        | False               | 7-6 4-6 10-6     |
| Club Matches |            |    34590102 | 2022-05-15T21:00:00 | Mariana Montoya Gómez            |     3534409 | Ana Maria Alzate               |    3528654 | myutr        | False               | 6-0 6-4          |
| Club Matches |            |    34590085 | 2022-05-15T21:00:00 | Julian Moreno                    |     3566512 | VALENTINA MARIN                |    2743035 | myutr        | False               | 7-5 6-2          |
| Club Matches |            |    34590082 | 2022-05-15T20:00:00 | Santiago Mora                    |     1157191 | Carlos Gonzalez Bastero        |    1393658 | myutr        | False               | 6-2 6-1          |
| Club Matches |            |    34590083 | 2022-05-15T20:00:00 | Rafael Gaviria Esquivel          |     2790180 | Carolina Vallejo               |    2742658 | myutr        | False               | 5-7 6-2 10-2     |
| Club Matches |            |    34590069 | 2022-05-15T20:00:00 | Daniel Toro Montoya              |     2802877 | Ricardo Pineda Salazar         |    2787941 | myutr        | False               | 6-2 6-3          |
| Club Matches |            |    34590081 | 2022-05-15T20:00:00 | Luis Javier Castro               |     2932966 | JUAN CARLOS GAVIRIA            |    2790179 | myutr        | False               | withdrew         |
| Club Matches |            |    34590100 | 2022-05-15T20:00:00 | Felipe Sanint Jaramillo          |     2957597 | Laura Saker                    |    2748006 | myutr        | False               | 6-4 6-4          |
| Club Matches |            |    34590050 | 2022-05-15T19:00:00 | Manuel Orozco Salazar            |     2933803 | Samuel Escandon                |    2938462 | myutr        | False               | 6-3 6-1          |
| Club Matches |            |    34590049 | 2022-05-15T19:00:00 | Juan Marulanda                   |     3073640 | Gabriel Echeverri              |    2933779 | myutr        | False               | 4-6 6-3 10-7     |
| Club Matches |            |    34590107 | 2022-05-15T19:00:00 | CAMILA ECHEVERRI CHAPARRO        |     3525478 | Fernan Fortich Barrios         |    2787912 | myutr        | False               | 6-2 6-2          |
| Club Matches |            |    34478292 | 2022-05-15T02:47:30 | Juan Martin Siegel Montoya       |     2941345 | Emma Villa                     |    3071940 | myutr        | False               | 3-6 6-2 10-7     |
| Club Matches |            |    34478284 | 2022-05-15T02:42:34 | Margarita Velasquez              |     3526233 | Ana María Manriquez Caldera    |    3108296 | myutr        | False               | 6-0 6-0          |
| Club Matches |            |    34478281 | 2022-05-15T02:39:24 | Diego Gomez                      |     3523870 | Eduardo Giraldo Garcia         |    2785800 | myutr        | False               | 6-2 6-4          |
| Club Matches |            |    34478280 | 2022-05-15T02:38:58 | Ana Rico                         |     2935240 | Mariana Gomez                  |    1524441 | myutr        | False               | 6-3 6-2          |
| Club Matches |            |    34478279 | 2022-05-15T02:38:09 | David Aguirre                    |     3066499 | Mariana Londoño                |    3168651 | myutr        | False               | 6-3 6-0          |
| Club Matches |            |    34478277 | 2022-05-15T02:37:44 | Ivan Restrepo                    |     3163526 | Martín Vélez                   |    2745683 | myutr        | False               | 3-6 6-3 10-8     |
| Club Matches |            |    34478276 | 2022-05-15T02:37:17 | Wilmar Orozco                    |     1357134 | Jorge Aristizabal              |    2731343 | myutr        | False               | 6-4 6-3          |
| Club Matches |            |    34478275 | 2022-05-15T02:36:23 | Andres Sossa                     |     3525605 | Natalia Londoño Paez           |    2683296 | myutr        | False               | 6-4 6-0          |
| Club Matches |            |    34478274 | 2022-05-15T02:35:50 | Pedro Cardona                    |     2785534 | Gustavo Sanchez                |    2951352 | myutr        | False               | 6-0 6-0          |
| Club Matches |            |    34478263 | 2022-05-15T02:31:44 | Simón Pineda Acevedo             |     2578005 | Christian Scanzani             |    3521270 | myutr        | False               | 6-3 6-4          |
| Club Matches |            |    34478262 | 2022-05-15T02:31:09 | Carolina Vallejo                 |     2742658 | Marcela Sosa                   |    2873886 | myutr        | False               | 7-5 6-3          |
| Club Matches |            |    34478244 | 2022-05-15T02:27:12 | Jeronimo Duque Salazar           |     3067789 | Lucas Marulanda                |    2741661 | myutr        | False               | 6-2 6-2          |
| Club Matches |            |    34478241 | 2022-05-15T02:26:30 | Juan felipe Obando               |     3171219 | Jorge González                 |    3525582 | myutr        | False               | 5-7 6-1 10-6     |
| Club Matches |            |    34478239 | 2022-05-15T02:25:38 | martin pinzon                    |     1524439 | felipe saker                   |    2785793 | myutr        | False               | 7-5 6-3          |
| Club Matches |            |    34478236 | 2022-05-15T02:24:04 | Juan Gutierrez                   |     2735950 | Camilo Muñoz Mejia             |    2952990 | myutr        | False               | 6-1 6-3          |
| Club Matches |            |    34478235 | 2022-05-15T02:23:18 | Ricardo Pineda Salazar           |     2787941 | Federico Gomez                 |    2787919 | myutr        | False               | 3-6 6-4 10-2     |
| Club Matches |            |    34590077 | 2022-05-14T21:00:00 | Luis Rueda                       |     1312175 | Matias Mesa Bedoya             |    2607480 | myutr        | False               | withdrew         |
| Club Matches |            |    34590065 | 2022-05-14T21:00:00 | martin pinzon                    |     1524439 | felipe saker                   |    2785793 | myutr        | False               | 7-5 6-3          |
| Club Matches |            |    34590080 | 2022-05-14T21:00:00 | Simón Pineda Acevedo             |     2578005 | Christian Scanzani             |    3521270 | myutr        | False               | 6-3 6-4          |
| Club Matches |            |    34590064 | 2022-05-14T21:00:00 | Pablo LEMUS                      |     2581102 | Juanita Salazar                |    1965361 | myutr        | False               | 6-1 6-1          |
| Club Matches |            |    34590076 | 2022-05-14T21:00:00 | Carolina Vallejo                 |     2742658 | Marcela Sosa                   |    2873886 | myutr        | False               | 7-5 6-3          |
| Club Matches |            |    34588403 | 2022-05-14T21:00:00 | Felipe Marín                     |     2848373 | Juan Guillermo Ramirez Zapata  |    3526852 | myutr        | False               | withdrew         |
| Club Matches |            |    34590068 | 2022-05-14T21:00:00 | Jeronimo Duque Salazar           |     3067789 | Lucas Marulanda                |    2741661 | myutr        | False               | 6-2 6-2          |
| Club Matches |            |    34590067 | 2022-05-14T21:00:00 | Juan felipe Obando               |     3171219 | Jorge González                 |    3525582 | myutr        | False               | 5-7 6-1 10-6     |
| Club Matches |            |    34590092 | 2022-05-14T20:00:00 | Wilmar Orozco                    |     1357134 | Jorge Aristizabal              |    2731343 | myutr        | False               | 6-4 6-3          |
| Club Matches |            |    34590063 | 2022-05-14T20:00:00 | Juan Gutierrez                   |     2735950 | Camilo Muñoz Mejia             |    2952990 | myutr        | False               | 6-1 6-3          |
| Club Matches |            |    34590090 | 2022-05-14T20:00:00 | Laura Saker                      |     2748006 | Sebastian Henao                |    2918693 | myutr        | False               | withdrew         |
| Club Matches |            |    34590089 | 2022-05-14T20:00:00 | Pedro Cardona                    |     2785534 | Gustavo Sanchez                |    2951352 | myutr        | False               | 6-0 6-0          |
| Club Matches |            |    34590062 | 2022-05-14T20:00:00 | Ricardo Pineda Salazar           |     2787941 | Federico Gomez                 |    2787919 | myutr        | False               | 3-6 6-4 10-2     |
| Club Matches |            |    34590096 | 2022-05-14T20:00:00 | Ana Rico                         |     2935240 | Mariana Gomez                  |    1524441 | myutr        | False               | 6-3 6-2          |
| Club Matches |            |    34590095 | 2022-05-14T20:00:00 | David Aguirre                    |     3066499 | Mariana Londoño                |    3168651 | myutr        | False               | 6-3 6-0          |
| Club Matches |            |    34590094 | 2022-05-14T20:00:00 | Ivan Restrepo                    |     3163526 | Martín Vélez                   |    2745683 | myutr        | False               | 3-6 6-3 10-8     |
| Club Matches |            |    34590098 | 2022-05-14T20:00:00 | Diego Gomez                      |     3523870 | Eduardo Giraldo Garcia         |    2785800 | myutr        | False               | 6-2 6-4          |
| Club Matches |            |    34590091 | 2022-05-14T20:00:00 | Andres Sossa                     |     3525605 | Natalia Londoño Paez           |    2683296 | myutr        | False               | 6-4 6-0          |
| Club Matches |            |    34590027 | 2022-05-14T19:00:00 | Gabriel Echeverri                |     2933779 | Rafael Sanint Delgado          |    3093914 | myutr        | False               | 6-1 6-0          |
| Club Matches |            |    34590048 | 2022-05-14T19:00:00 | Juan Martin Siegel Montoya       |     2941345 | Emma Villa                     |    3071940 | myutr        | False               | 3-6 6-2 10-7     |
| Club Matches |            |    34590106 | 2022-05-14T19:00:00 | Felipe Estrada                   |     2962922 | Mariana Saker                  |    2790088 | myutr        | False               | withdrew         |
| Club Matches |            |    34590101 | 2022-05-14T19:00:00 | Adriana Ossa Jaramillo           |     3169091 | Johanna Rincón Giraldo         |    3534417 | myutr        | False               | 6-1 6-3          |
| Club Matches |            |    34590104 | 2022-05-14T19:00:00 | Margarita Velasquez              |     3526233 | Ana María Manriquez Caldera    |    3108296 | myutr        | False               | 6-0 6-0          |
| Club Match   |            |    34454532 | 2022-05-09T11:00:00 | Juan Pablo Salazar               |     2847759 | Martin Zuluaga                 |    2585501 | myutr        | False               | 6-1 1-6 7-6 (3)  |
| Club Matches |            |    34454529 | 2022-05-05T14:00:00 | Juan felipe Obando               |     3171219 | felipe saker                   |    2785793 | myutr        | False               | 6-1 6-4          |
| Club Matches |            |    34454533 | 2022-05-05T12:00:00 | Ivan Restrepo                    |     3163526 | Laura Saker                    |    2748006 | myutr        | False               | 6-2 6-2          |
| Club Matches |            |    34454530 | 2022-05-05T11:00:00 | Juanita Salazar                  |     1965361 | Juan Pablo Salazar             |    2847759 | myutr        | False               | 6-1 6-2          |
| Club Matches |            |    34454531 | 2022-05-05T11:00:00 | Mariana Londoño                  |     3168651 | Victor Urrea                   |    3189025 | myutr        | False               | 6-2 6-2          |
| Club Matches |            |    34466786 | 2022-05-03T23:00:00 | Pablo Saker Otero                |     2737821 | Santiago Rios Jimenez          |    2790085 | myutr        | False               | 3-6 6-4 6-3      |
| Club Matches |            |    34600782 | 2022-05-03T20:00:00 | Pedro Cardona                    |     2785534 | Juan Pablo Gomez               |    2741663 | myutr        | False               | 6-1 6-2          |
| Club Matches |            |    34600493 | 2022-05-03T20:00:00 | Daniel Giraldo                   |     2814550 | Diego Fernando Gallego Ramirez |    2538723 | myutr        | False               | 6-4 6-4          |
| Club Matches |            |    34600889 | 2022-05-03T20:00:00 | Mariana Montoya Gómez            |     3534409 | Viviana Gandur                 |    3107756 | myutr        | False               | 6-3 6-4          |
| Club Matches |            |    34466787 | 2022-05-03T05:00:00 | Juan Guillermo Ramirez Zapata    |     3526852 | felipe saker                   |    2785793 | myutr        | False               | 6-4 6-2          |
| Club Match   |            |    34466784 | 2022-05-02T13:00:00 | Laura Saker                      |     2748006 | Felipe Sanint Jaramillo        |    2957597 | myutr        | False               | 6-2 6-1          |
| Club Matches |            |    34466781 | 2022-04-30T23:00:00 | Juan Pablo Salazar               |     2847759 | Felipe Marín                   |    2848373 | myutr        | False               | 7-6 (5) 6-4      |
| Club Matches |            |    34466766 | 2022-04-30T14:00:00 | Martín Vélez                     |     2745683 | Mariana Londoño                |    3168651 | myutr        | False               | 4-6 6-2 6-4      |
| Club Matches |            |    34466779 | 2022-04-30T12:00:00 | Juan felipe Obando               |     3171219 | Camilo Muñoz Mejia             |    2952990 | myutr        | False               | 6-1 6-3          |
| Club Matches |            |    34466780 | 2022-04-29T23:00:00 | Eduardo Giraldo Garcia           |     2785800 | Wilmar Orozco                  |    1357134 | myutr        | False               | 6-3 6-3          |
| Club Matches |            |    34466765 | 2022-04-29T13:00:00 | Andres Gomez                     |     2730492 | Margarita Velasquez            |    3526233 | myutr        | False               | 6-0 6-3          |
| Club Matches |            |    34466776 | 2022-04-29T13:00:00 | Felipe Sanint Jaramillo          |     2957597 | Wilmar Orozco                  |    1357134 | myutr        | False               | 6-1 6-3          |
| Club Matches |            |    34466774 | 2022-04-28T23:00:00 | felipe saker                     |     2785793 | Camilo Muñoz Mejia             |    2952990 | myutr        | False               | 6-1 7-5          |
| Club Matches |            |    34466763 | 2022-04-28T22:00:00 | Leonardo Vaz                     |     1357040 | Andres Gomez                   |    2730492 | myutr        | False               | 6-0 6-2          |
| Club Match   |            |    34593503 | 2022-03-05T19:00:00 | Matias Gomez Cardona             |     2942293 | Juan Marulanda                 |    3073640 | myutr        | False               | 6-2 6-1          |
| Club Matches |            |    34600494 | 2022-02-27T22:00:00 | Diego Fernando Gallego Ramirez   |     2538723 | Ricardo Castillo               |    2814844 | myutr        | False               | 6-4 6-2          |
| Club Matches |            |    34600781 | 2022-02-27T22:00:00 | Pedro Cardona                    |     2785534 | Mariana Gomez                  |    1524441 | myutr        | False               | 6-1 6-3          |
| Club Matches |            |    34600492 | 2022-02-27T22:00:00 | Daniel Giraldo                   |     2814550 | Nicolas Gomez                  |    2814557 | myutr        | False               | 6-2 6-1          |
| Club Matches |            |    34600948 | 2022-02-27T22:00:00 | Esteban Villegas                 |     3172183 | Tomas Zuluaga Sosa             |    2873899 | myutr        | False               | 6-0 6-4          |
| Club Matches |            |    34590351 | 2022-02-27T21:00:00 | Camilo Muñoz Mejia               |     2952990 | Mario Cesar DaSilva            |    3528676 | myutr        | False               | 6-3 6-1          |
| Club Matches |            |    34590364 | 2022-02-27T20:00:00 | Juan Pablo Gomez                 |     2741663 | Julian Ospina                  |    2798703 | myutr        | False               | 7-5 2-6 10-4     |
| Club Matches |            |    34593499 | 2022-02-27T19:00:00 | Matias Gomez Cardona             |     2942293 | Pedro Gutierrez                |    2785491 | myutr        | False               | 6-4 6-0          |
| Club Matches |            |    34593502 | 2022-02-27T19:00:00 | Juan Marulanda                   |     3073640 | Manuel Orozco Salazar          |    2933803 | myutr        | False               | 7-6 (3) 7-6 (5)  |
| Club Matches |            |    34590357 | 2022-02-26T21:00:00 | Daniel Giraldo                   |     2814550 | Felipe Marulanda Gómez         |    3541279 | myutr        | False               | 6-3 6-0          |
| Club Matches |            |    34590349 | 2022-02-26T21:00:00 | Camilo Muñoz Mejia               |     2952990 | Jorge Villa                    |    2820925 | myutr        | False               | 6-3 6-4          |
| Club Matches |            |    34590350 | 2022-02-26T21:00:00 | Mario Cesar DaSilva              |     3528676 | Rafael Gaviria Esquivel        |    2790180 | myutr        | False               | 6-3 7-5          |
| Club Matches |            |    34600768 | 2022-02-26T20:00:00 | Mariana Gomez                    |     1524441 | Felipe Sanint Jaramillo        |    2957597 | myutr        | False               | 6-3 6-4          |
| Club Matches |            |    34590362 | 2022-02-26T20:00:00 | Juan Pablo Gomez                 |     2741663 | David Aguirre                  |    3066499 | myutr        | False               | 4-6 6-4 10-8     |
| Club Matches |            |    34590363 | 2022-02-26T20:00:00 | Pedro Cardona                    |     2785534 | Mariana Londoño                |    3168651 | myutr        | False               | 6-1 6-4          |
| Club Matches |            |    34600956 | 2022-02-26T20:00:00 | Felipe Rios                      |     3187008 | viviana marcela cardona rincon |    2790093 | myutr        | False               | 6-3 6-4          |
| Club Matches |            |    34590344 | 2022-02-26T19:00:00 | Manuel Orozco Salazar            |     2933803 | Pamela Duque Salazar           |    2938390 | myutr        | False               | 6-4 6-4          |
| Club Matches |            |    34590343 | 2022-02-26T19:00:00 | Juan Marulanda                   |     3073640 | Emma Villa                     |    3071940 | myutr        | False               | 6-0 6-0          |
| Club Matches |            |    34590354 | 2022-02-20T21:00:00 | Juan Pablo Salazar               |     2847759 | Federico Gomez                 |    2787919 | myutr        | False               | 6-3 6-3          |
| Club Matches |            |    34590356 | 2022-02-20T21:00:00 | Santiago Rico Gaviria            |     3325141 | Juan Pablo Echeverri           |    2741519 | myutr        | False               | 4-6 7-6 (4) 10-2 |
| Club Matches |            |    34590355 | 2022-02-20T21:00:00 | Felipe Marulanda Gómez           |     3541279 | Santiago DUQUE ARANGO          |    2814796 | myutr        | False               | 6-1 6-1          |
| Club Matches |            |    34600767 | 2022-02-20T20:00:00 | Mariana Gomez                    |     1524441 | Victor Urrea                   |    3189025 | myutr        | False               | 6-7 (7) 6-3 10-7 |
| Club Matches |            |    34590361 | 2022-02-20T20:00:00 | Pedro Cardona                    |     2785534 | Ivan Restrepo                  |    3163526 | myutr        | False               | 6-2 1-6 10-4     |
| Club Matches |            |    34590360 | 2022-02-20T20:00:00 | Julian Ospina                    |     2798703 | Daniela Salazar Moreno         |    2743044 | myutr        | False               | 6-1 6-0          |
| Club Matches |            |    34590342 | 2022-02-20T20:00:00 | Manuel Orozco Salazar            |     2933803 | Mariana Guerrero               |    3077538 | myutr        | False               | 6-1 6-0          |
| Club Matches |            |    34590348 | 2022-02-20T20:00:00 | Mario Cesar DaSilva              |     3528676 | Luis Javier Castro             |    2932966 | myutr        | False               | 6-2 6-2          |
| Club Matches |            |    34590365 | 2022-02-20T19:00:00 | Camila Iza sierra                |     3521258 | Ana Maria Alzate               |    3528654 | myutr        | False               | 6-0 6-3          |
| Club Matches |            |    34590346 | 2022-02-19T21:00:00 | Santiago Mora                    |     1157191 | Luis Rueda                     |    1312175 | myutr        | False               | 7-5 6-2          |
| Club Matches |            |    34590353 | 2022-02-19T21:00:00 | Federico Gomez                   |     2787919 | Mauricio Gonzalez Marin        |    2785794 | myutr        | False               | 7-5 5-7 10-1     |
| Club Matches |            |    34590345 | 2022-02-19T21:00:00 | Jorge Villa                      |     2820925 | Pablo Solano                   |    2732603 | myutr        | False               | 6-4 6-4          |
| Club Matches |            |    34590347 | 2022-02-19T21:00:00 | Mauricio Rendon                  |     3169174 | Robert Sloboda                 |    1087901 | myutr        | False               | 6-3 6-0          |
| Club Matches |            |    34590359 | 2022-02-19T20:00:00 | Mariana Gomez                    |     1524441 | Wilmar Orozco                  |    1357134 | myutr        | False               | 6-4 7-5          |
| Club Matches |            |    34590352 | 2022-02-19T20:00:00 | Juanita Salazar                  |     1965361 | Lucas Marulanda                |    2741661 | myutr        | False               | 6-0 6-3          |
| Club Matches |            |    34590358 | 2022-02-19T20:00:00 | Pedro Cardona                    |     2785534 | Ana Rico                       |    2935240 | myutr        | False               | 6-0 6-1          |
| Club Matches |            |    34590367 | 2022-02-19T19:00:00 | CAMILA ECHEVERRI CHAPARRO        |     3525478 | Felipe Estrada                 |    2962922 | myutr        | False               | 6-2 6-2          |
| Club Matches |            |    34590366 | 2022-02-19T19:00:00 | Ana María Peláez                 |     3541392 | Pablo Rico                     |    3178932 | myutr        | False               | 2-6 6-2 10-7     |
+--------------+------------+-------------+---------------------+----------------------------------+-------------+--------------------------------+------------+--------------+---------------------+------------------+
```

### Using as a Library

## Credits

## License

This project is covered under the terms described in [LICENSE](LICENSE).

## Contributing

See the [Contributing](CONTRIBUTING.md) if you want to contribute.

## Changes

See the [Changelog](CHANGELOG.md) for a full list of changes.
