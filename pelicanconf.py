import os

AUTHOR = 'Bahagian Pembelajaran Digital'
SITENAME = 'e-Learning Platform Services Documentation'
SITEURL = ''

PATH = 'docs/content'
TIMEZONE = 'Asia/Kuala_Lumpur'
DEFAULT_LANG = 'en'
# Output path compatible with Read the Docs environment
OUTPUT_PATH = os.environ.get('READTHEDOCS_OUTPUT', 'output') + '/html'

DELETE_OUTPUT_DIRECTORY = True

