from django.urls import path
from.views import HtmlView,XalView,ExcelView
urlpatterns =[
    path('html',HtmlView.as_view()),
    path('xml',XalView.as_view()),
    path('excel',ExcelView.as_view()),
]
