# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from datetime import datetime

import urllib.parse
import urllib.request


class JourneeMondiale(object):

	@staticmethod
	def get(day_date=""):
		"""
		"""
		if not day_date:
			day_date = datetime.now().strftime("%d-%m")
		url = "https://www.journee-mondiale.com/date/%s.htm" % day_date
		html_content = urllib.request.urlopen(url).read()
		soup = BeautifulSoup(html_content, 'html.parser')
		titles = [e.get_text() for e in soup.findAll("h2", {"itemprop" : "name"})]
		return titles
