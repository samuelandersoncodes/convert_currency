import requests
import tkinter as tk
from tkinter import *
from tkinter import ttk

class CurrencyConverter():
    """
    Main class.
    Its first method requests data from the requests library.
    """
    def __init__(self, url):
        """
        This method requests data from the requests library.
        """
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']