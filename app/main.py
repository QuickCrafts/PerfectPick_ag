import strawberry
from fastapi import FastAPI
from strawberry.asgi import GraphQL
from starlette.middleware.cors import CORSMiddleware
import httpx


@strawberry.type
class User:
    name: str
    age: int

@strawberry.type
class Other:
    name: str


@strawberry.type
class Query:
    @strawberry.field
    def user(self) -> User:
        return User(name="Patrick", age=100)
    @strawberry.field
    def another(self) -> Other:
        return Other(name="Hey")


schema = strawberry.Schema(query=Query)


graphql_app = GraphQL(schema)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)

# Syntax for HTTP requests to Microservices
@app.get("/Users")
async def testFetch():
    api_url = "http://localhost:8080/Users"
    async with httpx.AsyncClient() as client:
        response = await client.get(api_url)
        print(response.json())
        return response.json()
