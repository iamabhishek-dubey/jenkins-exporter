#!/usr/bin/python
import json
import re
import sys
import time
import urllib2

from prometheus_client import start_http_server
from prometheus_client.core import GaugeMetricFamily, REGISTRY

