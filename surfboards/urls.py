from django.urls import path
from surfboards.views import (
    surfboard_list,
    my_surfboards,
    surfboard_detail,
    create_surfboard,
    edit_surfboard,
    delete_surfboard,
    create_res,
    update_res,
    delete_res,
)

urlpatterns = [
    # Surfboards
    path('', surfboard_list, name='surfboard_list'),
    path('create/', create_surfboard, name="create_surfboard"),
    path('my_surfboards/', my_surfboards, name="my_surfboards"),
    path('<int:id>/', surfboard_detail, name="surfboard_detail"),
    path('<int:id>/edit/', edit_surfboard, name='edit_surfboard'),
    path('<int:id>/delete/', delete_surfboard, name='delete_surfboard'),
    # Reservations:
    path('<int:id>/create_res/', create_res, name='create_res'),
    path('<int:id>/update_res/', update_res, name='update_res'),
    path('<int:id>/delete_res/', delete_res, name='delete_res'),

]
