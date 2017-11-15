# Elreact-rest Routing System

#### Routes:

##### addresses/

* HTTP methods: GET and POST
** GET: list all address
** POST: create a new address

```json
[
    {
        "id": 1,
        "zipcode": "85869020",
        "street": "Rua Ibitinga",
        "number": 261,
        "neighbor": "jardim santa rosa",
        "state": "PR",
        "country": "Brasil",
        "point": {
            "type": "Point",
            "coordinates": [
                -49.55010462859367,
                -21.822153457346843
            ]
        }
    },
]
```

##### addresses/(?P<pk>[0-9]+)/

* HTTP methods: GET, PUT and DELETE
** GET: list a specific address by his id
** PUT: edit a specific address by his id
** DELETE: remove a specific address by his id

```json
    {
        "id": 1,
        "zipcode": "85869020",
        "street": "Rua Ibitinga",
        "number": 261,
        "neighbor": "jardim santa rosa",
        "state": "PR",
        "country": "Brasil",
        "point": {
            "type": "Point",
            "coordinates": [
                -49.55010462859367,
                -21.822153457346843
            ]
        }
    }
```

##### events/

* HTTP methods: GET and POST
** GET: list all events
*** ?residential=true: list all events near from residential address of current logged user
*** ?path=true: list all events near from path of current logged user
*** ?current=true&lat=26.9119415283203&long=12.46100258450666: list all events near specific latitude and longitude
*** ?tags=true&tag=exercicio&tag=spinning: list all events by a list of tags
** POST: create a new event

```json
[
    {
        "id": 2,
        "name": "Evento lONGE PRA CARA",
        "description": "ssa",
        "date": "2017-11-13T19:35:25Z",
        "address": [
            {
                "id": 3,
                "zipcode": "85869020",
                "street": "longe pra carai",
                "number": 555,
                "neighbor": "aaaa",
                "state": "PR",
                "country": "Brasil",
                "point": {
                    "type": "Point",
                    "coordinates": [
                        26.9119415283203,
                        12.461002584506655
                    ]
                }
            }
        ],
        "owner": 1,
        "tags": [
            {
                "id": 1,
                "name": "Interação"
            }
        ]
    },
]
```

##### events/(?P<pk>[0-9]+)/

* HTTP methods: GET, PUT and DELETE
** GET: list a specific event by his id
** PUT: edit a specific event by his id
** DELETE: remove a specific event by his id

```json
{
    "id": 2,
    "name": "Evento lONGE PRA CARA",
    "description": "ssa",
    "date": "2017-11-13T19:35:25Z",
    "address": [
        {
            "id": 3,
            "zipcode": "85869020",
            "street": "longe pra carai",
            "number": 555,
            "neighbor": "aaaa",
            "state": "PR",
            "country": "Brasil",
            "point": {
                "type": "Point",
                "coordinates": [
                    26.9119415283203,
                    12.461002584506655
                ]
            }
        }
    ],
    "owner": 1,
    "tags": [
        {
            "id": 1,
            "name": "Interação"
        }
    ]
}
```

^ ^event-owners/$
^ ^event-owners/(?P<pk>[0-9]+)/$
^ ^app-users/$
^ ^paths/(?P<pk>[0-9]+)/$
^ ^paths/$
^ ^login/$