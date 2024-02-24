from flask import Flask, request
from google_books_api_wrapper.api import GoogleBooksAPI
import requests

client = GoogleBooksAPI()

def getEvents():
    pass

def getTextBookLinks(course_description):
    file = open('C:\\Users\\daved\\OneDrive\\Documents\\Projects\\Student Assistant\\api_keys\\google_api_key.txt', 'r')
    myAPIKey = file.readline()
    url = f"https://www.googleapis.com/books/v1/volumes?q={course_description}&key={myAPIKey}"
    response = requests.get(url)
    #print(response.json()['items'][0]['volumeInfo']['previewLink'])
    bookLinks = [response.json()['items'][i]['volumeInfo']['infoLink'] for i in range(len(response.json()['items']))]
    bookLinksDict = {}
    for i in range(len(bookLinks)):
        bookLinksDict[response.json()['items'][i]['volumeInfo']['title']] = bookLinks[i]
    #print(bookLinksDict)
    file.close()
    return bookLinksDict
if __name__ == "__main__":
    pass
    #print(getTextBookLinks("Circuit element definitions. Circuit laws: Ohm&#8217;s, KVL, KCL. Resistive voltage and current dividers. Basic loop and nodal analysis. Dependent sources. Circuit theorems: linearity, superposition, maximum power transfer, Thevenin, Norton. Time domain behavior of inductance and capacitance, energy storage. Sinusoidal signals, complex numbers, phasor and impedance concepts. Magnetically coupled networks. Single phase power and power factor."))

# Circuit element definitions. Circuit laws: Ohm&#8217;s, KVL, KCL. Resistive voltage and current dividers. Basic loop and nodal analysis. Dependent sources. Circuit theorems: linearity, superposition, maximum power transfer, Thevenin, Norton. Time domain behavior of inductance and capacitance, energy storage. Sinusoidal signals, complex numbers, phasor and impedance concepts. Magnetically coupled networks. Single phase power and power factor.