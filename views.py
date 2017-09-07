from django.http import HttpResponse

def index(request,album_id=34):
    return HttpResponse("<h1> This is the list of the albums {0} {1} {0} {2}".format(album_id,"this is 1","this is 2"))

def detail(request, album_id):
    return HttpResponse("<h2>Details for Album id:" + str(album_id) + "</h2>")
