import dotenv
import os
from helpers.search_products import SearchProducts


if __name__ == '__main__':
    dotenv.load_dotenv()
    email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')
    login = SearchProducts(email, password)
