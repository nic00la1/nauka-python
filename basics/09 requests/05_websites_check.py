import tkinter as tk
from tkinter import messagebox
import requests
from threading import Thread
import time
from datetime import datetime

class WebsiteCheckerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Website Checker")
        self.geometry("800x600")
        self.websites = [
            {"url": "https://onet.pl", "last_checked": None},
            {"url": "https://ithardware.pl", "last_checked": None},
            {"url": "https://dsfgthy43w89i.pl", "last_checked": None},
        ] # Dodane strony na starcie
        self.create_widgets()
        self.update_websites_list()
        Thre