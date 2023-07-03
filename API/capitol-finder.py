from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # parse the query from path
        path = self.path
        url_components = parse.urlparse(path)
        query_string_list = parse.parse_qs(url_components.query)
        dic = dict

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        country = dic['country']
        # capitol = dic['capitol']
        url = "https://restcountries.com/v3.1/name"
        country_response = requests.get(url + country)
        # capitol_response = requests.get(url + capitol)

        country_data = country_response.json()
        # capitol_data = capitol_response.json()

        country_message = country_data[0]['name']['common']
        output_country = "The capitol of " + country + " is " + capitol
        # capitol_message = capitol_data[0]['name']['common']
        # output_capitol = "The capitol of " + capitol + " is " + country

        
        



        # capitol_message = str(output_capitol)
        country_message = str(output_country)
        self.wfile.write(country_message.encode())
        return
