# CoinMarketCap Scraper API
  Welcome to the CoinMarketCap Scraper API! This project is designed to scrape data from CoinMarketCap for specified cryptocurrency coins and expose the data via a Django REST framework API. The API utilizes Celery for asynchronous task management and Selenium for web scraping.

# Table of Contents
  1.Overview
  2.Features
  3.Libraries Used
  4.Endpoints
  6.Usage
  7.Screenshots


# Overview
  This project is part of an assignment to create a Django REST framework API that scrapes cryptocurrency data from CoinMarketCap. The API accepts a list of crypto coin acronyms, scrapes the relevant data, and returns it in JSON format.

Features
1.Asynchronous scraping tasks using Celery.
2.Scrapes detailed data for each cryptocurrency coin.
3.Exposes two API endpoints for starting a scrape task and checking the status of the task.
4.Object-oriented design with a dedicated class for CoinMarketCap scraping logic.

# Libraries Used
1.Django
2.Django REST Framework
3.Celery
4.Requests
5.Selenium

# Endpoints
1. Start Scraping
  Endpoint: /api/taskmanager/start_scraping
  Method: POST
  Description: Accepts a list of crypto coin acronyms, starts scraping tasks for each, and returns a job ID.

<img width="959" alt="api_taskmanager_start_scarpping" src="https://github.com/Pankajs53/CoinMarketCapScraperAPI/assets/105196369/1e6d41c7-a770-4b3b-818e-0ff0d93a226f">

2. Check Scraping Status
Endpoint: /api/taskmanager/scraping_status/<job_id>
Method: GET
Description: Returns the current status and data for the specified job ID.
<img width="959" alt="api_taskmanager_scrapping_task" src="https://github.com/Pankajs53/CoinMarketCapScraperAPI/assets/105196369/2442adf9-f8d7-4bf6-a6ff-1839f57a243f">


# CELERY TASK ADMIN PANEL
<img width="953" alt="celery_task_adminpanel" src="https://github.com/Pankajs53/CoinMarketCapScraperAPI/assets/105196369/ea7a3a33-4c8b-455d-a2e7-de7aa6eef62e">


# Note on Data Storage
Instead of creating Django models to store the scraped data, this project stores the data in an Excel file. When the second API (/api/taskmanager/scraping_status/<job_id>) is hit, the scraped data is processed and saved to an Excel file. This approach simplifies data handling and storage for this assignment.[scraped_data.xlsx](https://github.com/user-attachments/files/15747380/scraped_data.xlsx)
