import bs4
import requests

# result = requests.get("https://quotes.toscrape.com")
# soup = bs4.BeautifulSoup(result.text,'lxml')
# print(soup)

# 3rd problem
result = requests.get("https://quotes.toscrape.com/page/1/")
soup = bs4.BeautifulSoup(result.text,'lxml')
authors_on_first_page = soup.select('.author')

auth_list = set()
for auth_name in authors_on_first_page:
    auth_list.add(auth_name.getText())

# print(auth_list)

# 4th Problem
quotes = soup.select('.text')

quote_list = []
for quote in quotes:
    quote_list.append(quote.getText())


# print(quote_list)

# 5th problem
tags = soup.select('.tag-item')
top_ten_tags = []

for tag in tags:
    top_ten_tags.append(tag.getText().replace('\n',''))

# print(top_ten_tags)


# 7th problem

base_url = "https://quotes.toscrape.com/page/{}"

uniq_auth_list = set()

for n in range(1,11):

    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)

    soup = bs4.BeautifulSoup(res.text,'lxml')
    authors_list = soup.select('.author')

    for name in authors_list:
        uniq_auth_list.add(name.text)


print(uniq_auth_list)