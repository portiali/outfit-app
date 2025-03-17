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





