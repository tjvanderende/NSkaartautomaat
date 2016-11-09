import requests
import xmltodict
import threading


class NsRequest (threading.Thread):
    def __init__(self, url, filename):
      super(NsRequest, self).__init__()
      self.auth_details = ('tjibbe.vanderende@student.hu.nl', 'yp9PbnRHnhWx-gBERapPKMy1o792T6U20D9Xw2W47xr8fvek-TvS9g')
      self.url = url
      self.filename = filename

    def request(self):
        stations = requests.get(self.url, auth=self.auth_details)
        with open(self.filename, 'w', encoding='utf-8') as stationsXML:
            stationsXML.write(stations.text)
        return stations.status_code == 200

    def run(self):
      return self.request()
