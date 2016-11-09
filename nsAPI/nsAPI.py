import requests
import xmltodict
import threading

auth_details = ('tjibbe.vanderende@student.hu.nl', 'yp9PbnRHnhWx-gBERapPKMy1o792T6U20D9Xw2W47xr8fvek-TvS9g')
api_vertrek = 'http://webservices.ns.nl/ns-api-avt?station='
api_stationlijst = 'http://webservices.ns.nl/ns-api-stations-v2'

def stationlijst():
    stations = requests.get(api_stationlijst, auth=auth_details)
    with open('stationlijst.xml', 'w', encoding='utf-8') as stationsXML:
        stationsXML.write(stations.text)

def vertrektijden(station):
    api_vertrek_station = api_vertrek + station
    vertrektijd = requests.get(api_vertrek_station, auth=auth_details)

    with open('vertrektijden.xml', 'w') as myXMLFile:
        myXMLFile.write(vertrektijd.text)

station = str(input('Welk station wilt u de informatie van hebben? '))
vertrekThread = threading.Thread(name=vertrektijden, target=vertrektijden(station))
stationThread = threading.Thread(name=stationlijst, target=stationlijst)

vertrekThread.start()
stationThread.start()
