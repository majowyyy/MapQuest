import urllib.parse
import requests
from tkinter import *

#Create an instance of tkinter window or frame
win=Tk()
win.resizable(False, False)
win.title("Map Quest with Gas Calculator")
startloc,destloc,gas = "","",""
main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "MhvbvH6lJAKgMu9wisKM5iSoZWOFFPQJ"
traffic_api = "http://www.mapquestapi.com/search/v2/radius?"
alternative_api = "http://www.mapquestapi.com/directions/v2/alternateroutes?"

#function to get the direction from starting location to destination city
def get_direction():
        url = main_api + urllib.parse.urlencode({"key":key, "from":startloc, "to":destloc})
        alt_url = alternative_api + urllib.parse.urlencode({"key":key, "from":startloc, "to":destloc})
        json_data = requests.get(url).json()
        json_data_alt = requests.get(alt_url).json()

        json_status = json_data["info"]["statuscode"]

        # if successfull, display the result
        if json_status == 0:

                navigate.destroy()
                Label( win, text="Destination City Location").pack()
                Label( win, text="Here are the Directions from " + (startloc) + " to " + (destloc)).pack()

                Label( win, text="Total Trip Duration: " + (json_data["route"]["formattedTime"])).pack()
                Label( win, text="Kilometers: " + str("{:.2f}".format(json_data["route"]["distance"] * 1.6))).pack()
                Label( win, text="Fuel Used (Ltr): " + str("{:.3f}".format(json_data["route"]["fuelUsed"]*3.78))).pack()
                Label( win, text="Amount of Money to be Spent on Fuel: " + str("{:.3f}".format(json_data["route"]["fuelUsed"]*3.78 *int(gas)))).pack()

                Label( win, text="Alternative Route: Total Trip Duration: " + (json_data_alt["route"]["formattedTime"])).pack()
                Label( win, text="Alternative route: Kilometers: " + str("{:.2f}".format(json_data_alt["route"]["distance"] * 1.6))).pack()
                Label( win, text="Alternative Route: Fuel Used (Ltr): " + str("{:.3f}".format(json_data_alt["route"]["fuelUsed"]*3.78))).pack()
                Label( win, text="Alternative Route: Amount of Money to be Spent on Fuel: " + str("{:.3f}".format(json_data_alt["route"]["fuelUsed"]*3.78 *int(gas)))).pack()
