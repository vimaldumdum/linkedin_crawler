from setuptools import setup

VERSION = "0.1"


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='last_crawler',
      version=VERSION,
      description='Selenium Scraper for Linkedin Profiles',
      long_description=readme(),
      author="Vimal Kumar",
      author_email='vimalk.03aug@gmail.com',
      packages=['scrape_linkedin'],
      zip_safe=False,
      classifiers=[
          'Development Status :: 0 - beta',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3'
      ],
      install_requires=[
          'beautifulsoup4>=4.6.0',
          'bs4',
          'selenium',
          'click',
          'joblib'
      ]
      )
