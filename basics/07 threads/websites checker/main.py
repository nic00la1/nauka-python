from websites import *
import os, sys
import threading, time
import requests

scriptDir = os.path.dirname(__file__)
os.chdir(scriptDir)

websites = Websites("websites.txt") 