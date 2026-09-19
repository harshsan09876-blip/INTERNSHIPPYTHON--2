import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

print("status: ", response.status_code)
print("Data: ", response.json())


import requests

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

print("status: ", response.status_code)
print("Data: ", response.json())


import requests

url = "https://jsonplaceholder.typicode.com/posts"

new_post = {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
  }

response = requests.post(url, json=new_post)
print("status: ", response.status_code)
print("Data: ", response.json())

import requests
url = "https://jsonplaceholder.typicode.com/posts/1"

new_data = {
    "userId": 1,
  "id": 1,
  "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
  "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"

}

response = requests.put(url, json=new_data)
print("status: ", response.status_code)
print("Data: ", response.json())


url = "https://jsonplaceholder.typicode.com/posts/1"
new_data = {
    "title": "updated title"
}

response = requests.patch(url, json=new_data)
print("status: ", response.status_code)
print("Data: ", response.json())


url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.delete(url)

print("status: ", response.status_code)

if response.status_code == 200:
    print("Post deleted successfully.")
else:
    print("Fialed to delete the post.")

