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
        
        # Sets the dimension of the GUI window (WidthxHeight)
        self.geometry("530x200")

        # Label specifications for app title and date
        self.intro_label = Label(self, text = 'Your One Time Pocket Currency Converter', fg = 'black', bg='darkgray', relief = tk.RAISED, borderwidth = 3)
        self.intro_label.config(font = ('Courier',15,'bold'))
        self.date_label = Label(self, text = f" Date : {self.currency_converter.data['date']}", relief = tk.GROOVE, borderwidth = 5)
        # positions the above labels by absolute coordinates
        self.intro_label.place(x = 10 , y = 5)
        self.date_label.place(x = 200, y= 50)

        # Creates an entry box for amount input
        valid = (self.register(self.restrictNumberOnly), '%d', '%P')
        self.amount_field = Entry(self, bd = 3, relief = tk.RIDGE, justify = tk.CENTER,validate='key', validatecommand=valid)
        self.converted_amount_field_label = Label(self, text = '', fg = 'black', bg = 'white', relief = tk.RIDGE, 
        justify = tk.CENTER, width = 17, borderwidth = 3)

        # Creates dropdown values for the various currencies
        self.from_currency_variable = StringVar(self)
        self.from_currency_variable.set("INR") # default value
        self.to_currency_variable = StringVar(self)
        self.to_currency_variable.set("USD") # default value
        font = ("Courier", 12, "bold")
        self.option_add('*TCombobox*Listbox.font', font)
        self.from_currency_dropdown = ttk.Combobox(self, textvariable=self.from_currency_variable,values=
        list(self.currency_converter.currencies.keys()), font = font, state = 'readonly', width = 12, justify = tk.CENTER)
        self.to_currency_dropdown = ttk.Combobox(self, textvariable=self.to_currency_variable,values=
        list(self.currency_converter.currencies.keys()), font = font, state = 'readonly', width = 12, justify = tk.CENTER)


api_url = 'https://api.exchangerate-api.com/v4/latest/USD'      
CurrencyConverter(api_url)