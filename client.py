import csv
import re

import requests
from bs4 import BeautifulSoup as bs


# initialize parser and soup


def init():
    r = requests.get('localhost/post-sitemap34.xml')  # replace the url with another one
    soup = bs(r.text, 'html.parser')

    return soup


# scrape all existing of the sitemap and save them in an excel file


def links(soup):
    with open('urls.csv', 'a+', newline='') as csvfile:
        for link in soup.find_all('loc'):
            urlwriter = csv.writer(csvfile, delimiter=' ')
            link1 = link.text.strip('|')
            urlwriter.writerow([link1])
            print(link1)
    csvfile.close()


# open all links in urls.csv, scrape them for all needed informations and save them in a new excel file.
# also iterate the filename of the excel file starting with each new url


def content():

    i = 0
    with open('urls.csv', 'r') as file:
        urlreader = csv.reader(file)
        for row in urlreader:
            link1 = ''.join(row)
            i += 1

            a = requests.get(link1)
            soup1 = bs(a.text, 'html.parser')

            with open('test%s.csv' % i, 'w+', newline='') as con:
                spamwriter = csv.writer(con, delimiter=' ')
                for links in soup1.find('h1', class_='entry-title'):
                    spamwriter.writerow(([links.strip()]))
                    print(links)

                for description in soup1.find_all('div', class_ = 'entry-content post_content'):
                    content1 = description.text
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
