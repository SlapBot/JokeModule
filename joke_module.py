import requests
import random
from bs4 import BeautifulSoup
from Stephanie.Modules.base_module import BaseModule


class JokeModule(BaseModule):
	def __init__(self, *args):
		super().__init__(*args)
		self.requests = requests

	def tell_joke(self):
		try:
			r = self.requests.get("http://www.goodbadjokes.com/")
			soup = BeautifulSoup(r.text, 'html.parser')
			posts = soup.find_all("div", class_="post index")
			if len(posts) > 0:
				index = random.randint(0, len(posts))
				joke = posts[index].find('a').text
			else:
				joke = "Couldn't fetch any new jokes, but don't feel bad, you are not any better"
			return joke
		except Exception:
			return "Couldn't fetch any new jokes, but don't feel bad, you are not any better"
