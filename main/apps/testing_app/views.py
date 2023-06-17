from django.shortcuts import render
from main_config.views import *


# Create your views here.



def main():
    config_token = config('config.ini', 'token')
    return config_token


if __name__ == '__main__':
    main()