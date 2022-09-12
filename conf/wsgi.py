"""
WSGI config for conf project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import  os 
import  sys
path  =  'C:\Users\Fabian\Desktop\modulo 2\Projeto-integrador\API-Taco\API_TACO' 
if path not in sys.path:
    sys.path.insert(0, path)
    
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')
os.environ['DJANGO_SETTINGS_MODULE'] = 'conf.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()