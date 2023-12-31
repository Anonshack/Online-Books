from django.urls import path
from .views import (AllBooks,
                    QR_Code,
                    HomePageView,

                    BooksDetailView,
                    BookUpdateView,

                    BooksDeleteView,
                    AboutPageView,

                    BooksAPIView,
                    upload_file,

                    download_file,
                    item_detail,

                    complaints_list,
                    create_complaint,

                    respond_to_complaint,
                    user_detail,
                    )

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path("api/", BooksAPIView.as_view()),

    path('user-list/<int:user_id>/', user_detail, name='user-detail'),
    path('book/edit/<int:pk>', BookUpdateView.as_view(), name='edit_book'),

    path('view/<int:pk>/', BooksDetailView.as_view(), name='book_detail'),
    path('book/delete/<int:pk>/', BooksDeleteView.as_view(), name='book_delete'),

    path('upload/', upload_file, name='upload_file'),
    path('contacts/', QR_Code.as_view(), name="contacts"),

    path('item/<int:item_id>/', item_detail, name='item_detail'),
    path('download/<int:pk>/', download_file, name='download_file'),

    path('about/', AboutPageView.as_view(), name='about'),
    path('books/', AllBooks.as_view(), name='all_books'),


    path('complaints/', complaints_list, name='complaints_list'),
    path('complaints/create/', create_complaint, name='create_complaint'),
    path('complaints/respond/<int:pk>/', respond_to_complaint, name='respond_to_complaint'),
]
