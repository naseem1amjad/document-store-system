# document-store-system
API developed using Django (Python) and django Rest Framework

## Environment Setup

(Helpfull commands)
pip3 install -r requirements.txt

python manage.py migrate

python manage.py loaddata data4Heroku.json

python manage.py runserver

Help about how to use APIs
--------------------------

Welcome to my page describing about how to use [APIs](/api/) for Docs Store System  

### Problem Statement:

Create an API that stores “digital documents” in “folders”. Folders or Documents can have one or many associated “Topics”, with short & long-form descriptors.  

### Solution:

Api has been developed using Python, Django, and PostgreSQL that can be accessed [here!](/api/)  
3 Tables were designed with the names “Documents”, “Folders”, and “Topics”  
JSON format is used for data transfer. Browsable API is used for documentation that provides list/view (GET) and forms for insertion (POST), updating (PUT) and deletion (DELETE)  

### Enpoint Details:

#### /api/folders/{id}

The client can access list of folder(s) by simply hitting /api/folders/ , this will show a list with folder\_id that can be noted by user to pass on subsequent requests.  
Example: GET /api/folders/1 will fetch data from table folders having id=1  

#### /api/topics/{id}

The client can access list of topic(s) by hitting /api/topics/ , this will list down the topics.  
Example: PUT api/topics/2 and having following in content (body) will update topic having id=2  
{ "topic\_id": 2, "topic\_name": "Arts" }  

#### /api/documents/{id}

The client (such as PostMan) can get the list of document(s) by hitting /api/documents/  
Example: To create a new document entry , POST api/documents/ having following JSON content sent  
{ "document\_name": "DocfromPostMan", "document\_short\_description": "from Postman", "folder": 1, "topics": \[1,2,3\] }  
  
Note: detail of folder\_id to be sent can be received by GET /api/folders/ , similarly ids of topics can be fetched by GET /api/topics/  

#### /api/list-documents-in-folderid/?folder\_id={id}

This endpoint is used to get list of all documents that are associated with a specific Folder{id} , you can use filter button at top right location to use GUI to input id.

#### /api/list-documents-of-topicid/?topic\_\_id={id}

This endpoint is used to get list of all documents that are associated with a specific Topic(id).

#### /api/search/

This is special endpoint that provide filtering of documents based on given folder NAME and given topic NAME.  
Example: To access all the documents in the folder “Customer Feedback” associated with the topic “SpekiLove!” you need to provide following url  
GET /api/search/?topic\_\_topic\_name=SpekiLove&folder\_\_folder\_name=CustomerFeedback  
  
\[[Work](/api/) done by [Naseem Amjad](https://courses.cognitiveclass.ai/certificates/ed7c8015c62a45abbfe85ffbf0f69762)\]
