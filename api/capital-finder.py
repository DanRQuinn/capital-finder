from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # parse the query from path
        path = self.path
        url_components = parse.urlparse(path)
        query_string_list = parse.parse_qs(url_components.query)
        dic = dict(query_string_list)

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        country = dic['country']
        capital = dic['capital']
        if country:
            url = "https://restcountries.com/v3.1/name"
            message = ''
            response = requests.get(url + country)
            country_data = response.json()
            country_object = country_data[0]['capital'][0]
            message = str(f'The capitol of {country} is {country_object}')
            self.wfile.write(message.encode())
            return

        elif capital:
            url = "https://restcountries.com/v3.1/capital"
            message = ''
            response = requests.get(url + capital)
            capital_data = response.json()
            capital_object = capital_data[0]['name']['common']
            message = str(f'{capital} is the capital of {capital_object}.')
            self.wfile.write(message.encode())
            return

    