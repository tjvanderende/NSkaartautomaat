import requests
import xmltodict
import threading

"""
De data wordt steeds overgezet naar een lokaal bestand (.xml).
Zodat er eigenlijk een lokale database wordt gegenereerd en de API ook zonder internet werkt.
"""
class NsRequest (threading.Thread):
    def __init__(self, url, filename):
      """

      :param url: URI van de NS api die ingeladen moet worden
      :param filename: File waar de data in opgeslagen moet worden.
      """
      super(NsRequest, self).__init__() # roep Thread aan.
      filePath = "assets/database/"
      self.auth_details = ('tjibbe.vanderende@student.hu.nl', 'yp9PbnRHnhWx-gBERapPKMy1o792T6U20D9Xw2W47xr8fvek-TvS9g')
      self.url = url
      self.filename = filePath+filename

    def request(self):
        stations = requests.get(self.url, auth=self.auth_details)
        with open(self.filename, 'w', encoding='utf-8') as stationsXML:
            stationsXML.write(stations.text)
        return stations.status_code == 200

    def run(self):
      return self.request()
