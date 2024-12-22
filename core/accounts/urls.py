from django.urls import path
 

def test(reqiuest):
    print("test")

urlpatterns =[
    path("" , test)
]