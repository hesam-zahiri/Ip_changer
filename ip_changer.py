import requests

def change_ip_with_vpn():
    # Request proxy information from the user
    proxy_ip = input('Please enter the proxy IP: ')
    proxy_port = input('Please enter the proxy port: ')

    # Creating a proxy dictionary using the information received from the user
    proxy = {
        'http': f'http://{proxy_ip}:{proxy_port}',
        'https': f'https://{proxy_ip}:{proxy_port}'
    }

    try:
        response = requests.get('http://ipinfo.io/json', proxies=proxy)
        if response.status_code == 200:
            data = response.json()
            print('New IP address:', data['ip'])
        else:
            print('Error getting IP address')
    except requests.exceptions.RequestException as e:
        print('Error connecting to VPN proxy:', str(e))

# Error connecting to VPN proxy:
change_ip_with_vpn()

