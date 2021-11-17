from pprint import pprint

from scraper import ProfileScraper
import sys


def scrapeProfile(li_at, url):
    with ProfileScraper(cookie=li_at) as scraper:
        profile = scraper.scrape(url=url)
        output = profile.to_dict()
        pprint(output)


if __name__ == '__main__':
    scrapeProfile(sys.argv[1], sys.argv[2])
