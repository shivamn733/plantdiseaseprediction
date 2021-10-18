from django.contrib import admin
from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index, name='home'),
    path('index',views.index, name='home' ),
    path('ulogin',views.ulogin, name='ulogin' ),
    path('ulogout',views.ulogout, name='ulogout' ),
    path('reg',views.reg, name='reg' ),
    path('suc',views.suc, name='suc' ),
    path('tokens',views.tokens, name='tokens'),
    path('verify/<authtoken>',views.verify, name='verify'),
    path("upload",views.upl,name='up')
    #path("upload",views.upl,name='up')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    

   

