# PerfectPick API Gateway

This API reference provides details on how to interact with the GraphQL API Gateway of our application. GraphQL is a powerful query language for APIs that allows clients to request exactly the data they need. This reference will cover the available queries, mutations, and types supported by our GraphQL API.

**Base URL**

The base URL for our API Gateway is [http://localhost:8000/graphiql](http://localhost:8000/graphiql).

**Run Project**

Run and deploy project instruction on [Deployment](#deploy).

**API Reference Index**

* [Authentication](#id1)
* [Message Queue](#id2)
* [Queries](#id3)
  * [Users Management](#id3.1)
    * [Get user by user id](#id3.1.1)
    * [Get users](#id3.1.2)
    * [Login with email](#id3.1.3)
    * [Login with google](#id3.1.4)
  * [Countries](#id3.2)
    * [Get countries](#id3.2.1)
    * [Get country by id](#id3.2.1)
  * [Likes](#id3.3)
    * [Get likes by user id](#id3.3.1)
    * [Get dislikes by user id](#id3.3.2)
    * [Get likes and dislikes by media id](#id3.3.3)
    * [Get wishlist](#id3.3.4)
  * [Catalog](#id3.4)
    <!-- Si viene el user id, se añade info de likes del usuario  -->
    * [Get books](#id3.4.1) 
    * [Get movies](#id3.4.2)
    * [Get songs](#id3.4.3)
    * [Get book by book id](#id3.4.4)
    * [Get movie by movie id](#id3.4.5)
    * [Get song by song id](#id3.4.6)
  * [Recommendations](#id3.5)
    * [Get recommend](#id3.5.1)
  * [Analysis](#id3.6)
    * [Generate analysis](#id3.6.1)
  * [Ads](#id3.7)
    * [Get user ads](#id3.7.1)
    * [Get ads by company](#id3.7.2)
  * [Payments](#id3.8)
    * [Get bills by company](#id3.8.1)
    * [Get bills by ad](#id3.8.2)
    * [Get payments](#id3.8.3)
* [Mutations](#id4)
  * [Users Management](#id4.1)
    * [Sign up user with email](#id4.1.1)
    * [Sign up user with google](#id4.1.2)
    * [Verify user account](#id4.1.3)
    * [Forgot Password](#id4.1.4)
    * [Update User](#id4.1.5)
    * [Complete setup](#id4.1.6)
    * [Delete User](#id4.1.7)
  * [Countries](#id4.2)
    * [Create country](#id4.2.1)
    * [Update country](#id4.2.1)
    * [Delete country](#id4.2.1)
    * [Import countries data](#id4.2.1)
  * [Likes](#id4.3)
    * [Like media](#id4.3.1)
    * [Dislike media](#id4.3.2)
    * [Delete like media](#id4.3.3)
    * [Delete dislike media](#id4.3.4)
    * [Rating media](#id4.3.5)
    * [Update media rating](#id4.3.6)
    * [Add media to wishlist](#id4.3.7)
    * [Remove media from wishlist](#id4.3.8)
  * [Catalog](#id4.4)
    * [Create book](#id4.4.1)
    * [Create movie](#id4.4.2)
    * [Create song](#id4.4.3)
    * [Update book](#id4.4.4)
    * [Update movie](#id4.4.5)
    * [Update song](#id4.4.6)
    * [Delete book](#id4.4.7)
    * [Delete movie](#id4.4.8)
    * [Delete song](#id4.4.9)
    * [Import books data](#id4.4.10)
    * [Import movies data](#id4.4.11)
    * [Import songs data](#id4.4.12)
  * [Recommendations](#id4.5)
    * [Mark Recommend as used](#id4.5.1)
    * [Generate new Recommend](#id4.5.2)
  * [Companies](#id4.6)
    * [Create company](#id4.6.1)
    * [Update company](#id4.6.2)
  * [Ads](#id4.7)
    * [Create ad](#id4.7.1)
    * [Update ad](#id4.7.2)
    * [Delete ad](#id4.7.3)
  * [Release](#id4.8)
    * [Publish Ad](#id4.8.1)
    * [TTPAR](#id4.8.2)
  * [Payments](#id4.9)
    * [Create bill](#id4.9.1)
    * [Delete bill](#id4.9.1)
    * [Pay bill](#id4.9.1)
* [Types](#id5)
  <!-- @todo -->
  * [Users Management](#id5.1)
  * [Countries](#id5.2)
  * [Likes](#id5.3)
  * [Catalog](#id5.4)
  * [Recommendations](#id5.5)
  * [Analysis](#id5.6)
  * [Release](#id5.7)
  * [Payments](#id5.8)

***
<br />
<br />

## API Reference

<a id="id1"></a>

### Authentication

```http
POST /graphql HTTP/1.1
Host: localhost:8000
Authorization: Bearer BEARER_TOKEN
Content-Type: application/json

{
  "query": "...",
  "variables": { "userId": "1" }
}
```



<a id="id2"></a>

### Message Queue

<!-- @todo -->



<a id="id3"></a>

### Queries

<a id="id3.1"></a>

#### User Management

<a id="id3.1.1"></a>

**Get user by user id**

_Logic Steps_

_Query Example_

_Query Response_

<!-- @todo -->



<a id="id3.1"></a>

### Mutations

<!-- @todo -->



<a id="id5"></a>

### Types

<!-- @todo -->



***
<br />
<br />

<a id="deploy"></a>

## Deployment

To deploy this project:

```bash
  ## todo
```

### Run Locally

Python is required.

1. Clone the project

```bash
  git clone https://github.com/QuickCrafts/PerfectPick_ag.git
```

2. Go to the project directory

```bash
  cd PerfectPick_ag
```

3. Start the server

```bash
  make run
```

If it's the first time run

```bash
  ./init.sh && make run
```