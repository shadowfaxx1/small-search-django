# Django Search Application with Trie

This project implements a Django web application that allows users to search for dishes stored in a database using a Trie data structure for efficient prefix-based searching.

## Overview

The application provides a search functionality where users can enter keywords related to dishes, and the system will suggest and display matching dishes in real-time using a Trie data structure. This approach enhances search speed and performance, especially useful for applications dealing with large datasets of items.

## Features

- **Search Functionality:** Users can enter keywords to find matching dishes stored in the database.
- **Responsive Design:** Utilizes Bootstrap and Tailwind CSS for a responsive and modern user interface.
- **Efficient Searching:** Implements Trie data structure to ensure fast and efficient prefix-based searching.

## Installation

1. Clone the repository:
   ```bash
   git clone `https://github.com/shadowfaxx1/small-search-django.git`
   cd django-trie-search-app

2. Set Vitual env:
    ``` python -m venv env
    ``` source env/bin/activate

3. Install dependencies:
    ``` pip install -r requirements.txt

4. Run Django commands in order :
    `python manage.py makemigrations`
    `python manage.py migrate`
    `python manage.py createsuperuser`

5. Start the development server:

    ```sh
    python manage.py runserver
    ```
## Usage

- Visit `http://127.0.0.1:8000/` to see the blog home page.
- Enter keywords in the search field to see real-time suggestions and search results.


## Contact

For any questions or issues, please open an issue on the repository or contact the maintainer at [mail2kaifkhan@gmail.com](mailto:mail2kaifkhan@gmail.com).
