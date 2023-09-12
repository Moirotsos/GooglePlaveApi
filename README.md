# Google Place API

Google Place API is a simple Django project that allows users to retrieve information about a place of their choice. Additionally, it provides the functionality to save information about each place and add descriptions.

## Project Overview

Google Place API is designed to provide users with easy access to place information. Users can search for a place and view details about it. They also have the ability to save information about places they find interesting and add descriptions to them.

## Getting Started

Follow these steps to set up and run Google Place API on your local machine.

### Prerequisites

Before you begin, ensure you have the following prerequisites installed:

1. **Python 3.10 or higher**: You need to have Python 3.10 or a higher version installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

2. **Google Maps API Key**: Obtain a Google Maps API key by visiting the [Google Cloud Console](https://console.cloud.google.com/).

3. **Django**: Make sure you have Django installed. If not, you can install it using pip:
   ```bash
   pip install Django
   
### Installation

- **Git**: If you don't have Git installed, you can download and install it from [Git's official website](https://git-scm.com/downloads). You will need Git to clone the project repository:

   ```bash
   git clone https://github.com/Moirotsos/googlePlaceApi.git
   
- **Virtual Environment**: It's a good practice to create a virtual environment to manage your project's dependencies. You can install virtualenv using pip:
  ```bash
  pip install virtualenv
  
- **Django Rest Framework**: Install Django Rest Framework:
   ```bash
    pip install djangorestframework

- **Requests Library**: Install the Requests library:
    ```bash
    pip install requests

- **Django Redis**: Install Django Redis:
    ```bash
    pip install django-redis

- **Google Maps Python Client Library**: Install the Google Maps Python Client Library:
    ```bash
    pip install -U googlemaps
### Configuration

In the project's settings, configure the Google Maps API key for the application to access Google Place API services. You can do this by adding your API key to the settings file.
    ```bash
    # settings.py  
    GOOGLE_KEY = 'YOUR_GOOGLE_API_KEY'



## Usage

This Django project provides three endpoints for interacting with place information:

###$ 1. Retrieve Place Information

Endpoint: `http://localhost:8000/places/?query=`
- To retrieve information about a place, make a GET request to this endpoint.
- Include the `query` parameter in the URL with the name of the place you want to retrieve information for.
- Example usage:
  
   GET `http://localhost:8000/places/?query=YourPlaceName`

#### 2. Save a Place

Endpoint: `http://localhost:8000/save_place/`

- To save a place, make a POST request to this endpoint.
- Pass a JSON object in the request body with the place information you want to save.
- Ensure that the place_id is included in the JSON, as it is considered independent.

#### 3. Add a Description to a Saved Place

Endpoint: http://localhost:8000/description_place/<str:place_id>/

- To add a description to a saved place, make a POST request to this endpoint.
- Include the place_id as part of the URL path.
- Pass a JSON object in the request body with the description you want to add.

# Authors     
- @[Moirotsos](https://github.com/Moirotsos/googlePlaceApi)
  
