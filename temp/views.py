from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse_lazy
from .models import Complaint
from rest_framework import status
from django.contrib.auth.decorators import user_passes_test
from django.forms import model_to_dict
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from django.http import FileResponse, HttpResponse
from django.shortcuts import get_object_or_404
from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializers
from .forms import FileUploadForm, QR_code_mainly
import os
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import (ListView,
                                  TemplateView,
                                  DetailView,
                                  UpdateView,
                                  DeleteView,
                                  )
from .models import (Books,
                    AboutPage,
                    QrCode,
                    )
from django.db.models import Q
from django.core.files.storage import FileSystemStorage


class AllBooks(ListView):
    model = Books
    template_name = 'all_books.html'
    context_object_name = 'temp'

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('queryset')
        
        if q:
            sat_q = Q(title__icontains=q) | Q(price__icontains=q)
            queryset = queryset.filter(sat_q)
        return queryset


class HomePageView(ListView):
    model = Books
    template_name = 'home.html'
    context_object_name = 'clay'

    def get_queryset(self):
        queryset = super().get_queryset()
        if 'queryset' in self.request.GET:
            q = self.request.GET['queryset']
            sat_q = Q(Q(title__icontains=q) | Q(price__icontains=q))
            queryset = queryset.filter(sat_q)
        return queryset


def item_detail(request, item_id):
    item = get_object_or_404(Books, pk=item_id)
    item.number_of_views += 1
    item.save()
    return HttpResponse(request, f'Item ID: {item_id}, Views: {item.number_of_views}')


class BooksDetailView(DetailView):
    model = Books  

    def get(self, request, pk):
        context = {}

        context['task'] = Books.objects.filter(id=pk)
        return render(request, 'books_detail.html', context)

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('queryset')
        
        if q:
            sat_q = Q(title__icontains=q) | Q(price__icontains=q)
            queryset = queryset.filter(sat_q)
        return queryset


class BookUpdateView(UpdateView):
    model = Books
    template_name = 'post_edit.html'
    fields = ['title', 'year', 'price', 'after', 'info'];


class BooksDeleteView(DeleteView):
    model = Books
    template_name = 'delete.html'
    success_url = reverse_lazy('todo_list')


class AboutPageView(TemplateView):
    template_name = 'about.html'
    context_object_name = 'about'

    def get_queryset(self):
        queryset = AboutPage.objects.all()
        q = self.request.GET.get('queryset')
        if q:
            queryset = queryset.filter(Q(title__contains=q) | Q(info__contains=q))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = self.get_queryset()
        return context


def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    return render(request, 'upload.html')


def download_file(request, pk):
    your_model_instance = get_object_or_404(Books, pk=pk)
    file_path = os.path.join(settings.MEDIA_ROOT, str(your_model_instance.file))
    response = FileResponse(open(file_path, 'rb'))
    return response


def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            new_book = Books(
                image=form.cleaned_data['image'],
                file=request.FILES['file'],
                title=form.cleaned_data['title'],
            )
            new_book.save()
            return redirect('book_list')

    else:
        form = FileUploadForm()
    return render(request, 'upload.html', {'form': form})


class QR_Code(TemplateView):
    template_name = 'contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qrcodes'] = QrCode.objects.all()
        return context


class BooksAPIView(APIView):
    def get(self, request):
        try:
            add = request.GET.get('clay')
            if add is not None:
                books = Books.objects.filter(all_books__gte=add).values()
            else:
                books = Books.objects.all().values()
        except:
            books = Books.objects.all().values()
        
        about_pages = AboutPage.objects.all().values()
        qr_codes = QrCode.objects.all().values()
        response_data = {
            'books': list(books),
            'about_pages': list(about_pages),
            'qr_codes': list(qr_codes),
        }

        return Response(response_data)

    def post(self, request):
        new_books = Books.objects.create(
        image=request.data['image'],
        file=request.data['file'],
        info=request.data['info'],
        year=request.data['year'],
        price=request.data['price'],
        after=request.data['after'],
        number_of_views=request.data['number_of_views'],
        )
        return Response({'new_books': model_to_dict(new_books)})

    @api_view(['DELETE'])
    @permission_classes([IsAdminUser])
    def delete(request, book_id):
        try:
            book = Books.objects.get(pk=book_id)
            book.delete()
            return Response({'res': 'success'})
        except Books.DoesNotExist:
            return Response({'res': 'error', 'message': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'res': 'error', 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Userlar uchun shikoyat va Savoliga Javoblar

def complaints_list(request):
    if request.user.is_superuser:
        complaints = Complaint.objects.filter(is_resolved=False)
    else:
        complaints = Complaint.objects.filter(user=request.user, is_resolved=False)
    return render(request, 'complaints/complaints_list.html', {'complaints': complaints})


def create_complaint(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        user = request.user
        complaint = Complaint.objects.create(user=user, text=text)
        return redirect('complaints_list')
    return render(request, 'complaints/create_complaint.html')


def respond_to_complaint(request, pk):
    complaint = get_object_or_404(Complaint, pk=pk)
    if request.method == 'POST':

        response_text = request.POST.get('response')
        complaint.response = response_text
        complaint.is_resolved = True
        complaint.save()
        return redirect('complaints_list')
    return render(request, 'complaints/respond_to_complaint.html', {'complaint': complaint})


@api_view(['GET'])
def user_detail(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializers(user)
        return Response({"result": serializer.data})