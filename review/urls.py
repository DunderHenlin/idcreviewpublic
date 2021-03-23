from django.urls import path
from . import views




urlpatterns=[
    path('',views.review,name="review"),
    path('<int:review_id>/',views.detail,name="detail"),
]