#!/usr/bin/env python3
from bs4 import BeautifulSoup

def gen_qa_index(filename):
	soup = BeautifulSoup(open(filename), "html.parser")
	faq = soup.find("a", {"name": "faq"})
	faq_titles = faq.parent.find_next_siblings("h3")

	print("<ul>")
	for title in faq_titles:
		anchor = title.find("a")
		print('\t<li><a href="#{anchor}">{title}</a></li>'.format(title=anchor.text, anchor=anchor["name"]))
	print("</ul>")


if __name__ == "__main__":
	gen_qa_index("index.html")

