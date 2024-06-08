import os
from celery import Celery,shared_task
from .CoinMarketCap import CoinMarketCap
import logging

logger = logging.getLogger(__name__)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myceleryproject.settings')

app = Celery('myceleryproject')

# Corrected this line to use 'django.conf' instead of 'django.config'
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load the task module
app.autodiscover_tasks()

# Define the task with a unique name, e.g., 'scrape_task'

@shared_task
def scrape_task(coin_name):
    scraper = CoinMarketCap(coin_name)
    return scraper.scrape_data()

# def scrape_task(self, coin_name):
#     try:
#         service = ScraperService(coin_name)
#         result = service.scrape_data()
#         return result
#     except Exception as e:
#         self.retry(exc=e, countdown=60)