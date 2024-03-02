from django.urls import path
from .views import *

urlpatterns=[
    path('',HomeListView.as_view(),name='home_hy'),
    path('professions/<int:id>/',ProfDetail.as_view(),name='detail_hy'),
    path('mijin_masnagitakan/',MijinListView.as_view(),name='mijin_hy'),
    path('dimord/',DimordDetailView.as_view(),name='dimord_hy'),
    path('download_file/',DownloadListView.as_view(),name='download_hy'),
    path('download/<str:filename>/', download_pdf, name='download_pdf_hy'),
    path('searchuser/',SearchWord,name='searchuser'),
    path('contact_us/',ContactUsPage.as_view(),name='contact_hy'),
    path('ashxatakazm/',Ashxatakazm.as_view(),name='ashxatakazm_hy'),
    path('stuff/<int:id>/',AshxDetail.as_view(),name='ashxdetail_hy'),
    
]