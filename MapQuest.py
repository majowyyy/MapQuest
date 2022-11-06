import urllib.parse
import requests
from tkinter import *

#Create an instance of tkinter window or frame
win=Tk()
win.resizable(True, True)
win.title("Map Quest with Gas Calculator")
startloc,destloc,gas = "","",""
main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "MhvbvH6lJAKgMu9wisKM5iSoZWOFFPQJ"
traffic_api = "http://www.mapquestapi.com/search/v2/radius?"
alternative_api = "http://www.mapquestapi.com/directions/v2/alternateroutes?"
