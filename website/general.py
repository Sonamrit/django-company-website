from .models import *

def global_data(request):
    data ={
        'settingData':Setting.objects.first(),
        'menuserviceData':Service.objects.all(),
    }
    return data