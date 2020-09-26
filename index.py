# not that I need them, just as an example
import requests
import json

def main(event, context):
   text = event['data']['text']
   return text
