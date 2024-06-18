from motor.motor_asyncio import AsyncIOMotorClient

mongo_uri = "mongodb://localhost:27017"
client = AsyncIOMotorClient(mongo_uri)
database = client["lorestanuniv3"]
