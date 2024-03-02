from django.urls import path
from .views import *

urlpatterns=[
    path('',EnHomeListView.as_view(),name='home_en'),
    path('Proffession_en/<int:id>/',EnProfDetail.as_view(),name='detail_en'),
    path('mijin_masnagitakan/',EnMijinListView.as_view(),name='mijin_en'),
    path('dimord/',DimordDetailView.as_view(),name='dimord_en'),
    path('download_file_en/',DownloadListView.as_view(),name='download_en'),
    path('download_en/<str:filename>/', download_pdf, name='download_pdf_en'),
    path('searchuser/',EnSearchWord,name='searchuser_en'),
    path('contact_us/',EnContactUsPage.as_view(),name='contact_en'),
    path('ashxatakazm/',EnAshxatakazm.as_view(),name='ashxatakazm_en'),
    path('stuff/<int:id>/',EnAshxDetail.as_view(),name='ashxdetail_en'),
]