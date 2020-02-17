from django.shortcuts import render, redirect
from .models import sports,match,readmore
from django.contrib.auth.models import auth, User
from django.contrib import messages
from django.db.models import Q
from project2.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

from django.http import HttpResponse

firstmatch = sports()
firstmatch.date = '1/12/1997'
firstmatch.head = 'it was a good match'
firstmatch.sub = 'fgfhagsa gfjhadvafgjshdfvns hhsgdfjbsvdcnggs sggdfnbdfsd nsgdf usgf hgfjfhsvjff'

secondmatch = sports()
secondmatch.date = '12 12 12'
secondmatch.head = 'amazing match'
secondmatch.sub = 'super kaliyaan mwone'
secondmatch.img = 'peace.jpg'

thirdmatch = sports()
thirdmatch.date = '10 10 10'
thirdmatch.head = 'shimmi hero aada hero'
thirdmatch.sub = 'mwone ath lockaa ing por'
thirdmatch.img = 'psyco.jpeg'

fourmatch = sports()
fourmatch.date = '12 12 1998'
fourmatch.head = 'vamban game'
fourmatch.sub = 'walare migacha onn'
fourmatch.img = 'messi.jpg'
fourmatch.img = 'ronu.jpg'
fourmatch.img = 'vijay.jpg'

lis = [firstmatch, secondmatch, thirdmatch, fourmatch]


def sportss(request):
    m=match.objects.all()
    return render(request, 'index.html', {'fm': firstmatch, 'sm': secondmatch, 'tm': thirdmatch,match:"m"})




def loop(request):
    return render(request, 'forloop.html', {'f': lis})


def jaya(request):
    if request.method == 'POST':
        a = request.POST['name']
        b = request.POST['password']
        user = auth.authenticate(username=a, password=b)
        if user is not None:
            auth.login(request, user)
            return redirect('sports:home')
        else:
            messages.error(request, "invalid username/password")

    return render(request, 'login.html')

def out(request):
    auth.logout(request)
    return redirect('sports:home')


def reg(request):

    if request.method == 'POST':
        c = request.POST['fullname']
        d = request.POST['youremail']
        e = request.POST['password']
        f = request.POST['confirm-password']
        g = request.POST['firstname']
        h = request.POST['lastname']
        print(c,d,g,h)
        if (e == f):

            if (User.objects.filter(username=c).exists()):
                messages.error(request, "username already exist")
                return redirect('sports:register-page')
            elif (User.objects.filter(email=d).exists()):
                messages.error(request, "email already exist")
                return redirect('sports:register-page')
            else:
                z = User.objects.create_user(username=c, email=d, password=e, first_name=g, last_name=h)
                z.save()
                return render(request, 'register.html')

        else:
            messages.error(request, "password doesn't match")
            return redirect('sports:register-page')
    return render(request, 'register.html')

def blog (request):
    ad = readmore.objects.order_by('-date')[0:1]
    bd = readmore.objects.order_by('date')[1:]
    return render(request, 'Blog.html', {'ad': ad, 'bd': bd})

def about (request):
    return render(request, 'about.html')

def team (request):
    return render(request, 'team.html')

def news (request):
    return render(request, 'news.html')

def contact (request):
    subject='melcow to the world of sports'
    message='Sport includes all forms of competitive physical activity or games which,[1] through casual or organised participation, at least in part aim to use, maintain or improve physical ability and skills while providing enjoyment to participants, and in some cases, entertainment for spectators.[2] Hundreds of sports exist, from those between single contestants, through to those with hundreds of simultaneous participants, either in teams or competing as individuals. In certain sports such as racing, many contestants may compete, simultaneously or consecutively, with one winner; in others, the contest (a match) is between two sides, each attempting to exceed the other. Some sports allow a "tie" or "draw", in which there is no single winner; others provide tie-breaking methods to ensure one winner and one loser. A number of contests may be arranged in a tournament producing a champion. Many sports leagues make an annual champion by arranging games in a regular sports season, followed in some cases by playoffs.'
    recipent=request.GET.get('email_id')
    send_mail(subject,message,EMAIL_HOST_USER,[recipent], fail_silently=False)
    return render(request, 'contact.html',{'f':recipent})

def search (request):
    a=request.GET.get('f', None)
    results=sports.objects.filter(Q(head__icontains=a) | Q(sub__icontains=a))
    result=match.objects.filter(Q(team1__icontains=a) | Q(team2__icontains=a))
    return render(request, 'searchresult.html', {'search1':results,'search': result})

def read (request):
     return render(request,'single-blog.html')