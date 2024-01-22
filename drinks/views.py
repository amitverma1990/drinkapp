from django.http import JsonResponse
from .modals import Drink
from .serilizer import Drinkserilizer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from drinks import serilizer

@api_view(['GET','POST'])
def drink_list(request, format=None):
    # get all the drinks
    # serilized them
    # retun JSON
    
    if request.method=='GET':
        drink = Drink.objects.all()
        serilizer = Drinkserilizer(drink, many = True)
        return Response(serilizer.data)
        #return JsonResponse({'drinks':serilizer.data}, safe=False)
    
    if request.method == 'POST':
        serilizer = Drinkserilizer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status=status.HTTP_201_CREATED)
        
        
@api_view(['GET','PUT','DELETE'])
def drink_details(request, id,format=None):
    try:
      drink =  Drink.objects.get(pk =id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
        
    if request.method == 'GET':
        serilizer = Drinkserilizer(drink)
        return Response(serilizer.data)
    elif request.method =='PUT':
        serilizer = Drinkserilizer(drink,data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data)
        return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method =='DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)