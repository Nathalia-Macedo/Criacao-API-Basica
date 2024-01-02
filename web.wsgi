#language:python
import sys
path = 'C:\Users\nathalia.martins\Desktop\Organização\Aprendendo\Criacao-API-Basica\app.py'
if path not in sys.path:
    sys.path.append(path)
    

from web import app as application
