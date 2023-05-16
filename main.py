import dotenv
import os
from login import Login


if __name__ == '__main__':
    dotenv.load_dotenv()

    email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')

    login = Login(email, password)
