import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

# -----------------------------
# In-memory "database"
# -----------------------------
db = {
    1: {"id": 1, "name": "John Doe"}
}

# -----------------------------
# GraphQL Type
# -----------------------------
@strawberry.type
class User:
    id: int
    name: str


# -----------------------------
# QUERY
# -----------------------------
@strawberry.type
class Query:
    @strawberry.field
    def user(self, id: int) -> User | None:
        user = db.get(id)
        if not user:
            return None
        return User(id=user["id"], name=user["name"])


# -----------------------------
# MUTATION
# -----------------------------
@strawberry.type
class Mutation:
    @strawberry.mutation
    def update_user_name(self, id: int, new_name: str) -> User:
        if id not in db:
            raise ValueError("User not found")

        db[id]["name"] = new_name
        return User(id=id, name=new_name)


# -----------------------------
# Schema
# -----------------------------
schema = strawberry.Schema(query=Query, mutation=Mutation)

# -----------------------------
# FastAPI App
# -----------------------------
app = FastAPI()
graphql_app = GraphQLRouter(schema)

app.include_router(graphql_app, prefix="/graphql")