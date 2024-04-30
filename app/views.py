from django.shortcuts import render
from django.http import HttpResponse


VERSION = '0.0.1'
BANNER_SLANT = '''
    ____  ____  ____  ____  __    ______
   / __ )/ __ \/ __ \/ __ \/ /   / ____/
  / __  / / / / / / / / / / /   / __/   
 / /_/ / /_/ / /_/ / /_/ / /___/ /___   
/_____/\____/\____/_____/_____/_____/   
                                        
'''

# Create your views here.
def index(request): 
    # print(f'{BANNER_SLANT}\n{VERSION}\n')

    return render(request, 'app/index.html', {})
