import os
from dotenv import load_dotenv
from dotenv import dotenv_values


load_dotenv()  # take environment variables from .env

# os.getenv('TOKEN', default='Not found')
token = os.getenv('TOKEN', 'Not found')

environs = dotenv_values('.env')

print(token)

print(environs)

config = {
    **dotenv_values('.env.dev'),
    **dotenv_values('.env.sensitive'),
    # **os.environ
}


print(config)
