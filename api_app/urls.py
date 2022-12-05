from django.urls import path
from .views.auth_views import *
from .views.user_views import *
from .views.post_view import *

all_url = {
    'url_auth':[
        path('login', AuthView.as_view({'post':'login'}), name='login'),
        path('refresh-token', AuthView.as_view({'post':'refresh_token'}), name='refresh-token'),
        path('register', AuthView.as_view({'post':'register'}), name='register'),
    ],
    'url_in_auth':[
        path('get-data-token', AuthView.as_view({'get':'get_data_token'}), name='get-data-token'),
        path('logout', AuthView.as_view({'post':'logout'}), name='logout'),
    ],
    'url_user':[
        path('all-user', UserView.as_view({'get':'all_user'}), name='all-user'),
        path('get-user/<int:id>', UserView.as_view({'get':'get_user'}), name='get_user'),
        path('add-user', AuthView.as_view({'post':'register'}), name='add-user'),
        path('edit-user/<int:id>', UserView.as_view({'put':'edit_user'}), name='edit-user'),
        path('delete-user/<int:id>', UserView.as_view({'delete':'delete_user'}), name='delete-user'),
    ],
    'url_post':[
        path('all-post', PostView.as_view({'get':'all_post'}), name='all-post'),
        path('detail-post/<int:id>', PostView.as_view({'get':'_post'}), name='detail-post'),
    ]
}

urlpatterns = []

for item in all_url:
    urlpatterns += all_url[item]