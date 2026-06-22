import requests

response = requests.get(
    "https://api.themoviedb.org/3/movie/5?api_key=13cf3587f132337dc3b9c3728695ec5a&language=en-US"
)

print(response.status_code)
print(response.json())