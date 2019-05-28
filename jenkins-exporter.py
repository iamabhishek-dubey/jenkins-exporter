#!/usr/bin/python3
from httplib2 import Http
import base64
import json
import time
import os
import signal
import faulthandler
from threading import Lock
from urllib.parse import urlencode, quote_plus
from prometheus_client import start_http_server
from prometheus_client.core import GaugeMetricFamily, REGISTRY
import logging
from pythonjsonlogger import jsonlogger

faulthandler.enable()

class JenkinsApiClient():
    def __init__(self, config)
    