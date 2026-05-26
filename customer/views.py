from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
from customer.models import Movie
from customer.form import MovieForm

def customer_dashboard(request):
    beta_data= Movie.objects.all()
    return render (request,'customer.html', context={'data_shows':beta_data})

# Create your views here



def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            Movie=form.save()
            return redirect('add_movie') 
        else:
            return render(request, 'movie/add_movie.html', context={"form":form})
    else:
        form=MovieForm()
    return render(request, 'movie/add_movie.html', context={'form': form})

# def update_movie(request, id):
#    if request.method == 'GET':
#       movie_info = Movie.objects.get(id=id)
#       new_form = MovieForm(instance=movie_info)
#       return render(request, 'movie/update_movie.html', context={'form':new_form, 'id':id})
#    if request.method == 'POST':
#         get_info = Movie.objects.get(id=id)
#         update_form_movie = MovieForm(request.POST, instance=get_info)
#         if update_form_movie.is_valid():
#             update_form_movie.save()
#             return redirect('display_movie')
#         else:
#             return HttpResponse('Invalid user information')    




def update_movie(request, id):
    movie_info = get_object_or_404(Movie, id=id)
    
    if request.method == 'GET':
        new_form = MovieForm(instance=movie_info)
        return render(request, 'movie/update_movie.html', context={'form': new_form, 'id': id})

    elif request.method == 'POST':
        update_form_movie = MovieForm(request.POST, request.FILES, instance=movie_info)  # <-- Add request.FILES here
        if update_form_movie.is_valid():
            update_form_movie.save()
            return redirect('display_movie')
        else:
            # Instead of HttpResponse, re-render the form with errors
            return render(request, 'movie/update_movie.html', context={'form': update_form_movie, 'id': id})

    # For any other HTTP method, return 405 Method Not Allowed or redirect
    return HttpResponse(status=405)










def display_movie(request):
    data_fetch = Movie.objects.all()
    return render(request,'movie/display.html', context={'send_data' :data_fetch})

def view_movie(request,id):
    data_get = Movie.objects.get(id=id)
    return render(request,'movie/view_movie.html', context={'dp_data':data_get}) 

def delete_movie(request,id):
    movie_info_delete = Movie.objects.get(id=id)
    movie_info_delete.delete()
    return redirect('display_movie')    




