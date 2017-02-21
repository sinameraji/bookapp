from django.shortcuts import render
from .models import Book
from django.utils import timezone

# Create your views here.

def book_list(request):
    books = Book.objects.filter(readDate__lte=timezone.now()).order_by('readDate')
    return render(request, 'bookWorm/book_list.html', {'books': books})


#def upload_pic(request):
#    if request.method == 'POST':
#        form = ImageUploadForm(request.POST, request.FILES)
#        if form.is_valid():
#            m = ExampleModel.objects.get(pk=course_id)
#            m.model_pic = form.cleaned_data['image']
#            m.save()
#            return HttpResponse('image upload success')
#    return HttpResponseForbidden('allowed only via POST')