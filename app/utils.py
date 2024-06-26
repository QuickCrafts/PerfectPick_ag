import httpx
import os


async def Authenticate(userToken: str):
    api_url = os.environ.get("USERS_URL")
    print("we are here")
    print(api_url)
    auth_url = api_url + "/Users/verify/" + userToken
    print(auth_url)
    async with httpx.AsyncClient() as client:
        response = await client.get(auth_url)
        if response.status_code == 200:
            isTokenValid = True
        else:
            isTokenValid = False
        return{
            "isTokenValid": isTokenValid,
            "Code": response.status_code,
        }
    
async def CheckAdmin(id:int):
    api_url = os.environ.get("USERS_URL")
    auth_url = api_url + "/Users/verify/role/" + str(id)
    async with httpx.AsyncClient() as client:
        response = await client.get(auth_url)
        if response.status_code == 500:
            raise ValueError("Couldn't check if user is admin")
        
        data = response.json()
        isAdmin = data["isAdmin"]
        return{
            "isAdmin": isAdmin,
            "Code": response.status_code,
            "role": response.text.role,
        }