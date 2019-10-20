pr0x-tube - an automated scraping and processing for tube sites
=============

pr0xTube is a long time project to scrape and process data from several tube sites
and convert them into your own blog or CMS for further actions.
pr0xTube is written from scratch and focuses on tube sites with a specific (and similiar) wordpress template/design
also the possibility to access sitemap urls.

With the access to sitemap urls, pr0xTube is able to scrape and save all urls of its target site into an excel file - line by line.
After that, it will continue to load every single url, scrapes the site for the title, description and category and creates a new excel with those informations.

With the implementation of an also from scratch written Wordpress-API (in the future), these excel files can be used to automatically create new blog posts with those informations.

The Project is currently under development and will feature a full frontend with Flask and backend support with MongoDB in the future.

# Installation

1) `git clone https://github.com/N0W3N/pr0x-tube.git /path/to/your/folder

or

1) download and unzip the package to your preferred path
2) run `pip install -r requirements.txt` inside the directory
3) edit line 9 with your own url (make sure the url matches the requirements of the code)

# Usage

`python client.py`

excel files will be created in the work directory you've 'git cloned' it before.



