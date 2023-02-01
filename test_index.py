from selenium import webdriver
import requests
import pytest

response = requests.get("https://www.google.com")

if response.status_code == 200:
    print("La solicitud ha sido exitosa.")
else:
    print("La solicitud ha fallado.")