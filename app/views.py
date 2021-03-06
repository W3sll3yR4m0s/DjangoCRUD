from django.shortcuts import render, redirect
from app.forms import CarrosForm
from app.models import Carros
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    data = {}
    #data['db'] = Carros.objects.all()
    #all = Carros.objects.all() - [ Warning: A paginação pode gerar resultados inconsistentes com uma object_list não ordenada. ]
    
    def search():
        search = request.GET.get('search')
        if search:
            data['db'] = Carros.objects.filter(Modelo__icontains=search)
        else:
            #data['db'] = Carros.objects.all()
            #data['db'] = Carros.objects.get_queryset().order_by('id')
            data['db'] = paginator.get_page(pages)
    
    all = Carros.objects.get_queryset().order_by('id')
    paginator = Paginator(all, 4)
    pages = request.GET.get('page')
    data['db'] = paginator.get_page(pages)
    
    search()
    
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = CarrosForm()
    return render(request, 'form.html', data)

def create(request):
    form = CarrosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    data['form'] = CarrosForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    form = CarrosForm(request.POST or None, instance=data['db'])
    if form.is_valid:
        form.save()
        return redirect('home')

def delete(request, pk):
    db = Carros.objects.get(pk=pk)
    db.delete()
    return redirect('home')
