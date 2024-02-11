import requests

def call_add_numbers_api(x, y, server_ip):
    url = f'{server_ip}/add_numbers'  # Replace <server_ip> with the IP address of your server

    payload = {'x': x, 'y': y}
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        result = response.json()['result']
        print(f"The result of {x} + {y} is {result}.")
    else:
        print("Error:", response.json()['error'])

if __name__ == "_main_":
    # Example usage
    call_add_numbers_api(5, 3,'172.16.13.137')