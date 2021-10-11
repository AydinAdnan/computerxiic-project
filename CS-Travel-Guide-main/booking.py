"""Module name : Booking.py
   Module containing booking related functions"""

import webbrowser


def yatra():
   place = input("\nEnter Destination : ")
   adults = int(input("Enter total number of Adults : "))
   children = int(input("Enter total number of children : "))
   yatra = ("https://www.yatra.com/pwa/hotels/srp?roomRequests[0].id=1&roomRequests[0].noOfAdults={}&roomRequests[0].noOfChildren={}&source=BOOKING_ENGINE&pg=1&tenant=B2C&isPersnldSrp=1&city.name={}&city.code={}&state.name=KER&state.code=KER&country.name=India&country.code=IND".format(
       adults, children, place, place))
   print("You are being redirected")
   webbrowser.open(yatra, new=1)


def easemytrip():
   destination = input("Enter your Destination : ")
   checkin = input("Enter Check-in date in format DD/MM/YYYY : ")
   checkout = input("Enter Check-out date in format DD/MM/YYYY : ")
   pax = input("Enter number of adults : ")
   rooms = input("Enter number of rooms required : ")
   easemytrip = ("https://hotels.easemytrip.com/newhotel/Hotel/HotelListing?e=202193214436&city={},%20India&cin={}&cOut={}&Hotel=NA&Rooms={}&pax={}".format(
       destination, checkin, checkout, rooms, pax))
   print("You are being redirected")
   webbrowser.open(easemytrip, new=1)
