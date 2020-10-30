import argparse
import getpass
import pathlib
import os

def parse_args():
    desc = "Scrape a pinterest board"
    parser = argparse.ArgumentParser(description=desc)

    parser.add_argument('--verbose', action='store_true', help='Print progress to console.')
    parser.add_argument('--email', type=str, default='user@domain.com')
    parser.add_argument('--password', type=str, default='password')
    parser.add_argument('--url', type=str, default='https://www.pinterest.com/tarotluv/tarot-cards-and-decks/')
    parser.add_argument('--output_folder', type=str, default='./output')

    args = parser.parse_args()
    return args

def main():
    global args
    args = parse_args()
    from pinterest_scraper import scraper as s
    from selenium import webdriver

    if args.email == 'user@domain.com':
        args.email = input('email: ')

    if args.password == 'password':
        args.password = getpass.getpass('password: ')


    print('launching chrome...')
    chrome = webdriver.Chrome()

    print('logging into pinterest as ' + args.email)
    ph = s.Pinterest_Helper(args.email, args.password, chrome)

    print('scraping images from ' + args.url)
    images = ph.runme(args.url)

    print('saving images...')
    pathlib.Path(args.output_folder).mkdir(parents=True, exist_ok=True)
    s.download(images, args.output_folder)

if __name__ == "__main__":
    main()