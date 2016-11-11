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
      init functie van threading.

      :param url: URI van de NS api die ingeladen moet worden
      :param filename: File waar de data in opgeslagen moet worden.
      """
      super(NsRequest, self).__init__() # roep Thread aan.
      filePath = "assets/database/"
      self.auth_details = ('tjibbe.vanderende@student.hu.nl', 'yp9PbnRHnhWx-gBERapPKMy1o792T6U20D9Xw2W47xr8fvek-TvS9g')
      self.url = url
      self.filename = filePath+filename

    def _request(self):
        """
        request aan de NS API server doen en in een xml file zetten voor offline gebruik.
        """
        try:
          stations = requests.get(self.url, auth=self.auth_details)
          with open(self.filename, 'w', encoding='utf-8') as stationsXML:
            stationsXML.write(stations.text)
        except requests.HTTPError:
            print('An HTTP error has occurred')
        except FileNotFoundError:
            print('File could not be found')
        except KeyError:
            print('A Key Error has occurred')
        except requests.ConnectionError:
            print('A Connection Error has occurred')
        except requests.Timeout:
            print('Either the connection has timed out, or the server did not send any data in the allotted time.')

    def run(self):
      return self._request()
