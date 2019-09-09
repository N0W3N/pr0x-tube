import requests
from bs4 import BeautifulSoup as bs
import csv
import re

def init():

    r = requests.get('localhost/post-sitemap34.xml')
    soup = bs(r.text, 'html.parser')

    return soup


def links(soup):
    with open('eggs.csv', 'a+', newline = '') as csvfile:
        for link in soup.find_all('loc'):
            spamwriter = csv.writer(csvfile, delimiter=' ')
            link1 = link.text.strip('|')
            spamwriter.writerow([link1])
            print(link1)
    csvfile.close()

def content():

    i = 0

    with open('eggs.csv', 'r') as file:
        spamreader = csv.reader(file)
        for row in spamreader:
            link1 = ''.join(row)
            i += 1

            a = requests.get(link1)
            soup1 = bs(a.text, 'html.parser')

            with open('test%s.csv' % i, 'w+', newline = '') as con:
                spamwriter = csv.writer(con, delimiter=' ')
                for links in soup1.find('h1', class_ = 'entry-title'):
                    spamwriter.writerow(([links.strip()]))
                    print(links)

                for content in soup1.find_all('div', class_ = 'entry-content post_content'):
                    content1 = content.text
                    spamwriter.writerow([content1.strip()])
                    print(content)

                for category in soup1.find_all('footer', {"class": "entry-meta"}):
                    cat = category.text
                    print(cat)
                    string = re.sub('Posted in', '', cat)
                    string1 = re.sub('Tagged', ',', string)
                    string2 = re.sub('Bookmark the permalink', '', string1)
                    print(string2[:-4])
                    spamwriter.writerow([string2[:-4].strip()])


def main():
    init()
    links(soup=init())
    content()


if __name__ == "__main__":
    main()
