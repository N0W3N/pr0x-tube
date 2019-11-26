import csv
import re
import requests
from bs4 import BeautifulSoup as bs
#import sys
#from parser import


def init():

    """ initialization of the main scraper
    to collect information, create and return the soup.
     """

    r = requests.get('http://www.localhost.com/post-sitemap41.xml')
    soup = bs(r.text, 'html.parser')
    return soup


def links(soup):

    """parsing function to collect all existing links of the sitemap url.
    These links will be saved in one single csv file for further actions."""

    with open('urls.csv', 'a+', newline='') as csvfile:
        for link in soup.find_all('loc'):
            urlwriter = csv.writer(csvfile, delimiter=' ')
            link1 = link.text.strip('|')
            urlwriter.writerow([link1])
            print(link1)
    csvfile.close()


def content():

    """Main function to scrape and collect all required information of all posts on the site.
     It reads the urls-file, loads each of the posts one by one, scrapes them for title, content, categories, thumbnail
     and video link - if available.
     The function creates for each loaded link a new csv file and writes those information down."""

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

                for image_link in soup1.select('.aligncenter'):
                    url = image_link['src']
                    print(url)
                    spamwriter.writerow([url])

                for stream_link in soup1.find_all('iframe'):
                    frame = stream_link['src']
                    print(stream_link)
                    spamwriter.writerow([frame])


def main():
    init()
    links(soup=init())
    content()


if __name__ == "__main__":
    main()
