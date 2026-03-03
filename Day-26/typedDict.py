from typing import TypedDict

class Movie(TypedDict):
    title: str
    year: int
    rating: float

my_movie: Movie = {
    "title": "Inception",
    "year": 2010

}

print(my_movie)
print(my_movie["title"])
print(my_movie["year"])
print(my_movie.get("rating"))

my_movie["rating"] = 9
print(my_movie)

def process_movie(mov: Movie) -> None:
    print(f'Processing movie: {mov.get("title")} ({mov.get("year")} with rating {mov.get("rating")}')

process_movie(my_movie)

amovie = {
    "title": "The Matrix",
    "year": 1999,
    "rating": 8.7
}

process_movie(amovie)

m = {'title': 'Alice', 'year': 2020}
process_movie(m)


# Defining a TypedDict with optional keys
class Employee(TypedDict):
    name: str
    age: int
    department: str

emp1 = Employee = {
    "name": "RNS",
    "age": 13,
    "department": "Engineering"
}

# Accessing values
print(emp1.get("name"))

# Nested TypedDict
class Address(TypedDict):
    street: str
    city: str
    zip_code: str

class User(TypedDict):
    username: str
    email: str
    address: Address

user1: User = {
    "username": "john_doe",
    "email": "abc@gmail.com",
    "address": {
        "street": "123 Main St",
        "city": "Anytown"

    }
}

print(user1.get("address","").get("zip_code"))