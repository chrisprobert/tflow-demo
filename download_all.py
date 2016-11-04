#!/usr/bin/env python

import urllib2
import logging

logging.basicConfig(
    format='%(levelname)s %(asctime)s %(message)s', level=logging.DEBUG)

with open('imagenet_10k_urls.txt', 'r') as fp:
	lines = fp.readlines()[:5000]

for line in lines:
	url = line.split()[1]
	fname = line.split()[0] + ".jpg"
	logging.info("downloading %s" % fname)
	try :
		response = urllib2.urlopen(url, timeout=3)
		data = response.read()
		with open(fname, 'w') as fp:
			fp.write(data)
	except :
		logging.error("caught an error")
		continue
