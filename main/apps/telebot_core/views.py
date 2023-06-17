from django.shortcuts import render
from main_config.views import config

# Create your views here.
file_path = '/path/to/config.ini'
section_name = 'my_section'
result = config(file_path, section_name)
print(result)