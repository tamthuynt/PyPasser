from pypasser import reCaptchaV3
import re
import requests
from requests.utils import dict_from_cookiejar

def login():
    recaptcha_response = reCaptchaV3(
                "https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LeE-B8UAAAAADot-Vz7dAQ_5jXunhPg8qPzwMXa&co=aHR0cHM6Ly93d3cucGF5YmFjay5kZTo0NDM.&hl=en&v=vP4jQKq0YJFzU6e21-BGy3GP&size=invisible&badge=inline&cb=iqus9nttvr6j"
            )

if __name__ == '__main__':
    login()
