import requests
import tkinter as tk
from tkinter import *
from tkinter import ttk

class CurrencyConverter():
    """
    Main class.
    Its first method requests data from the requests library.
    The second method does the currency conversion and limits the conversion's decimal places to four.
    """
    def __init__(self, url):
        """
        This method requests data from the requests library.
        """
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']

    def convert(self, from_currency, to_currency, amount):
        """
        This method processes the currency conversion and limits the converted amount to four decimal places.
        """
        initial_amount = amount
        if from_currency != 'USD':
            amount = amount / self.currencies[from_currency]
        # limits the decimal places to four
        amount = round(amount * self.currencies[to_currency], 4)
        return amount
        
api_url = 'https://api.exchangerate-api.com/v4/latest/USD'       
CurrencyConverter(api_url)