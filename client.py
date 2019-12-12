import csv
import re
import requests
from bs4 import BeautifulSoup as bs
import sys
# from parser import


def init():
    """ initialization of the main scraper
    to collect information, create and return the soup.
     """

    try:
        r = requests.get('http://www.localhost.com/post-sitemap41.xml')
    except requests.ConnectionError as ConnectionError:
        print("Failed to establish a new connection")
        print(ConnectionError)
        sys.exit()
    except requests.Timeout as TimeoutError:
        print("Site isn't responding yet. Either it's down for maintenance or Cloudflare is up.")
        print(TimeoutError)
        sys.exit()
    else:
        mainSoup = bs(r.text, 'html.parser')
        return mainSoup


def links(mainSoup):
    """parsing function to collect all existing links of the sitemap url.
    These links will be saved in one single csv file for further actions."""

    with open('/Users/test/pr0x-tube/urls/urls.csv', 'a+', newline='') as csvfile:
        for url in mainSoup.find_all('loc'):
            url_writer = csv.writer(csvfile, delimiter=' ')
            url_list = url.text.strip('|')
            url_writer.writerow([url_list])
            print(url_list)
    csvfile.close()


def content():
    """Main function to scrape and collect all required information of all posts on the site.
     It reads the urls-file, loads each of the posts one by one, scrapes them for title, content, categories, thumbnail
     and video link - if available.
     The function creates for each loaded link a new csv file and writes those information down."""

    file_number = 0
    with open('/Users/test/pr0x-tube/urls/urls.csv', 'r') as file:
        url_reader = csv.reader(file)
        for url_row in url_reader:
            post_link = ''.join(url_row)
            file_number += 1

            try:
                link_row = requests.get(post_link)
            except requests.ConnectionError as ConnectionError:
                print("Failed to establish a new connection.")
                print(ConnectionError)
                sys.exit()
            except requests.Timeout as TimeoutError:
                print("Site isn't responding yet. Either it's down for maintenance or Cloudflare is up.")
                print(TimeoutError)
                sys.exit()
            else:
                url_soup = bs(link_row.text, 'html.parser')

            with open('test%s.csv' % file_number, 'w+', newline='') as info_writer:
                info_writer = csv.writer(info_writer, delimiter=' ')
                for title_post in url_soup.find('h1', class_='entry-title'):
                    info_writer.writerow(([title_post.strip()]))
                    print(title_post)

                for description in url_soup.find_all('div', class_='entry-content post_content'):
                    content1 = description.text
                    info_writer.writerow([content1.strip()])
                    print(content)

                for category in url_soup.find_all('footer', {"class": "entry-meta"}):
                    cat = category.text
                    print(cat)
                    string = re.sub('Posted in', '', cat)
                    string1 = re.sub('Tagged', ',', string)
                    string2 = re.sub('Bookmark the permalink', '', string1)
                    print(string2[:-4])
                    info_writer.writerow([string2[:-4].strip()])

                for image_link in url_soup.select('.aligncenter'):
                    url = image_link['src']
                    print(url)
                    info_writer.writerow([url])

                for stream_link in url_soup.find_all('iframe'):
                    frame = stream_link['src']
                    print(stream_link)
                    info_writer.writerow([frame])


def main():
    init()
    links(mainSoup=init())
    content()


if __name__ == "__main__":
    main()
