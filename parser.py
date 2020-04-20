from bs4 import BeautifulSoup as bs
import re
import requests
import sys
import csv


def init():
    """
    initialization of the main scraper
    to collect information, create and return the soup.
    """
    try:
        r = requests.get('http://localhost/post-sitemap44.xml')
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
    These links will be saved into one single csv file for further actions."""
    try:
        with open('/Users/test/pr0x-tube/urls/urls.csv', 'a+', newline='') as c:
            for url in mainSoup.find_all('loc'):
                url_writer = csv.writer(c, delimiter=' ')
                url_list = url.text.strip('|')
                url_writer.writerow([url_list])
                print(url_list)
    except IOError:
        print('URLs are not available. The script needs to be executed again or the current file can not be accessed.')
        sys.exit()


def content():
    """
    Main function to scrape and collect all required information of all posts on the site.
     It reads the urls-file, loads each of the posts one by one, scrapes them for title, content, categories, thumbnail
     and video link - if available.
     The function creates for each loaded link a new csv file and writes those information down.
     """

    file_number = 0
    with open('/Users/test/pr0x-tube/urls/urls.csv', 'r') as file:
        url_reader = csv.reader(file)
        for url_row in url_reader:
            post_link = ''.join(url_row)
            file_number += 1

            """ 
            As we create a new requests for each link, we also have to check, if the site is up or down.
            This part of the code will probably be rewritten into a class, since it has been already used for
            the sitemap function.
            """
            try:
                link_row = requests.get(post_link)
            except requests.ConnectionError as ConnectionError:
                print("Failed to establish a new connection.")
                print(ConnectionError)
            except requests.Timeout as TimeoutError:
                print("Site isn't responding yet. Either it's down for maintenance or Cloudflare is up.")
                print(TimeoutError)
            else:
                url_soup = bs(link_row.text, 'html.parser')

                with open('test%s.csv' % file_number, 'w+', newline='') as c:
                    title = url_soup.find('h1', class_='entry-title').text
                    description = url_soup.find('div', class_='entry-content post_content').text
                    category = url_soup.find('footer', {"class": "entry-meta"})

                    # using for loops here since there are possibly more than one links available

                    for image_link in url_soup.select('.aligncenter'):
                        img_link = image_link
                        # img_link = image_link['src']
                    go_link = url_soup.select(
                            '.entry-content > p:nth-child(3) > strong:nth-child(1) > span:nth-child(1) > span:nth-child(1) > a:nth-child(2)')
                    for dl_link in go_link:
                        link = dl_link['href']
                    cat_temp = re.sub('Posted in', '', category.text)
                    cat_temp1 = re.sub('Tagged', '', cat_temp)
                    categories = re.sub('Bookmark the permalink', '', cat_temp1)

                    info_writer = csv.writer(c, delimiter=' ')
                    info_writer.writerow(([title]))
                    info_writer.writerow(([description]))
                    info_writer.writerow(([categories]))
                    info_writer.writerow(([img_link]))
                    info_writer.writerow(([link]))


def main():
    links(mainSoup=init())
    content()


if __name__ == "__main__":
    main()
