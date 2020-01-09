from django.urls import path, include, re_path
from . import views

app_name = 'info'

urlpatterns = [

   # path('test/', views.Test.as_view()),

    path('api/', include([
        path('v1/', include([
            path('transport-full/all/', views.TransportFullListAPIView.as_view()),
            path('transport-full/create/', views.TransportFullCreateAPIView.as_view()),
            path('transport-full/detail/<int:pk>', views.TransportFullDetailAPIView.as_view()),

            path('goods-count/all/', views.GoodsCountListAPIView.as_view()),
            path('goods-count/create/', views.GoodsCountCreateAPIView.as_view()),
            path('goods-count/detail/<int:pk>', views.GoodsCountDetailAPIView.as_view()),

        ])),
    ])),

    path('order-client/', include([
        path('', views.OrderClientListView.as_view(), name='order-client-list'),
        path('<int:pk>/', views.OrderClientDetailView.as_view(), name='order-client-detail'),
        path('create/', views.OrderClientCreateView.as_view(), name='organization-create'),
    #     path('<int:pk>/update/', views.OrderClientUpdateView.as_view(), name='order-client-update'),
    #     path('<int:pk>/delete/', views.OrderClientDeleteView.as_view(), name='order-client-delete'),
    ])),

    path('organization/', include([
        path('', views.OrganizationListView.as_view(), name='organization-list'),
        path('<int:pk>/', views.OrganizationDetailView.as_view(), name='organization-detail'),
        path('create/', views.OrganizationCreateView.as_view(), name='organization-create'),
    #     path('<int:pk>/update/', views.OrganizationUpdateView.as_view(), name='organization-update'),
    #     path('<int:pk>/delete/', views.OrganizationDeleteView.as_view(), name='organization-delete'),
    ])),

    path('goods/', include([
        path('', views.GoodsListView.as_view(), name='goods-list'),
        path('<int:pk>/', views.GoodsDetailView.as_view(), name='goods-detail'),
        path('create/', views.GoodsCreateView.as_view(), name='goods-create'),
    #     path('<int:pk>/update/', views.GoodsUpdateView.as_view(), name='goods-update'),
    #     path('<int:pk>/delete/', views.GoodsDeleteView.as_view(), name='goods-delete'),
    ])),

    path('transport/', include([
        path('', views.TransportListView.as_view(), name='transport-list'),
        path('<int:pk>/', views.TransportDetailView.as_view(), name='transport-detail'),
        path('create/', views.TransportCreateView.as_view(), name='transport-create'),
    #     path('<int:pk>/update/', views.TransportUpdateView.as_view(), name='transport-update'),
    #     path('<int:pk>/delete/', views.TransportDeleteView.as_view(), name='transport-delete'),
    ])),

    path('driver/', include([
        path('', views.DriverListView.as_view(), name='driver-list'),
        path('<int:pk>/', views.DriverDetailView.as_view(), name='driver-detail'),
        path('create/', views.DriverCreateView.as_view(), name='driver-create'),
    #     path('<int:pk>/update/', views.DriverUpdateView.as_view(), name='driver-update'),
    #     path('<int:pk>/delete/', views.DriverDeleteView.as_view(), name='driver-delete'),
    ])),

    path('аdres/', include([
        path('', views.AddressListView.as_view(), name='аdres-list'),
        path('<int:pk>/', views.AddressDetailView.as_view(), name='аdres-detail'),
        path('create/', views.AddressCreateView.as_view(), name='аdres-create'),
    #     path('<int:pk>/update/', views.AddressUpdateView.as_view(), name='аdres-update'),
    #     path('<int:pk>/delete/', views.AddressDeleteView.as_view(), name='аdres-delete'),
    ])),

    path('executor-person/', include([
        path('', views.ExecutorPersonListView.as_view(), name='executor-person-list'),
        path('<int:pk>/', views.ExecutorPersonDetailView.as_view(), name='executor-person-detail'),
        path('create/', views.ExecutorPersonCreateView.as_view(), name='executor-person-create'),
    #     path('<int:pk>/update/', views.ExecutorPersonUpdateView.as_view(), name='executor-person-update'),
    #     path('<int:pk>/delete/', views.ExecutorPersonDeleteView.as_view(), name='executor-person-delete'),
    ])),

    path('executor-legal/', include([
        path('', views.ExecutorLegalListView.as_view(), name='executor-legal-list'),
        path('<int:pk>/', views.ExecutorLegalDetailView.as_view(), name='executor-legal'),
        path('create/', views.ExecutorLegalCreateView.as_view(), name='executor-legal'),
    #     path('<int:pk>/update/', views.ExecutorLegalUpdateView.as_view(), name='executor-legal'),
    #     path('<int:pk>/delete/', views.ExecutorLegalDeleteView.as_view(), name='executor-legal'),
    ])),

    path('client-person/', include([
        path('', views.ClientPersonListView.as_view(), name='client-person-list'),
        path('<int:pk>/', views.ClientPersonDetailView.as_view(), name='client-person'),
        path('create/', views.ClientPersonCreateView.as_view(), name='sclient-person'),
    #     path('<int:pk>/update/', views.ClientPersonUpdateView.as_view(), name='client-person'),
    #     path('<int:pk>/delete/', views.ClientPersonDeleteView.as_view(), name='client-person'),
    ])),

    path('client-legal/', include([
        path('', views.ClientLegalListView.as_view(), name='client-legal-list'),
        path('<int:pk>/', views.ClientLegalDetailView.as_view(), name='client-legal'),
        path('create/', views.ClientLegalCreateView.as_view(), name='client-legal'),
    #     path('<int:pk>/update/', views.ClientLegalUpdateView.as_view(), name='client-legal'),
    #     path('<int:pk>/delete/', views.ClientLegalDeleteView.as_view(), name='client-legal'),
    ])),

    path('tariff/', include([
        path('', views.TariffListView.as_view(), name='tariff-list'),
        path('<int:pk>/', views.TariffDetailView.as_view(), name='tariff-detail'),
        path('create/', views.TariffCreateView.as_view(), name='tariff-create'),
    #     path('<int:pk>/update/', views.TarifUpdateView.as_view(), name='tariff-update'),
    #     path('<int:pk>/delete/', views.TarifDeleteView.as_view(), name='tariff-delete'),
    ])),
]
