# Simple-microservice

## Dependencies: 
- Flask
- pymongo
- flask_pymongo
   
## Instalation:
`pip3 install -r requirements`

## Available actions:
- Create product
- Get full list of products
- Find product by its parameter
- Find product by id
- Find product by name

## Test commands:
### Create product:
`curl --request POST \
  --url http://localhost:5000/product/new \
  --header 'content-type: application/json' \
  --data '{    "id" : <id>, 
               "name": <name>, 
               "description" : <description>, 
               "parameters" : [{"key" : "<key1>", "value" : "<value1>"},
                                ...
                               {"key" : "<keyN>", "value" : "<valueN>"}]
}'`<br/>   where 
- \<id\> - product id
- \<name\> - product name
- \<description\> - product description 
- \<keyX\> - name of parameter
- \<valueX\> - value of parameter
  
### Get full list of products:
`curl --request GET \
--url http://localhost:5000//product/find_all \
--data ''`

### Find product by its parameter:
`curl --request GET \
--url http://localhost:5000//product/find_by_param \
--header 'Content-Type: application/json' \
--data '{   
    "key" : "<key>", 
    "value" : "<value>"
}'`<br/>   where
- \<key\> - name of parameter 
- \<value\> - value of parameter
  
### Find product by id:
`curl --request GET \
--url http://localhost:5000//product/find_by_id \
--header 'Content-Type: application/json' \
--data '{   
    "id" : <id>
}'`<br/>   where 
- \<id\> - product id

### Find product by name: 
`curl --request GET \
--url http://localhost:5000//product/find_by_name \
--header 'Content-Type: application/json' \
--data '{   
    "name" : "pro"
}'`<br/>   where
- \<name\> - product name
