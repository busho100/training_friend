from django.shortcuts import render,redirect
from .models import Friend
from django.shortcuts import render
from .forms import HelloForm
from django.http import HttpResponse

# Create your views here.
def index(request):
    data = Friend.objects.all()
    context ={
        'title':'Hello Friend',
        'massage':'all friends',
        'data': data,
    }
    return render(request, 'friends/index.html', context)

    '''
     if (request.method == 'POST'):
        num = request.POST['id']
        item = Friend.objects.get(id=num)
        context['data'] = [item]
        context['form'] = HelloForm(request.POST)
    else:
        context['data'] = Friend.objects.all() 

    return render(request, 'friends/index.html', context)

    def create(request):
        context = {
           'title':'Hello Friend',
            'form':HelloForm()
        }

        if(request.method =='POST'):
            name = request.POST['name']
            mail = request.POST['mail']
            male = 'male' in request.POST
            age = request.POST['age']
            birth = request.POST['birthday']

            friend = Friend(name=name,mail=mail,male=male,age=age,birthday=birth)
            friend.save()
            return redirect(to='/friends')
        return render(request, 'friends/index.html', context)
'''