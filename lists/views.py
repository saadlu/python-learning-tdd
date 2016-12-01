from django.shortcuts import redirect, render
from django.http import HttpResponse
from lists.models import Item

# Create your views here.
def home_page(request):
    if(request.method == 'POST'):
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/the-only-list-in-the-world/')
    else:
        return render(request, 'home.html')
    pass

def view_list(request):
    return render(request, 'list.html', {'items':Item.objects.all})
