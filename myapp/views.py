# views.py
from django.http import JsonResponse
from django.shortcuts import render
import logging
logger = logging.getLogger(__name__)
# create your views here

from django.http import JsonResponse
from django.shortcuts import render
from celery.result import AsyncResult
import logging

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


logger = logging.getLogger(__name__)

from myceleryproject.celery import scrape_task


# used intially for testing 
def index(request):
    # queuing the task
    print("Result: ")
    result1 = scrape_task.delay()
    print("Result 1->",result1)
    job_id = result1.id
    print(f"Job ID: {job_id}")
    return render(request,"myapp/home.html")

def about(request):
    return render(request,'myapp/about.html')

def contact(request):
    return render(request,'myapp/contact.html')



# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# myapp/views.py
from django.http import JsonResponse
from django.views import View
from celery.result import AsyncResult
from myceleryproject.celery import scrape_task
import json
import logging
from .models import CryptoCoin,Contract,OfficialLink,Social
from .helper import create_excel_file

logger = logging.getLogger(__name__)



# The @method_decorator(csrf_exempt, name='dispatch') is used to apply the csrf_exempt decorator 
# to the dispatch method of the ScrapingView class. This means that CSRF (Cross-Site Request Forgery) 
# protection will be disabled for all requests handled by this view. This is useful when you need to 
# accept POST requests from external sources that won't have the CSRF token.
@method_decorator(csrf_exempt, name='dispatch')
class ScrapingView(View):
    # The post method is used to handle POST requests. In this context, it is used to start a scraping task.
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            urls_to_scrape = data.get('urls', [])

            job_ids = {}
            for url in urls_to_scrape:
                 # Asynchronously start a scraping task for each URL.
                response = scrape_task.delay(url)
                job_ids[url] = response.id
                logger.info(f'For URL -> {url}, job ID is -> {response.id}')

            # Return a JSON response indicating that the scraping has started.
            response_data = {
                'message': 'Scraping started successfully',
                'job_ids': job_ids
            }
            return JsonResponse(response_data)
        except json.JSONDecodeError:
            # Return an error response if the JSON payload is invalid.
            return JsonResponse({'error': 'Invalid JSON payload'}, status=400)
        except Exception as e:
            # Return a generic error response for any other exceptions.
            return JsonResponse({'error': str(e)}, status=500)


    # The get method is used to handle GET requests. In this context, it is used to check the status 
    # of a scraping task and retrieve the result if the task is successful.
    def get(self, request, *args, **kwargs):
        task_id = kwargs.get('task_id')
        if not task_id:
             # Return an error response if no task ID is provided.
            return JsonResponse({'error': 'Task ID is required'}, status=400)

        # Retrieve the task result using the task ID.
        result = AsyncResult(task_id)
        response = {'state': result.state}

        if result.successful():
            try:
               # If the task is successful, get the result, which is expected to be a dictionary.
                scraped_data = result.get()
                
                 # Call a custom function to create an Excel file from the scraped data.
                create_excel_file(scraped_data)
                print("scraped_data", scraped_data)

            except Exception as e:
                return JsonResponse({'error': 'An error occurred while processing the data: ' + str(e)}, status=500)
        else:
            
            return JsonResponse({'error': 'Task failed or not ready'}, status=400)

         # Include the scraped data in the response if everything is successful.
        response['result'] = scraped_data
        return JsonResponse(response)