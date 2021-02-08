API urls

`https://domen.com/api/organization/`

`https://domen.com/api/account/`

`GET`, `POST`, `PATCH`, `DELETE` metodlari ruxsat etilgen
<hr>

`POST` methodi arqali `SignIn` */api/account/login/*

Request data
```
{
    "username":"admin",
    "password":"password"
}
```
Response data
```
{
    "auth_token": "5a0bd6d5a57aa7881e660f2871f4238630719dfc"
}
```
Barliq soraw (request) lar `headers` inde `auth_token` ma'nisi qosip jiberiledi.
```headers = {"Authentication": "Token <auth_token>"}```
<hr>

`GET` methodi  */api/organization/detail/*

`GET` arqali firmag'a tiyisli barliq mag'liwmatlar alinadi.

> /api/organization/detail/

Response data 
```
{
    "id": 1,
    "organizations_department": [
        {
            "id": 1,
            "department_employee": [
                {
                    "id": 2,
                    "fio": "Timati Cook",
                    "phone": 7654321,
                    "organization_id": 1,
                    "department_id": 1
                }
            ],
            "employee_count": 1,
            "name": "Design",
            "organization_id": 1
        },
        {
            "id": 2,
            "department_employee": [],
            "employee_count": 0,
            "name": "Mac",
            "organization_id": 1
        },
        {
            "id": 5,
            "department_employee": [],
            "employee_count": 0,
            "name": "Call center",
            "organization_id": 1
        }
    ],
    "no_department_employees": [
        {
            "id": 6,
            "fio": "Forty Two",
            "phone": null,
            "organization_id": 1,
            "department_id": null
        }
    ],
    "name": "Apple",
    "address": "USA, CA"
}
```
<hr>

`GET`, `POST`, `PATCH`, `DELETE` methodlarina ruxsat etilgen */api/organization/department/*

`GET` arqali firmag'a tiyisli bo'limler dizimin aliw

> /api/organization/department/

Response data
```
[
    {
        "id": 1,
        "department_employee": [
            {
                "id": 2,
                "fio": "Timati Cook",
                "phone": 7654321,
                "organization_id": 1,
                "department_id": 1
            }
        ],
        "employee_count": 1,
        "name": "Design",
        "organization_id": 1
    },
    {
        "id": 2,
        "department_employee": [],
        "employee_count": 0,
        "name": "Mac",
        "organization_id": 1
    },
    {
        "id": 5,
        "department_employee": [],
        "employee_count": 0,
        "name": "Call center",
        "organization_id": 1
    }
]
```
<hr>

`GET` method arqali bo'lim haqqinda mag'liwmat aliw
> /api/organization/department/< id >/

Response data
```
{
    "id": 1,
    "department_employee": [
        {
            "id": 2,
            "fio": "Tim Cook",
            "phone": 7654321,
            "organization_id": 1,
            "department_id": 1
        }
    ],
    "employee_count": 1,
    "name": "Design",
    "organization_id": 1
}
```
`PATCH` methodi arqali bo'lim mag'liwmatlarin o'zgertiw
> /api/organization/department/< id >/

Request data
```
{
    "name": "Collegue"
}
```
Reponse data
```
{
    "success": true,
    "errors": {},
    "data": {
        "id": 1,
        "department_employee": [
            {
                "id": 2,
                "fio": "Tim Cook",
                "phone": 7654321,
                "organization_id": 1,
                "department_id": 1
            }
        ],
        "employee_count": 1,
        "name": "Colleague",
        "organization_id": 1
    }
}
```
<hr>

`DELETE` methodi arqali `id` g'a tiyisli bo'limdi o'shiriw
> /api/organization/department/3/

Response data
```
{
    "success": true
}
```
<hr>

`POST` methodi arqali jan'a bo'lim jaratiw
> /api/organization/department/

Request data
```
{
    "name":"Taza bo'lim ati"
}
```
Response data
```
{
    "success": true,
    "errors": {},
    "data": {
        "id": 12,
        "department_employee": [],
        "employee_count": 0,
        "name": "Taza bo'lim",
        "organization_id": 1
    }
}
```
<hr>

`GET`, `POST`, `PATCH`, `DELETE` methodlarina ruxsat berilgen */api/organization/employee/*

`GET` arqali firmag'a tiyisli jumisshilardin' dizimin aliw
> /api/organization/employee/

Response data
```
[
    {
        "id": 3,
        "fio": "Johny ayv",
        "phone": 1234567,
        "organization_id": 1,
        "department_id": null
    },
    {
        "id": 6,
        "fio": "Forty Two",
        "phone": null,
        "organization_id": 1,
        "department_id": null
    },
    {
        "id": 2,
        "fio": "Tim Cook",
        "phone": 7654321,
        "organization_id": 1,
        "department_id": 1
    }
]
```
<hr>

`GET` arqali `id` g'a tiyisli jumisshi mag'liwmatlarin aliw 
> /api/organization/employee/< id >/

Reponse data
```
{
    "id": 2,
    "fio": "Tim Cook",
    "phone": 7654321,
    "organization_id": 1,
    "department_id": 1
}
```
`PATCH` methodi arqali `id` g'a tiyisli jumisshi mag'liwmatlarin o'zgertiw
> /api/organization/employee/< id >/

Request data
```
{
   "fio": "New name",
   "phone": "New phone number",
   "department_id": 1
}
```
Response data
```
{
    "success": true,
    "data": {
        "id": 2,
        "fio": "Tim Cook",
        "phone": New phone number(Big Int),
        "organization_id": 1,
        "department_id": 1
    }
}
```
<hr>

`DELETE` method `id` g'a tiyisli jumisshini o'shiriw
> /api/organization/employee/< id >/

Response data 
```
{
   "success":True
}
```
<hr>

`POST` methodi arqali taza jumisshi qosiw yamsa excel file ju'klew
> /api/organization/employee/

**Add new employee**

Request data
```
{
    "fio": "New employee",
    "phone": 998911234567,
    "department_id": 1
}
```
Response data
```
{
    "success": true,
    "errors": {},
    "data": {
            taza jumisshi mag'liwmatlari
    }
}
```
**Upload file (ext: \*.xls, \*.xlsx)**

Request data
```
{
    "file": excel.xlsx
}
```
Response data
```
{
    "success": true,
    "errors": {},
    "data": {}
}
```
