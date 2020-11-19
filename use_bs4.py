import requests

url = 'https://detik.com'
try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f'Sucess! {response}')
        # print(f'Content {response.text}')
        soup = BeautifulSoup
    else:
        print(f'Woops, ada kesalahan requests {response.status_code}')
except Exception as e:
    print('There is an error', e)
print('Program ended')
