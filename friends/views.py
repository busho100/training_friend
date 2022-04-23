from django.shortcuts import render,redirect
from .models import Friend
from .forms import HelloForm, FriendForm
from django.http import HttpResponse

# Create your views here.
def index(request):
    data = Friend.objects.all()
    context ={
        'title':'Hello Friend',
        'data': data,
    }
    return render(request, 'friends/index.html', context)
    
    ''' if (request.method == 'POST'):#もし、リクエストがPOSTであれば、以下の処理をせよ！
        num = request.POST['id']#入力されたidナンバーをnumに代入せよ！
        item = Friend.objects.get(id=num)#numに代入されたrequest.POST['id']を　idとして、データを取得せよ！
        context['data'] = [item] #取得したデータ（item）で、'data'を上書きせよ！
        context['form'] = HelloForm(request.POST)
    else:
        context['data'] = Friend.objects.all() 
    
    return render(request, 'friends/index.html', context) '''
    
def create(request):

    if(request.method =='POST'):
        obj = Friend()
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/friends')
    
    context = {
        'title':'Hello Friend',
        'form':FriendForm(),
    }
    return render(request, 'friends/create.html', context)
