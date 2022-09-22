import urllib.parse
import requests
from tkinter import *

#Create an instance of tkinter window or frame
win=Tk()
win.resizable(False, False)
win.title("Map Quest with Gas Calculator")
orig,dest,gas = "","",""
main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "MhvbvH6lJAKgMu9wisKM5iSoZWOFFPQJ"
traffic_api = "http://www.mapquestapi.com/search/v2/radius?"
alternative_api = "http://www.mapquestapi.com/directions/v2/alternateroutes?"

#function to get the direction from source to destionation city
def get_direction():
        url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
        alt_url = alternative_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
        json_data = requests.get(url).json()
        json_data_alt = requests.get(alt_url).json()

        json_status = json_data["info"]["statuscode"]

        # if successfull, display the result
        if json_status == 0:

                navigate.destroy()
                Label( win, text="Destination City").pack()
                Label( win, text="Directions from " + (orig) + " to " + (dest)).pack()

                Label( win, text="Trip Duration: " + (json_data["route"]["formattedTime"])).pack()
                Label( win, text="Kilometers: " + str("{:.2f}".format(json_data["route"]["distance"] * 1.6))).pack()
                Label( win, text="Fuel Used (Ltr): " + str("{:.3f}".format(json_data["route"]["fuelUsed"]*3.78))).pack()
                Label( win, text="Money to be Spent on Fuel: " + str("{:.3f}".format(json_data["route"]["fuelUsed"]*3.78 *int(gas)))).pack()

                Label( win, text="Alternative Route: Trip Duration: " + (json_data_alt["route"]["formattedTime"])).pack()
                Label( win, text="Alternative route: Kilometers: " + str("{:.2f}".format(json_data_alt["route"]["distance"] * 1.6))).pack()
                Label( win, text="Alternative Route: Fuel Used (Ltr): " + str("{:.3f}".format(json_data_alt["route"]["fuelUsed"]*3.78))).pack()
                Label( win, text="Alternative Route: Money to be Spent on Fuel: " + str("{:.3f}".format(json_data_alt["route"]["fuelUsed"]*3.78 *int(gas)))).pack()
        
                #display the route result in a scrollbar
                scrollbar.pack(side=RIGHT, fill = Y)
                myList = Listbox(win,  yscrollcommand=scrollbar.set, width=100)

                for each in json_data["route"]["legs"][0]["maneuvers"]:
                        narrative = each["narrative"] + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)")
                        myList.insert(END, narrative)

                myList.pack(side=LEFT, fill=BOTH)
                scrollbar.config(command=myList.yview)

                #display the route result in a scrollbar
                scrollbar.pack(side=RIGHT, fill = Y)
                myList = Listbox(win,  yscrollcommand=scrollbar.set, width=100)

                for each in json_data_alt["route"]["legs"][0]["maneuvers"]:
                        narrative = each["narrative"] + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)")
                        myList.insert(END, narrative)
                        
                myList.pack(side=LEFT, fill=BOTH)
                scrollbar.config(command=myList.yview)

                #display the route result in a scrollbar
                scrollbar.pack(side=RIGHT, fill = Y)
                myList = Listbox(win,  yscrollcommand=scrollbar.set, width=100)

                #button to close the application
                Button(win, height=1, width=10, text="Close ", command=destroy).pack()
                lbl.destroy()

        elif json_status == 402:
                msg.set("INVALID LOCATION!")
                lbl.pack()
        elif json_status == 611:
                msg.set("INVALID LOCATION!")
                lbl.pack()
        else:
                msg.set("SOMETHING WENT WRONG!")
                lbl.pack()

#function that will get the value of text box
def get_input():
   global orig
   global dest
   global gas
   orig = source_txt.get(1.0, "end-1c")
   dest = destination_txt.get(1.0, "end-1c")
   gas = gas_txt.get(1.0, "end-1c")
   if(orig and dest and gas):
       if(gas.isdigit()):
        get_direction()
       else:
        msg.set("GAS PRICE MUST BE INTEGER!")
        lbl.pack()    
   else:
       msg.set("PLEASE FILL OUT THE FORM!")
       lbl.pack()

#creating a result label that will be displayed on the window
msg = StringVar()
lbl = Label( win, textvariable=msg)

#function to close the window
def destroy():
        win.destroy()

#Creating a text box and label widget for source city
source_lbl = Label( win, text="Source City")
source_txt=Text(win, height=2, width=40)
source_lbl.pack()
source_txt.pack()

#Creating a scrollbar widget for result
scrollbar = Scrollbar(win)

#Creating a text box and label widget for destination city
destination_lbl = Label( win, text="Destination City")
destination_txt=Text(win, height=2, width=40)
destination_lbl.pack()
destination_txt.pack()

#Creating a text box and label widget for gas price
gas_lbl = Label( win, text="Gas Price")
gas_txt=Text(win, height=2, width=40)
gas_lbl.pack()
gas_txt.pack()

#Create a button for navigate
navigate= Button(win, height=1, width=10, text="Navigate", command=get_input)
navigate.pack()

win.mainloop() 