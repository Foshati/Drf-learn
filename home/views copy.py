# ?  class based views  render file html in django

# from django.shortcuts import render
# from django.views import View


# class Home(View):
#     def get(self, request):
#         return render(request, "home.html")

#####* response in drf *#####
# ? function based views drf
# from rest_framework.decorators import api_view
# from rest_framework.response import Response


# @api_view(["GET"])
# def Home(request):
#     return Response({"name": "sam-get"})


# ?  class based views drf
# from rest_framework.views import APIView
# from rest_framework.response import Response


# class Home(APIView):
#     def get(self, request):
#         return Response({"name": "sam"})

#####* Request in drf *#####
# ?  class based views drf get argument in request
# from rest_framework.views import APIView
# from rest_framework.response import Response


# class Home(APIView):
#     def get(self, request, name):
#         return Response({"name": f"{name}-get"})

#! test url-get: http://127.0.0.1:8000/sara


# ?  class based views drf get .query_params in request
# from rest_framework.views import APIView
# from rest_framework.response import Response


# class Home(APIView):
#     def get(self, request):
#         name = request.query_params["name"]
#         return Response({"name": f"{name}-get"})


#! test url-get: http://127.0.0.1:8000/?name=bob


# ?  class based views drf post .data in request
from rest_framework.views import APIView
from rest_framework.response import Response


class Home(APIView):
    def get(self, request):
        return Response({"name": "sam"})

    def post(self, request):
        name = request.data["name"]
        return Response({"name": name})


#! test url-post: http://127.0.0.1:8000/
#! json: {"name": "sara" }
