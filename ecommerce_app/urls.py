from django.urls import path

from .views import *

urlpatterns=[
    path('',index),
    path('navbar/',navbar),
    path('shoplogin/',shoplogin),
    path('userlogin/',userlogin),
    path('shopregister/',shopregisterview),
    path('userregister/',userregisterview),
    path('addproduct/',addproductview),
    path('viewproduct/',viewproductview),
    path('deleteproduct/<int:id>',productdeleteview),
    path('editshop/<int:id>',editshopview),
    path('editproduct/<int:id>',editproductsview),
    path('userprofile',userprofileview),
    path('viewcart/',viewcartview),
    path('addtocart/<int:id>',addtocartview),
    path('deletecart/<int:id>',deletecart),
    path('buy/<int:id>',buy),
    path('email/',email_send),
    path('success/',success),
    path('about/',about),
    path('contact/',contact),
    path('loshop/',logoutshop),
    path('louser/',logoutuser)
]