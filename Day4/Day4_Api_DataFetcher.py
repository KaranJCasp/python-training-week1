'''import requests
1. API Data Fetcher
Using JSONPlaceholder API (https://jsonplaceholder.typicode.com):
Fetch list of users from /users endpoint
Print each user's name and email
Handle connection errors gracefully

Sample Output:
Users List:
Leanne Graham - Sincere@april.biz
Ervin Howell - Shanna@melissa.tv'''

import requests
import json
import pprint

def userData(url):
    response=requests.get(url)
    if(response.status_code==200):
        data=response.json()
        print("--- Formatted JSON Output ---")
        if(data):
            for i in range(len(data)):
                print(data[i]['name'],"-",data[i]['email'])

        else:
            print(f'data is empty')
        # print(json.dumps(data, indent=4)) # here indet = 4 mean that show in json data in 4  spaces
        # print("\n--- Pretty-Printed Python Object ---")
        # pprint.pprint(data)
        
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")


if __name__ == "__main__":
    userData("https://jsonplaceholder.typicode.com/users")
