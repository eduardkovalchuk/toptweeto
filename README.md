# STRUSER project

To start project:
```
$ docker-compose up
```

***

## Login client with JIRA via OAuth1

1. Initialization of flow:

| Method   | Endpoint             | Request body | Response Body                                                                |
| :------: | :------------------: | :----------: | :--------------------------------------------------------------------------: |
| POST     | api/jira/init_oauth/ | ```{}```     | ```{ "request_token_key": "TOKEN_KEY_VALUE", "authorization_url": "URL" }``` |

2. Redirect user to retreived **authorization_url**
3. User logins to jira
4. Jira redirects user to frontend
5. Make request with retreived **request_token_key** (from step 1) to get access_token

| Method   | Endpoint               | Request body                                     | Response Body                                   |
| :------: | :--------------------: | :----------------------------------------------: | :---------------------------------------------: |
| POST     | api/jira/access_token/ | ```{ "request_token_key": "TOKEN_KEY_VALUE" }``` | ```{ "access_token_key": "TOKEN_KEY_VALUE" }``` |

7. Set header 'Jira-Authorization' with value of *access_token_key*

8. Make export request to export section or project

> before exporting you have to provide *jira_base_url* for **account** AND *jira_key* for **project**


| Method   | Endpoint                 | Request body                 | Response Body                                                                                                                              |
| :------: | :----------------------: | :--------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------: |
| POST     | api/jira/export_section/ | ```{ "section_pk": "PK" }``` | ```[{"issues":[{"id":ID, "key": "KEY", "self":"LINK"}], "errors":[]}, {"issues":[{"id":ID, "key": "KEY", "self":"LINK"}], "errors":[]}]``` |

| Method   | Endpoint                 | Request body                                        | Response Body                                   |
| :------: | :----------------------: | :-------------------------------------------------: | :---------------------------------------------: |
| POST     | api/jira/export_project/ | ```{ "project_pk": "PK", "lead": LEAD_USERNAME }``` | ```"{"self": "LINK", "id":ID, "key": "KEY"}"``` |
