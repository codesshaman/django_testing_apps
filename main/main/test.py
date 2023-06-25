import sys
sys.path.insert(0, 'apps/config_parser')
from django.shortcuts import render
from config_parser.views import config



# Create your views here.


def main():
    config_token = config('config.ini', 'token')
    return config_token


if __name__ == '__main__':
    main()
