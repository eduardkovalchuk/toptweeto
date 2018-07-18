# toptweet
Toptweet is an application that allows you to get most popular tweets on  Twitter.com

| Method   | Endpoint             | Request body | Response Body                                                                |
| :------: | :------------------: | :----------: | :--------------------------------------------------------------------------: |
| POST     | api/jira/init_oauth/ | ```{}```     | ```{ "request_token_key": "TOKEN_KEY_VALUE", "authorization_url": "URL" }``` |


| Method   | Endpoint               | Request body                                     | Response Body                                   |
| :------: | :--------------------: | :----------------------------------------------: | :---------------------------------------------: |
| POST     | api/jira/access_token/ | ```{ "request_token_key": "TOKEN_KEY_VALUE" }``` | ```{ "access_token_key": "TOKEN_KEY_VALUE" }``` |


| Method   | Endpoint                 | Request body                 | Response Body                                                              |
| :------: | :----------------------: | :--------------------------: | :------------------------------------------------------------------------: |
| POST     | api/jira/export_section/ | ```{ "section_pk": "PK" }``` | ```[{"issues":[{"id":"ID", "key": "KEY", "self":"LINK"}], "errors":[]}]``` |
