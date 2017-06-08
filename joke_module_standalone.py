import requests
from bs4 import BeautifulSoup
import random

class JokeModule:
	def __init__(self):
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

if __name__ == '__main__':
	jk = JokeModule()
	print(jk.tell_joke())
