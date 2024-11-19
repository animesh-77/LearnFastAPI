# simple file to test the server response

import requests

# print("TESTS FOR SERVER")
# print(requests.get("http://localhost:8000").json())
# print(requests.get("http://127.0.0.1:8000").text)
# print("\n\n")


# print("TESTS FOR /items")
# print(requests.get("http://localhost:8000/items/0").json())
# # # also try with invalid id
# print(requests.get("http://localhost:8000/items/23").json())
# print(requests.get("http://localhost:8000/items/asd").json())

# print("\n\n")
# print("TESTS FOR /items/")
# print(requests.get("http://127.0.0.1:8000/items?name=Nails").json())
# print(requests.get("http://localhost:8000/items?name=Hammer").json())

# print(requests.get("http://127.0.0.1:8000/items?count=20").json())
# print(requests.get("http://127.0.0.1:8000/items?category=tools").json())


# # This request fails because 'ingredient' is not a valid category, as defined in the Category enum:
# print(requests.get("http://127.0.0.1:8000/items?category=ingredient").json())


# # These request fail because count has to be an integer:

# # Here, validation occurs because of the specified type hints on the endpoint.
# print(requests.get("http://127.0.0.1:8000/items/?count=Hello").json())

# And here, because of Pydantic we can pass
print(
    requests.post(
        "http://127.0.0.1:8000/",
        json={
            "name": "Screwdriver",
            "price": 3.99,
            "count": 12,
            "id": 4,
            "category": "tools",
        },
    ).json()
)

print(
    requests.put(
        "http://localhost:8000/update/4?name=RatchetScrewdriver"
    ).json()
)

print(requests.put("http://127.0.0.1:8000/update/4?price=-1").json())

print(requests.delete("http://127.0.0.1:8000/delete/4").json())
