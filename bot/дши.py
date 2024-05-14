import subprocess
import sys

# Установка pip
subprocess.check_call([sys.executable, '-m', 'ensurepip'])

# Установка библиотек
libraries = ['requests', 'datetime', 'telebot', 'google-auth', 'google-auth-oauthlib', 'google-auth-httplib2', 'google-api-python-client']
for lib in libraries:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', lib])