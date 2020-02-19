pr0x-tube - an automated scraping and processing for tube sites
=============

pr0x-tube is an ongoing long-term project, which scrapes tube sites for its content, converts them into a JSON file and reposts them on your own Blog or CMS.
This project is only for educational purpose and was 'forked' from a very old own project, written in PHP and Javascript.
pr0x-tube will be fully written and developed in Python, using Mezzanine as CMS and an own API to handle the JSON files correctly.

# How does it work?

pr0x-tube mainly uses BeautifulSoup and requests to first load an sitemap-url, then loads all existing blog post urls into an excel file.
If pr0x-tube has a stable set of urls, it can load all urls in that excel step by step, to scrape all needed information for the upcoming JSON file.
The needed information we need are "title", "content", "categories", "media link" and "download link" (if possible).
Those information will be written in the JSON file, then the API sends it via POST-request to our CMS/Blog and creates a blog post.


