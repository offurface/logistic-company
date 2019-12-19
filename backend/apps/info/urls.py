from django.urls import path, include, re_path
from . import views

app_name = 'info'

urlpatterns = [

    path('organization/', include([
        path('', views.OrganizationListView.as_view(), name='organization-list'),
    #     path('<int:pk>/', views.SportTypeDetailView.as_view(), name='sport-type-detail'),
    #     path('create/', views.SportTypeCreateView.as_view(), name='sport-type-create'),
    #     path('<int:pk>/update/', views.SportTypeUpdateView.as_view(), name='sport-type-update'),
    #     path('<int:pk>/delete/', views.SportTypeDeleteView.as_view(), name='sport-type-delete'),
    ])),

    path('goods/', include([
        path('', views.GoodsListView.as_view(), name='goods-list'),
    #     path('<int:pk>/', views.CoachDetailView.as_view(), name='coach-detail'),
    #     path('create/', views.CoachCreateView.as_view(), name='coach-create'),
    #     path('<int:pk>/update/', views.CoachUpdateView.as_view(), name='coach-update'),
    #     path('<int:pk>/delete/', views.CoachDeleteView.as_view(), name='coach-delete'),
    ])),

    path('transport/', include([
        path('', views.TransportListView.as_view(), name='transport-list'),
    #     path('<int:pk>/', views.ParentDetailView.as_view(), name='transport-detail'),
    #     path('create/', views.ParentCreateView.as_view(), name='transport-create'),
    #     path('<int:pk>/update/', views.ParentUpdateView.as_view(), name='transport-update'),
    #     path('<int:pk>/delete/', views.ParentDeleteView.as_view(), name='transport-delete'),
    ])),

    # path('driver/', include([
    #     path('', views.SportsmanListView.as_view(), name='sportsman-list'),
    #     path('<int:pk>/', views.SportsmanDetailView.as_view(), name='sportsman-detail'),
    #     path('create/', views.SportsmanCreateView.as_view(), name='sportsman-create'),
    #     path('<int:pk>/update/', views.SportsmanUpdateView.as_view(), name='sportsman-update'),
    #     path('<int:pk>/delete/', views.SportsmanDeleteView.as_view(), name='sportsman-delete'),
    #     path('<int:pk>/primary/', views.PrimaryCreateView.as_view(), name='sportsman-primary'),
    #     path('<int:pk>/umo/', views.UMOCreateView.as_view(), name='sportsman-umo'),
    # ])),

    # path('Adres/', include([
    #     path('', views.SportsmanListView.as_view(), name='sportsman-list'),
    #     path('<int:pk>/', views.SportsmanDetailView.as_view(), name='sportsman-detail'),
    #     path('create/', views.SportsmanCreateView.as_view(), name='sportsman-create'),
    #     path('<int:pk>/update/', views.SportsmanUpdateView.as_view(), name='sportsman-update'),
    #     path('<int:pk>/delete/', views.SportsmanDeleteView.as_view(), name='sportsman-delete'),
    #     path('<int:pk>/primary/', views.PrimaryCreateView.as_view(), name='sportsman-primary'),
    #     path('<int:pk>/umo/', views.UMOCreateView.as_view(), name='sportsman-umo'),
    # ])),

    # path('ExecutorPerson/', include([
    #     path('', views.SportsmanListView.as_view(), name='sportsman-list'),
    #     path('<int:pk>/', views.SportsmanDetailView.as_view(), name='sportsman-detail'),
    #     path('create/', views.SportsmanCreateView.as_view(), name='sportsman-create'),
    #     path('<int:pk>/update/', views.SportsmanUpdateView.as_view(), name='sportsman-update'),
    #     path('<int:pk>/delete/', views.SportsmanDeleteView.as_view(), name='sportsman-delete'),
    #     path('<int:pk>/primary/', views.PrimaryCreateView.as_view(), name='sportsman-primary'),
    #     path('<int:pk>/umo/', views.UMOCreateView.as_view(), name='sportsman-umo'),
    # ])),

    # path('ExecutorLegal/', include([
    #     path('', views.SportsmanListView.as_view(), name='sportsman-list'),
    #     path('<int:pk>/', views.SportsmanDetailView.as_view(), name='sportsman-detail'),
    #     path('create/', views.SportsmanCreateView.as_view(), name='sportsman-create'),
    #     path('<int:pk>/update/', views.SportsmanUpdateView.as_view(), name='sportsman-update'),
    #     path('<int:pk>/delete/', views.SportsmanDeleteView.as_view(), name='sportsman-delete'),
    #     path('<int:pk>/primary/', views.PrimaryCreateView.as_view(), name='sportsman-primary'),
    #     path('<int:pk>/umo/', views.UMOCreateView.as_view(), name='sportsman-umo'),
    # ])),

    # path('ClientPerson/', include([
    #     path('', views.SportsmanListView.as_view(), name='sportsman-list'),
    #     path('<int:pk>/', views.SportsmanDetailView.as_view(), name='sportsman-detail'),
    #     path('create/', views.SportsmanCreateView.as_view(), name='sportsman-create'),
    #     path('<int:pk>/update/', views.SportsmanUpdateView.as_view(), name='sportsman-update'),
    #     path('<int:pk>/delete/', views.SportsmanDeleteView.as_view(), name='sportsman-delete'),
    #     path('<int:pk>/primary/', views.PrimaryCreateView.as_view(), name='sportsman-primary'),
    #     path('<int:pk>/umo/', views.UMOCreateView.as_view(), name='sportsman-umo'),
    # ])),

    # path('ClientLegal/', include([
    #     path('', views.SportsmanListView.as_view(), name='sportsman-list'),
    #     path('<int:pk>/', views.SportsmanDetailView.as_view(), name='sportsman-detail'),
    #     path('create/', views.SportsmanCreateView.as_view(), name='sportsman-create'),
    #     path('<int:pk>/update/', views.SportsmanUpdateView.as_view(), name='sportsman-update'),
    #     path('<int:pk>/delete/', views.SportsmanDeleteView.as_view(), name='sportsman-delete'),
    #     path('<int:pk>/primary/', views.PrimaryCreateView.as_view(), name='sportsman-primary'),
    #     path('<int:pk>/umo/', views.UMOCreateView.as_view(), name='sportsman-umo'),
    # ])),


]
