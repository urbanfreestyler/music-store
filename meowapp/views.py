from django.conf.global_settings import EMAIL_HOST_USER
from django.shortcuts import render
from django.core.paginator import Paginator
# Create your views here.
from django import contrib
from django.shortcuts import render, redirect
from .models import *
from .forms import ContactForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.conf import settings

from django.http import HttpResponse, JsonResponse, response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import status
from rest_framework.decorators import api_view


from .serializers import BeatSerializer, RegistrationSerializer

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your views here.


#home page
def home(request):
    beats = Beat.objects.all()
    keys = Key.objects.all()
    genres = Genre.objects.all()

    paginator= Paginator(Beat.objects.all(),1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={"page_obj":page_obj}



    if request.method == "POST" and request.POST.get('key_id'):
        beats = Beat.objects.filter(key=request.POST.get('key_id'))
        if request.method == "POST" and request.POST.get('genre_id'):
            beats = beats.filter(genre=request.POST.get('genre_id'))
    elif request.method == "POST" and request.POST.get('selected1'):
        if request.method == "POST" and request.POST('genre_id'):
            beats = Beat.objects.filter(genre=request.POST.get('genre_id'))
    elif request.method == "POST" and request.POST.get('genre_id'):
        beats = Beat.objects.filter(genre=request.POST.get('genre_id'))
    else:
        beats = Beat.objects.all()
    

    context = {'beats':beats,
            'keys': keys,
            'genres':genres,
            'page_obj':page_obj}

    return render(request, 'meowapp/index.html', context)


# Checkout
@login_required(login_url='login')
def checkout(request, id):
    beat = Beat.objects.get(id=id)
    context = {'beat': beat}
    return render(request, 'meowapp/checkout.html', context)



@login_required(login_url='login')
def delivery(request, id):
    beat = Beat.objects.get(id=id)
    context = {'beat':beat}

    return render(request, 'meowapp/delivery.html', context)

# delivery to customer's email
def send_mail(request, id):
    beat = Beat.objects.get(id=id)
    file = beat.untagged_audio
    to_mail = request.POST.get('to_email')
        
    message = """Hey! 
Thanks for purchasing!. Don't forget to tag me on Instagram, when uploading your track ;) (@meow_onthebeat).
Enjoy ;)"""
    subject = "Meow Beats"
    email = EmailMessage(subject, message, EMAIL_HOST_USER, [to_mail])
    email.attach(file.name, file.read(), 'audio/mp3')
    email.send()

    return redirect('home')
    return messages.success(request, "Sent successfully to " + to_mail)
    


#feedback

def contact_us(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        print(form)
    context = {'form':form}
    return render(request, 'meowapp/index.html', context)




#sign up, log in, log out


@api_view(['POST',])
def registerPage(request):
    if request.method == "POST":
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid:
            account = serializer.save()
            data['response'] = "Successfully registered a new user."
            data['email'] = account.email
            data['username'] = account.username
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
        return response(data)


@receiver(post_save, sender = settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


def registration(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'meowapp/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'username or password is incorrect')

        context = {}
        return render(request, 'meowapp/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')


""" 

            API SECTION 

"""

@api_view(['GET', 'POST', 'DELETE'])
def beat_list(request):
    if request.method == 'GET':
        beats = Beat.objects.all()

        beats_serializer = BeatSerializer(beats, many=True)
        return JsonResponse(beats_serializer.data, safe=False)

    elif request.method == 'POST':
        beat_data = JSONParser().parse(request)
        beat_serializer = BeatSerializer(data=beat_data)
        if beat_serializer.is_valid():
            beat_serializer.save()
            return JsonResponse(beat_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(beat_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Beat.objects.all().delete()
        return JsonResponse({'message': '{} Beats were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def beat_detail(request, pk):
    try: 
        beat = Beat.objects.get(pk=pk) 
    except Beat.DoesNotExist: 
        return JsonResponse({'message': 'This beat does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        beat_serializer = BeatSerializer(beat) 
        return JsonResponse(beat_serializer.data) 
 
    elif request.method == 'PUT': 
        beat_data = JSONParser().parse(request) 
        beat_serializer = BeatSerializer(beat, data=beat_data) 
        if beat_serializer.is_valid(): 
            beat_serializer.save() 
            return JsonResponse(beat_serializer.data) 
        return JsonResponse(beat_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        beat.delete() 
        return JsonResponse({'message': 'Beat was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
