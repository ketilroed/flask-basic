import sys
import logging
logging.basicConfig(stream=sys.stderr)

sys.path.insert(0, '/var/www/ketilroed.no/public_html/flask-basic/')
from app import app as application


