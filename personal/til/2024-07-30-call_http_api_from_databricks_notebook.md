
# Calling HTTP API from Databricks Notebook

[![Back to TIL Hub](https://img.shields.io/badge/←%20Back%20to-TIL%20Hub-blue?style=for-the-badge)](README.md)

```scala
// Import necessary libraries
import org.apache.http.client.methods.{HttpGet, HttpPost}
import org.apache.http.entity.StringEntity
import org.apache.http.impl.client.HttpClientBuilder
import org.apache.http.util.EntityUtils
import scala.util.{Try, Success, Failure}
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions._

// Define case classes to represent a post
case class Post(id: Int, userId: Int, title: String, body: String)
case class NewPost(userId: Int, title: String, body: String)

// Function to fetch a post by ID
def getPost(postId: Int): Try[String] = {
  val client = HttpClientBuilder.create().build()
  val request = new HttpGet(s"https://jsonplaceholder.typicode.com/posts/$postId")

  Try {
    val response = client.execute(request)
    val entity = response.getEntity
    val jsonString = EntityUtils.toString(entity)
    client.close()
    jsonString
  }
}

// Function to create a new post
def createPost(newPost: NewPost): Try[String] = {
  val client = HttpClientBuilder.create().build()
  val request = new HttpPost("https://jsonplaceholder.typicode.com/posts")
  val json = s"""{"userId": ${newPost.userId}, "title": "${newPost.title}", "body": "${newPost.body}"}"""
  request.setEntity(new StringEntity(json))
  request.setHeader("Content-type", "application/json")

  Try {
    val response = client.execute(request)
    val entity = response.getEntity
    val jsonString = EntityUtils.toString(entity)
    client.close()
    jsonString
  }
}

// Get the SparkSession
val spark = SparkSession.builder.getOrCreate()
import spark.implicits._

// Example 1: GET request
println("Example 1: GET request")
val getResult = getPost(1)

getResult match {
  case Success(jsonString) => print(jsonString)
  case Failure(error) => println(s"Failed to fetch post: ${error.getMessage}")
}

// Example 2: POST request
println("\nExample 2: POST request")
val newPost = NewPost(userId = 1, title = "New Post Title", body = "This is the body of the new post.")
val postResult = createPost(newPost)

postResult match {
  case Success(jsonString) => print(jsonString)
  case Failure(error) => println(s"Failed to create post: ${error.getMessage}")
}
```


---
This Scala code is used to make HTTP requests to a JSONPlaceholder API, which is a fake online REST service that you can use for testing and prototyping. Here's a breakdown of what the code does:

**Defining Case Classes**

The code starts by defining two case classes: `Post` and `NewPost`. These classes represent the structure of the data that will be sent to and received from the API.

* `Post` has four fields: `id`, `userId`, `title`, and `body`.
* `NewPost` has three fields: `userId`, `title`, and `body`.

**Defining Functions**

The code defines two functions: `getPost` and `createPost`. These functions make HTTP requests to the API.

* `getPost(postId: Int)`: This function takes a `postId` as an argument and makes a GET request to the API to retrieve a post with the specified ID. The function returns a `Try` object, which is a Scala type that represents a computation that may fail. If the request is successful, the function returns a `Success` object containing the JSON response as a string. If the request fails, the function returns a `Failure` object containing the error message.
* `createPost(newPost: NewPost)`: This function takes a `NewPost` object as an argument and makes a POST request to the API to create a new post. The function returns a `Try` object, similar to `getPost`.

**Making HTTP Requests**

The code uses the Apache HttpClient library to make the HTTP requests. Here's a high-level overview of how the requests are made:

* `getPost`: The function creates an `HttpGet` object with the URL of the post to retrieve. It then executes the request using the `HttpClient` object and retrieves the response. The function extracts the JSON response from the entity and returns it as a string.
* `createPost`: The function creates an `HttpPost` object with the URL of the API endpoint to create a new post. It then sets the request entity to a JSON string representation of the `NewPost` object. The function executes the request using the `HttpClient` object and retrieves the response. The function extracts the JSON response from the entity and returns it as a string.

**Using the SparkSession**

The code creates a SparkSession object, which is used to interact with the Spark SQL engine. However, in this code, the SparkSession is not actually used to perform any Spark-related operations. It's likely that the SparkSession is created to set up the Spark environment for future use.

**Example Usage**

The code includes two example usage sections:

* `Example 1: GET request`: This section calls the `getPost` function with a `postId` of 1 and prints the response.
* `Example 2: POST request`: This section creates a new `NewPost` object and calls the `createPost` function with the new post. It then prints the response.

