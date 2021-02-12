API urls

`https://domen.com/api/v1/organization/`

`https://domen.com/api/v1/account/`

`GET`, `POST`, `PATCH`, `DELETE` metodlari ruxsat etilgen
<hr>

`POST` methodi arqali `SignIn` */api/v1/account/login/*

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

`GET` methodi  */api/v1/organization/detail/*

`GET` arqali firmag'a tiyisli barliq mag'liwmatlar alinadi.

> /api/v1/organization/detail/

Response data 
```
{
    "success": true,
    "code": 200,
    "message": "Всё данные о копмании TexnoPOS IT mektebi",
    "payload": {
        "data": {
            "id": 1,
            "name": "TexnoPOS IT mektebi",
            "address": "Ǵarezsizlik kóshesi, 80/4",
            "department": [
                {
                    "id": 1,
                    "employee": [
                        {
                            "id": 3,
                            "fio": "Saliq Bisenov",
                            "phone": 998999541234,
                            "organization_id": 1,
                            "department_id": 1
                        },
                        {
                            "id": 4,
                            "fio": "Umida Reimbaeva",
                            "phone": 998991234567,
                            "organization_id": 1,
                            "department_id": 1
                        }
                    ],
                    "_employee_count": 2,
                    "name": "Programmers",
                    "organization_id": 1
                },
                {
                    "id": 2,
                    "employee": [
                        {
                            "id": 1,
                            "fio": "Sharapat Kalabaev",
                            "phone": 998901234567,
                            "organization_id": 1,
                            "department_id": 2
                        }
                    ],
                    "_employee_count": 1,
                    "name": "Administraciya",
                    "organization_id": 1
                },
                {
                    "id": 3,
                    "employee": [
                        {
                            "id": 2,
                            "fio": "Alibek Embergenov",
                            "phone": 998911234567,
                            "organization_id": 1,
                            "department_id": 3
                        }
                    ],
                    "_employee_count": 1,
                    "name": "Oqitiwshilar",
                    "organization_id": 1
                }
            ],
            "_no_department_employees": [
                {
                    "id": 5,
                    "fio": "Batir Urazbaev",
                    "phone": 998931234567,
                    "organization_id": 1,
                    "department_id": null
                }
            ]
        }
    }
}
```
<hr>

`GET`, `POST`, `PATCH`, `DELETE` methodlarina ruxsat etilgen */api/organization/department/*

`GET` arqali firmag'a tiyisli bo'limler dizimin aliw

> /api/v1/organization/department/

Response data
```
{
    "success": true,
    "code": 200,
    "message": "Всё отделения компании TexnoPOS IT mektebi",
    "payload": [
        {
            "id": 1,
            "employee": [
                {
                    "id": 3,
                    "fio": "Saliq Bisenov",
                    "phone": 998999541234,
                    "organization_id": 1,
                    "department_id": 1
                },
                {
                    "id": 4,
                    "fio": "Umida Reimbaeva",
                    "phone": 998991234567,
                    "organization_id": 1,
                    "department_id": 1
                }
            ],
            "_employee_count": 2,
            "name": "Programmers",
            "organization_id": 1
        },
        {
            "id": 2,
            "employee": [
                {
                    "id": 1,
                    "fio": "Sharapat Kalabaev",
                    "phone": 998901234567,
                    "organization_id": 1,
                    "department_id": 2
                }
            ],
            "_employee_count": 1,
            "name": "Administraciya",
            "organization_id": 1
        },
        {
            "id": 3,
            "employee": [
                {
                    "id": 2,
                    "fio": "Alibek Embergenov",
                    "phone": 998911234567,
                    "organization_id": 1,
                    "department_id": 3
                }
            ],
            "_employee_count": 1,
            "name": "Oqitiwshilar",
            "organization_id": 1
        }
    ]
}
```
<hr>

`GET` method arqali bo'lim haqqinda mag'liwmat aliw
> /api/v1/organization/department/< id >/

Response data
```
{
    "success": true,
    "code": 200,
    "message": "Отдел Administraciya",
    "payload": {
        "id": 2,
        "employee": [
            {
                "id": 1,
                "fio": "Sharapat Kalabaev",
                "phone": 998901234567,
                "organization_id": 1,
                "department_id": 2
            }
        ],
        "_employee_count": 1,
        "name": "Administraciya",
        "organization_id": 1
    }
}
```
`PATCH` methodi arqali bo'lim mag'liwmatlarin o'zgertiw
> /api/v1/organization/department/< id >/

Request data
```
{
    "name": "Дирекция"
}
```
Reponse data
```
{
    "success": true,
    "message": "Успешно изменён!",
    "code": 200,
    "payload": {
        "id": 2,
        "employee": [
            {
                "id": 1,
                "fio": "Sharapat Kalabaev",
                "phone": 998901234567,
                "organization_id": 1,
                "department_id": 2
            }
        ],
        "_employee_count": 1,
        "name": "Дирекция",
        "organization_id": 1
    }
}
```
<hr>

`DELETE` methodi arqali `id` g'a tiyisli bo'limdi o'shiriw
> /api/v1/organization/department/2/

Response data
```
{
    "success": True,
    "code": 200,
    "message": "Дирекция успешно удалено!",
    "payload":[],
}
```
<hr>

`POST` methodi arqali jan'a bo'lim jaratiw
> /api/v1/organization/department/

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
    "code": 201,
    "message": "Media создан!",
    "payload": {
        "id": 4,
        "employee": [],
        "_employee_count": 0,
        "name": "Media",
        "organization_id": 1
    }
}
```
<hr>

`GET`, `POST`, `PATCH`, `DELETE` methodlarina ruxsat berilgen */api/organization/employee/*

`GET` arqali firmag'a tiyisli jumisshilardin' dizimin aliw
> /api/v1/organization/employee/

Response data
```
{
    "success": true,
    "code": 200,
    "message": "Список сотрудников!",
    "payload": [
        {
            "id": 1,
            "fio": "Sharapat Kalabaev",
            "phone": 998901234567,
            "organization_id": 1,
            "department_id": 2
        },
        {
            "id": 2,
            "fio": "Alibek Embergenov",
            "phone": 998911234567,
            "organization_id": 1,
            "department_id": 3
        },
        {
            "id": 3,
            "fio": "Saliq Bisenov",
            "phone": 998999541234,
            "organization_id": 1,
            "department_id": 1
        },
        {
            "id": 4,
            "fio": "Umida Reimbaeva",
            "phone": 998991234567,
            "organization_id": 1,
            "department_id": 1
        },
        {
            "id": 5,
            "fio": "Batir Urazbaev",
            "phone": 998931234567,
            "organization_id": 1,
            "department_id": null
        }
    ]
}
```
<hr>

`GET` arqali `id` g'a tiyisli jumisshi mag'liwmatlarin aliw 
> /api/organization/employee/< id >/

Reponse data
```
{
    "success": true,
    "code": 200,
    "message": "Данные о сотруднике!",
    "payload": {
        "id": 2,
        "fio": "Alibek Embergenov",
        "phone": 998911234567,
        "organization_id": 1,
        "department_id": 3
    }

```
`PATCH` methodi arqali `id` g'a tiyisli jumisshi mag'liwmatlarin o'zgertiw
> /api/v1/organization/employee/< id >/

Request data
```
{
   "fio": "Alibek Embergenov",
   "phone": "911234567",
   "department_id": 2
}
```
Response data
```
{
    "success": true,
    "code": 200,
    "message": "Успешно изменён!",
    "payload": {
        "id": 2,
        "fio": "Alibek Embergenov",
        "phone": 911234567,
        "organization_id": 1,
        "department_id": 2
    }
}
```
<hr>

`DELETE` method `id` g'a tiyisli jumisshini o'shiriw
> /api/v1/organization/employee/< id >/

Response data 
```
{
    "success":True,
    "code": 200,
    "message":"Удалено!",
    "payload": []
}
```
<hr>

`POST` methodi arqali taza jumisshi qosiw yamsa excel file ju'klew
> /api/v1/organization/employee/

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
    "code": 201,
    "message": "Добавлено!",
    "payload": {
        "id": 6,
        "fio": "Salamat Sarsenov",
        "phone": 907654321,
        "organization_id": 1,
        "department_id": 4
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
    "success":True, 
    "code": 201,
    "message": "Добавлено!",
    "payload": [],
},
```
