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


