
data_v1 = [{
    "name": "Megan Holtz",
    "ancestors": [
        "Billy Holtz",
        "Mickey Mouse",
        "Barbara Holtz",
        "Dina Dinkley",
        "Edwardo III",
        "Steve Long",
        "Sarah Long"],
    "age": 29
    }, {
    "name": "Billy Holtz",
    "ancestors": [
        "Mickey Mouse",
        "Dina Dinkley"
    ],
    "age": 67
    }, {
    "name": "Darryl Holtz",
    "ancestors": [
        "Mickey Mouse",
        "Dina Dinkley"
    ],
    "age": 54
    }, {
    "name": "Mickey Mouse",
    "ancestors": [],
    "age": 111
    }, {
    "name": "Dina Dinkley",
    "ancestors": ["Edwardo III"],
    "age": 98
    }, {
    "name": "Edwardo III",
    "ancestors": [],
    "age": 130
    }, {
    "name": "Barbara Holtz",
    "ancestors": ["Steve Long", "Sarah Long"],
    "age": 98
    }
]

data_v2 = [
    {
        "name": "Megan Holtz",
        "parents": [
            {
                "name": "Billy Holtz",
                "parents": [
                    {
                        "name": "Dina Dinkley",
                        "parents": [
                            {
                                "name": "Edwardo III",
                                "ancestors": ["Edwardo III"],
                                "age": 130
                            }
                        ],
                        "age": 98
                    },
                    {
                        "name": "Mickey Mouse",
                        "parents": [],
                        "age": 111
                    }
                ],
                "age": 67
            }, {
                "name": "Barbara Holtz",
                "parents": [
                    {
                        "name": "Steve Long"
                    },
                    {
                        "name": "Barbara Long"
                    }
                ]
            }
        ],
        "age": 29
    }
]
