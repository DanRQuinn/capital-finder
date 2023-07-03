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
        url = "https://restcountries.com/v3.1/all"
        response = requests.get(url + country)
        data = response.json()
        defininitions = []
        for word_data in data:
            defininition = word_data['meanings'][0]['definition'][0]['definitions']
            defininitions.append(defininition)

        message = str(defininitions)
        self.wfile.write(message.encode())
        return
