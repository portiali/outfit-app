# client-side pyhton app for outfit app, which is calling
# a set of lambda functions in AWS through API Gateway
# the overall purpose of the app is to recommend users an outfit
# based no images of clothes in their outfit and weather
#
# Authors: 
# Portia Li & Mariana Ma
#
# Northwestern University
# CS 310
#

import requests
import jsons

import random
import uuid
import pathlib
import logging
import sys
import os
import base64
import time

from configparser import ConfigParser


# functions: 
# outfit()
#   returns outfit in a folder? -- resized and everything


# upload()
#   allows user to continously upload outfits to S3
#   should call sagemaker-- server side probs
#   also return a description of what sagemaker analyzed
#   loop continously until user says no more clothes left to upload

# weather()
#   abstraction from user-- but should get the weather data from weather API
#   makes clothing decisions accordingly


# main:
#   initial welcome prompt, ask for username, assign user id accordingly

############################################################
#
# classes
#
class Data:

  def __init__(self, row):
    self.dataid = row[0]
    self.clothingid = row[1]
    self.gender = row[2]
    self.category = row[3]
    self.articleType = row[4]
    self.color = row[5]
    self.season = row[6]
    self.usage = row[7]

class User:
   def __init__(self, row):
      self.userid = row[0]
      self.username = row[1]

###################################################################
#
# web_service_get
#
# When calling servers on a network, calls can randomly fail. 
# The better approach is to repeat at least N times (typically 
# N=3), and then give up after N tries.
#
def web_service_get(url):
  """
  Submits a GET request to a web service at most 3 times, since 
  web services can fail to respond e.g. to heavy user or internet 
  traffic. If the web service responds with status code 200, 400 
  or 500, we consider this a valid response and return the response.
  Otherwise we try again, at most 3 times. After 3 attempts the 
  function returns with the last response.
  
  Parameters
  ----------
  url: url for calling the web service
  
  Returns
  -------
  response received from web service
  """

  try:
    retries = 0
    
    while True:
      response = requests.get(url)
        
      if response.status_code in [200, 400, 480, 481, 482, 500]:
        #
        # we consider this a successful call and response
        #
        break
      #
      # failed, try again?
      #
      retries = retries + 1
      if retries < 3:
        # try at most 3 times
        time.sleep(retries)
        continue
          
      #
      # if get here, we tried 3 times, we give up:
      #
      break

    return response

  except Exception as e:
    print("**ERROR**")
    logging.error("web_service_get() failed:")
    logging.error("url: " + url)
    logging.error(e)
    return None
############################################################
#
# get_or_create_user
#

def get_or_create_user(baseurl):
    try: 
        
        # /usernames is called in main and passed in here as a list
        username = input("Enter your username: ")
        api = "/users"
        url = baseurl + api

        # prepare the data to send as JSON in POST body
        data = {
           "username": username
        }


        #POST req to add new user if they don't exist 
        # and to retrieve data of user if they do
        res = requests.post(url, json=data)
        
        if res.status_code == 200:
           body = res.json()
           message = body['message']
           print(message)
           return body['userid']
        elif res.status_code == 500:
           body = res.json()
           message = body['message']
           print(message)
           return
        else:
           body = res.json()
           print(body)
           return
           
    except Exception as e:
        print("**ERROR")
        print("**ERROR: invalid input")
        print("**ERROR")
        return -1



    
############################################################

# main 
#

try:
    print('** Welcome to Pick-a-Fit! **\n')
    print("Let's get you started.\n")
    print()

    # eliminate traceback so we just get error message:
    sys.tracebacklimit = 0

    #
    # what config file should we use for this session?
    #
    config_file = 'outfitapp-client-config.ini'

    #
    # setup base URL to web service:
    #
    configur = ConfigParser()
    configur.read(config_file)
    baseurl = configur.get('client', 'webservice')

    #
    # make sure baseurl does not end with /, if so remove:
    #
    if len(baseurl) < 16:
        print("**ERROR: baseurl '", baseurl, "' is not nearly long enough...")
        sys.exit(0)

    if baseurl.startswith("http:"):
        print("**ERROR: your URL starts with 'http', it should start with 'https'")
        sys.exit(0)

    lastchar = baseurl[len(baseurl) - 1]
    if lastchar == "/":
        baseurl = baseurl[:-1]

    #get user's username or create a new user based on username
    userid = get_or_create_user(baseurl)    

    # couldn't access username/couldn't insert user
    if not userid:
       print('Error with user, please try again')
       sys.exit(1)

    #
    # done
    #
    print()
    print('** done **')
    sys.exit(0)

except Exception as e:
    logging.error("**ERROR: main() failed:")
    logging.error(e)
    sys.exit(0)
