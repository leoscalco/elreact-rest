# Elreact-rest Routing System

#### Routes:

##### addresses/

* HTTP methods: GET and POST
    * GET: list all address
    * POST: create a new address

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
    * GET: detail a specific address by your id
    * PUT: edit a specific address by your id
    * DELETE: remove a specific address by your id

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
    * GET: list all events
        * ?residential=true: list all events near from residential address of current user
        * ?path=true: list all events near from path of current user
        * ?current=true&lat=26.9119415283203&long=12.46100258450666: list all events near specific latitude and longitude
        * ?tags=true&tag=exercicio&tag=spinning: list all events by a list of tags
        * ?owner=1: list all events by an owner
    * POST: create a new event

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
    * GET: detail a specific event by your id
    * PUT: edit a specific event by your id
    * DELETE: remove a specific event by your id

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

##### event-owners/

* HTTP methods: GET and POST
    * GET: list all events owners
    * POST: create a new event owner (extra field => password: "senharparacriptografia")

```json
[
    {
        "id": 1,
        "user": {
            "id": 2,
            "username": "joao",
            "first_name": "Joao",
            "last_name": "Silva",
            "email": "joao@silva.com",
            "last_login": null,
            "date_joined": "2017-11-13T16:27:47Z",
            "is_staff": false
        },
        "occupation": "DEV",
        "userType": 1,
        "phone": "4530285385"
    },
    {
        "id": 2,
        "user": {
            "id": 5,
            "username": "joao123",
            "first_name": "Joao",
            "last_name": "Silva",
            "email": "jo3a3o2@silva.com",
            "last_login": "2017-11-14T15:48:08.773190Z",
            "date_joined": "2017-11-14T15:47:50.831375Z",
            "is_staff": false
        },
        "occupation": "DEV",
        "userType": 1,
        "phone": "4530285385"
    }
]
```

##### event-owners/(?P<pk>[0-9]+)/

* HTTP methods: GET, PUT and DELETE
    * GET: detail a specific event owner by your id
    * PUT: edit a specific event owner by your id
    * DELETE: remove a specific event owner by your id

```json
{
    "id": 1,
    "user": {
        "id": 2,
        "username": "joao",
        "first_name": "Joao",
        "last_name": "Silva",
        "email": "joao@silva.com",
        "last_login": null,
        "date_joined": "2017-11-13T16:27:47Z",
        "is_staff": false
    },
    "occupation": "DEV",
    "userType": 1,
    "phone": "4530285385"
},
{
    "id": 2,
    "user": {
        "id": 5,
        "username": "joao123",
        "first_name": "Joao",
        "last_name": "Silva",
        "email": "jo3a3o2@silva.com",
        "last_login": "2017-11-14T15:48:08.773190Z",
        "date_joined": "2017-11-14T15:47:50.831375Z",
        "is_staff": false
    },
    "occupation": "DEV",
    "userType": 1,
    "phone": "4530285385"
}
```

##### app-users/

* HTTP methods: GET and POST
    * GET: list all app users
    * POST: create a new app user (extra field => password: "senharparacriptografia")

```json
[
    {
        "id": 1,
        "user": {
            "id": 1,
            "username": "leoscalco",
            "first_name": "",
            "last_name": "",
            "email": "leo@leo.com",
            "last_login": "2017-11-15T14:42:17.354263Z",
            "date_joined": "2017-11-13T15:54:34.539560Z",
            "is_staff": true
        },
        "userType": {
            "id": 2,
            "type": "AppUser"
        },
        "phone": "4530285385",
        "residentialAddress": {
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
    }
]
```

##### app-users/(?P<pk>[0-9]+)/

* HTTP methods: GET, PUT and DELETE
    * GET: detail a specific app user by your id
    * PUT: edit a specific app user by your id
    * DELETE: remove a specific app user by your id

```json
{
    "id": 1,
    "user": {
        "id": 1,
        "username": "leoscalco",
        "first_name": "",
        "last_name": "",
        "email": "leo@leo.com",
        "last_login": "2017-11-15T14:42:17.354263Z",
        "date_joined": "2017-11-13T15:54:34.539560Z",
        "is_staff": true
    },
    "userType": {
        "id": 2,
        "type": "AppUser"
    },
    "phone": "4530285385",
    "residentialAddress": {
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
}
```

##### paths/

* HTTP methods: GET and POST
    * GET: list all paths
        * ?appuser=(?P<pk>[0-9]+): list all paths from specific app user
    * POST: create a new path

```json
[
    {
        "id": 1,
        "date": "2017-11-13T16:31:48.675339Z",
        "address": {
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
    },
]
```

##### paths/(?P<pk>[0-9]+)/

* HTTP methods: GET, PUT and DELETE
    * GET: detail a specific path by your
    * PUT: edit a specific path by your id
    * DELETE: remove a specific path by your id

```json
{
        "id": 1,
        "date": "2017-11-13T16:31:48.675339Z",
        "address": {
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
    }
```

##### login/

* HTTP methods: POST
  * POST: send a username and password and get success ou fail message and the user logged (any kind of user).

```json
{
    "username": "admin",
    "password": "acesso123"
}

##### logout/

* HTTP methods: POST
  * POST: just call a logout url and django will rely on that.

```json
NO JSON REQUIRED.
