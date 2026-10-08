PET_VALID = {
    "id": 158,
    "category": {
        "id": 0,
        "name": "dogs"
    },
    "name": "max",
    "photoUrls": [
        "https://example.com/max.jpg"
    ],
    "tags": [
        {
            "id": 0,
            "name": "friendly"
        }
    ],
    "status": "available"
}


PET_MULTIPLE_PHOTOS = {
    "id": 159,
    "category": {
        "id": 0,
        "name": "dogs"
    },
    "name": "max2",
    "photoUrls": [
        "https://example.com/max1.jpg",
        "https://example.com/max2.jpg"
    ],
    "tags": [
        {
            "id": 0,
            "name": "friendly"
        }
    ],
    "status": "available"
}


PET_INVALID_STATUS = {
    "id": 160,
    "category": {
        "id": 0,
        "name": "dogs"
    },
    "name": "max3",
    "photoUrls": [
        "https://example.com/max3.jpg"
    ],
    "tags": [
        {
            "id": 0,
            "name": "friendly"
        }
    ],
    "status": "sold123"
}


PET_MISSING_NAME = {
    "id": 161,
    "category": {
        "id": 0,
        "name": "dogs"
    },
    "photoUrls": [
        "https://example.com/max4.jpg"
    ],
    "tags": [
        {
            "id": 0,
            "name": "friendly"
        }
    ],
    "status": "available"
}

PET_EMPTY = {}


PET_EMPTY_PHOTOS = {
    "id": 162,
    "category": {
        "id": 0,
        "name": "dogs"
    },
    "name": "max5",
    "photoUrls": [],
    "tags": [
        {
            "id": 0,
            "name": "friendly"
        }
    ],
    "status": "available"
}


PET_INVALID_ID_TYPE = {
    "id": "abc",
    "category": {
        "id": 0,
        "name": "dogs"
    },
    "name": "max6",
    "photoUrls": [
        "https://example.com/max6.jpg"
    ],
    "tags": [
        {
            "id": 0,
            "name": "friendly"
        }
    ],
    "status": "available"
}


PET_EMPTY_STATUS = {
    "id": 163,
    "category": {
        "id": 0,
        "name": "dogs"
    },
    "name": "max7",
    "photoUrls": [
        "https://example.com/max7.jpg"
    ],
    "tags": [
        {
            "id": 0,
            "name": "friendly"
        }
    ],
    "status": ""
}