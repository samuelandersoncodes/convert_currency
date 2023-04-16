import requests
import tkinter as tk
from tkinter import *
from tkinter import ttk

class CurrencyConverter():
    """
    Main class.
    Its first method requests data from the requests library.
    The second method does the currency conversion 
    and limits the conversion's decimal places to four.
    """
    def __init__(self, url):
        """
        This method requests data from the requests library.
        """
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']

    def convert(self, from_currency, to_currency, amount):
        """
        This method processes the currency conversion 
        and limits the converted amount to four decimal places.
        """
        initial_amount = amount
        if from_currency != 'USD':
            amount = amount / self.currencies[from_currency]
        # limits the decimal places to four
        amount = round(amount * self.currencies[to_currency], 4)
        return amount

class App(tk.Tk):
    """
    Class for the app frames and labels. 
    """
    def __init__(self, converter):
        """
        This method facilitates inheritance from the tk package for the widget design
        It is responsible for creating the app widget and positioning them unto the frame
        for the frame to be loaded onto the window
        """      
        tk.Tk.__init__(self)
        self.title = 'Currency Converter'
        self.currency_converter = converter
        
api_url = 'https://api.exchangerate-api.com/v4/latest/USD'      
CurrencyConverter(api_url)