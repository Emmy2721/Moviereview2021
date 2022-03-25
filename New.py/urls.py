from movie.urls import path, include
from .views import index, products, productDetail

urlpatterns = [
    path('', index, name='index'),
    path('products/',products, name='products'),
    path('productDetail/<int:id>', productDetail, name='detail'),
    path('newproduct/', views.newProduct, name='newproduct'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]
]

