# STRUSER project

To start project:
```
$ docker-compose up
```

***

## Login client with JIRA via OAuth1

0. Initialization of flow:

| Method   | Endpoint             | Request body | Response Body                                                                |
| :------: | :------------------: | :----------: | :--------------------------------------------------------------------------: |
| POST     | api/jira/init_oauth/ | ```{}```     | ```{ "request_token_key": "TOKEN_KEY_VALUE", "authorization_url": "URL" }``` |

0. Redirect user to retreived **authorization_url**
0. User logins to jira
0. Jira redirects user to frontend
0. With retreived **request_token_key** (from step 1) make request 

| Method   | Endpoint               | Request body                                     | Response Body                                   |
| :------: | :--------------------: | :----------------------------------------------: | :---------------------------------------------: |
| POST     | api/jira/access_token/ | ```{ "request_token_key": "TOKEN_KEY_VALUE" }``` | ```{ "access_token_key": "TOKEN_KEY_VALUE" }``` |

0. Set header 'Jira-Authorization' with value of *access_token_key*

0. Make export request to export section or project

> before exporting you have to provide *jira_base_url* for **account** AND *jira_key* for **project**


| Method   | Endpoint                 | Request body                 | Response Body                                                                                                                              |
| :------: | :----------------------: | :--------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------: |
| POST     | api/jira/export_section/ | ```{ "section_pk": "PK" }``` | ```[{"issues":[{"id":ID, "key": "KEY", "self":"LINK"}], "errors":[]}, {"issues":[{"id":ID, "key": "KEY", "self":"LINK"}], "errors":[]}]``` |

| Method   | Endpoint                 | Request body                                        | Response Body                                   |
| :------: | :----------------------: | :-------------------------------------------------: | :---------------------------------------------: |
| POST     | api/jira/export_project/ | ```{ "project_pk": "PK", "lead": LEAD_USERNAME }``` | ```"{"self": "LINK", "id":ID, "key": "KEY"}"``` |
