from django.urls import path

import mainapp.views as mainapp


app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.products, name='index'),
    path('<int:pk>/', mainapp.products, name='category'),
    path('<int:pk>/page/<int:page>/', mainapp.products, name='page'),
    path('productdetail/<int:id>/', mainapp.productdetail, name='productdetail')
]