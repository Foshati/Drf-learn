# ?  class based views  render file html in django

# from django.shortcuts import render
# from django.views import View


# class Home(View):
#     def get(self, request):
#         return render(request, "home.html")


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
#         return Response({"name": "sam-post"})
