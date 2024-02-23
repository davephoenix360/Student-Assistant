from flask import Flask, request
from google_books_api_wrapper.api import GoogleBooksAPI

client = GoogleBooksAPI()


def getEvents():
    pass

def getTextBooks(course_description):
    url = f"https://www.googleapis.com/books/v1/volumes?q={course_description}&key=myAPIKey"
    #myBooks = client.get_book_by_title(course_description)
    
    myBooks = client.get_book_by_url(url)
    
    print(myBooks.description)
    return myBooks

if __name__ == "__main__":
    print(getTextBooks("Circuit"))

# Circuit element definitions. Circuit laws: Ohm&#8217;s, KVL, KCL. Resistive voltage and current dividers. Basic loop and nodal analysis. Dependent sources. Circuit theorems: linearity, superposition, maximum power transfer, Thevenin, Norton. Time domain behavior of inductance and capacitance, energy storage. Sinusoidal signals, complex numbers, phasor and impedance concepts. Magnetically coupled networks. Single phase power and power factor.