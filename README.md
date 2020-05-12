# django_rest

## Api Endpoints and their description:

#### 1. Create User(No authoriastion is compulsory):

   ` POST http://127.0.0.1:8000/users/ `

   With body containing user details in JSON Format, like this:

  ``` 
  {
      "username":<YOUR-USERNAME>,
      "tweets":[],
      "password":<YOUR-PASSWORD>
  }
  ```
  
#### 2. Create a Tweet (Auth Required):
  
   ` POST http://127.0.0.1:8000/tweets/ `
   
  With body containing the tweet in JSON Format, like this:
  
  ``` 
    {
      "text":"Tweet content."
    }
  ```
  

#### 3. Update a tweet(Owner Auth required)

 ` PUT http://127.0.0.1:8000/tweets/<id of tweet to be updated>/ `
 
   With body containing the updated tweet in JSON Format, like this:
  
  ``` 
    {
      "text":"Updated Tweet content."
    }
  ```
  
  
#### 4. Delete a tweet(Owner Auth required)

  ` DELETE http://127.0.0.1:8000/tweets/<id of tweet to be deleted>/ `
 
  
#### 5. Get list of All tweets(No Auth Required):
  
   ` GET http://127.0.0.1:8000/tweets/`
   
   
#### 6. Get list of All Users(No Auth Required):

   ` GET http://127.0.0.1:8000/users/`
   
   
#### 7. Get a particular Tweet(No Auth Required):
 
  ` GET http://127.0.0.1:8000/tweets/<id of the tweet>/ `


#### 8. Get a particular User(No Auth Required):
 
  ` GET http://127.0.0.1:8000/users/<id of the user>/ `
  


 

