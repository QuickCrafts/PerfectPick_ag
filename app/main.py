import strawberry
from fastapi import FastAPI
from strawberry.asgi import GraphQL
from starlette.middleware.cors import CORSMiddleware
from app.GraphQL.Companies.companiesMutations import CreateCompany, UpdatedCompany
from app.GraphQL.Companies.companiesType import CompanyId
from app.GraphQL.Release.releaseMutations import PublishAd
from app.GraphQL.Users.userQueries import GetAllUsers, GetSingleUser, EmailLogin, GoogleLogin
from app.GraphQL.Users.userMutations import RegisterUser, VerifyAccount
from app.GraphQL.Users.userTypes import User, UserToken, GoogleURL, Other
from app.GraphQL.Payments.paymentsQueries import GetAllPayments, GetPaymentByAd, GetPaymentByCompany, GetSinglePayment
from app.GraphQL.Payments.paymentType import Payment
from dotenv import load_dotenv
from app.utils import Authenticate

load_dotenv()


@strawberry.type
class Query:
    @strawberry.field
    async def GetUsers(self, userToken: str) -> list[User]:
        isTokenValid = await Authenticate(userToken)
        if isTokenValid["isTokenValid"] == False:
            raise ValueError("Invalid Token, user not authorized")
        return await GetAllUsers()
    
    @strawberry.field
    async def GetUserByUserID(self, userID: int, userToken: str) -> User:
        isTokenValid = await Authenticate(userToken)
        if isTokenValid["isTokenValid"] == False:
            raise ValueError("Invalid Token, user not authorized")
        potentialData = await GetSingleUser(userID=userID)
        if potentialData is None:
            raise ValueError("User not found")
        else:
            return potentialData
        
    @strawberry.field
    async def LoginWithEmail(self, email: str, password: str) -> UserToken:
        userToken = await EmailLogin(email=email, password=password)
        if userToken is None:
            raise ValueError("User not found")
        else:
            return userToken
        
    @strawberry.field
    async def LoginWithGoogle(self) -> GoogleURL:
        userToken = await GoogleLogin()
        if userToken is None:
            raise ValueError("User not found")
        else:
            return userToken
        
    @strawberry.field
    async def BillsByCompanyId (self,  userToken: str ,companyID: int) -> list[Payment]:
        isTokenValid = await Authenticate(userToken)
        if isTokenValid["isTokenValid"] == False:
            raise ValueError("Invalid Token, user not authorized")
        if isTokenValid["role"] != 1:
            raise ValueError("User not authorized")
        potentialData = await GetPaymentByCompany(companyID=companyID)
        if potentialData is None:
            raise ValueError("Bills not found")
        else:
            return potentialData
    
    @strawberry.field
    async def BillsByAdId (self,  userToken: str ,adID: int) -> list[Payment]:
        isTokenValid = await Authenticate(userToken)
        if isTokenValid["isTokenValid"] == False:
            raise ValueError("Invalid Token, user not authorized")
        if isTokenValid["role"] != 1:
            raise ValueError("User not authorized")
        potentialData = await GetPaymentByAd(adID=adID)
        if potentialData is None:
            raise ValueError("Bills not found")
        else:
            return potentialData

    @strawberry.field
    async def AllBills (self,  userToken: str) -> list[Payment]:
        isTokenValid = await Authenticate(userToken)
        if isTokenValid["isTokenValid"] == False:
            raise ValueError("Invalid Token, user not authorized")
        if isTokenValid["role"] != 1:
            raise ValueError("User not authorized")
        potentialData = await GetAllPayments()
        if potentialData is None:
            raise ValueError("Bills not found")
        else:
            return potentialData
    
    @strawberry.field
    async def BillById (self,  userToken: str, idPayment: int) -> Payment:
        isTokenValid = await Authenticate(userToken)
        if isTokenValid["isTokenValid"] == False:
            raise ValueError("Invalid Token, user not authorized")
        if isTokenValid["role"] != 1:
            raise ValueError("User not authorized")
        potentialData = await GetSinglePayment(idPayment=idPayment)
        if potentialData is None:
            raise ValueError("Bill not found")
        else:
            return potentialData

@strawberry.type
class Mutation:
    @strawberry.field
    async def RegisterWithEmail(self, email: str, password: str, firstName: str, lastName: str, birthdate: str, role: bool) -> UserToken:
        userToken = await RegisterUser(email=email, password=password, firstName=firstName, lastName=lastName, birthdate=birthdate, role=role)
        if userToken is None:
            raise ValueError("User not found")
        else:
            return userToken
    
    @strawberry.field
    async def VerifyUserAccount(self, token: str) -> Other:
        message = await VerifyAccount(token=token)
        if message is None:
            raise ValueError("User not found")
        else:
            return message
        
    @strawberry.field
    async def CreateCompany(self,userToken: str, name: str, email: str) -> CompanyId:
        isTokenValid = await Authenticate(userToken)
        if isTokenValid["isTokenValid"] == False:
            raise ValueError("Invalid Token, user not authorized")
        if isTokenValid["role"] != 1:
            raise ValueError("User not authorized")
        company = await CreateCompany(name=name, email=email)
        if company is None:
            raise ValueError("Company not created")
        else:
            return company

    @strawberry.field
    async def UpdateCompany (self, userToken: str, companyId:int, name: str, email: str) -> CompanyId:
        isTokenValid = await Authenticate(userToken)
        if isTokenValid["isTokenValid"] == False:
            raise ValueError("Invalid Token, user not authorized")
        if isTokenValid["role"] != 1:
            raise ValueError("User not authorized")
        company = await UpdatedCompany(companyId=companyId, name=name, email=email)
        if company is None:
            raise ValueError("Company not updated")
        else:
            return company
        
    @strawberry.field
    async def PublishAd(self, userToken: str, adID: int) -> Other:
        isTokenValid = await Authenticate(userToken)
        if isTokenValid["isTokenValid"] == False:
            raise ValueError("Invalid Token, user not authorized")
        if isTokenValid["role"] != 1:
            raise ValueError("User not authorized")
        publish = await PublishAd(adID=adID)
        
        return publish

schema = strawberry.Schema(query=Query, mutation=Mutation)


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
    return await Authenticate("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjZXJ0c2VyaWFsbnVtYmVyIjoiMmo2Mm9PQUNya1BBbWc2SS9WV2Q3QT09IiwibmJmIjoxNzExMzg3MTc4LCJleHAiOjE3MTE0MDE1NzgsImlhdCI6MTcxMTM4NzE3OH0.g-_vB7PcG4_BqU-m1qQGXtUDcSeWfcTZhV6boBRJP9Q")

