## Create Employee

### POST /create

#### Request headers

    Content-Type: application/json

#### Request payload

    {
        "address": "Downtown Street 41",
        "birth_date": "1981-02-02",
        "boss": "Yamazaki Yamaha",
        "first_name": "Nin",
        "last_name": "Niku",
        "salary": 350000
    }

#### Response payload

    {
        "result": {
            "_id": "5d444836e66ae6015682e668",
            "address": "Downtown Street 41",
            "birth_date": "1981-02-02",
            "boss": "Yamazaki Yamaha",
            "first_name": "Nin",
            "last_name": "Niku",
            "salary": 350000
        }
    }

## Get Employee

### GET /employee/{_id}

#### Request URL

    http://127.0.0.1:5000/employee/5d444836e66ae6015682e668

#### Response payload

    {
        "result": {
            "_id": "5d444836e66ae6015682e668",
            "address": "Downtown Street 41",
            "birth_date": "1981-02-02",
            "boss": "Yamazaki Yamaha",
            "first_name": "Nin",
            "last_name": "Niku",
            "salary": 350000
        }
    }

## Update Employee

### POST /update/{_id}

#### Request headers

    Content-Type: application/json

#### Request payload

    {
        "salary" : 900000
    }

#### Response payload

    Success Fully Updated

## Delete Employee

### DELETE /employee/{_id}

#### Request URL

    http://127.0.0.1:5000/delete/5d444836e66ae6015682e668

#### Response payload

    Success Fully Deleted


## List Employee

### GET /employee/list?limit={limit}&offset={offset}&first_name={first_name}&last_name={last_name}&birth_date={birth_date}&address={address}&boss={boss}&salarygreaterthan={salarygreaterthan}&salarylessthan={salarylessthan}

#### Default Values
    Limit = 5
    Offset = 0
    salarygreaterthan = 0
    salarylessthan = 9223372036854775807

#### Request URL

    http://127.0.0.1:5000/list?limit=3&offset=0&first_name=&last_name=&birth_date=&address=&boss=&salarygreaterthan=&salarylessthan=

#### Response payload

    {
        "next_url": "/list?limit=10&offset=10&first_name=&last_name=&birth_date=&address=&boss=&salarygreaterthan=0&salarylessthan=9223372036854775807",
        "prev_url": "",
        "result": [
            {
                "_id": "5d43cef0ddc99c6eac6d92d6",
                "address": "ABC Avuenue",
                "birth_date": "1991-02-02",
                "boss": "Mr Roberts",
                "first_name": "Samla",
                "last_name": "Smithson",
                "salary": 300000
            },
            {
                "_id": "5d43db92688df09cd1d594ec",
                "address": "ABC Avuenue",
                "birth_date": "1991-02-02",
                "boss": "Mr Roberts",
                "first_name": "John",
                "last_name": "Doe",
                "salary": 190000
            }
        ]
    }
