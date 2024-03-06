from django.shortcuts import redirect, render
from django.views.generic import ListView,DetailView
from .models import *
import os
from django.http import FileResponse, HttpResponseNotFound
from django.conf import settings
from django.core.paginator import Paginator
from .forms import *
from django.core.mail import EmailMessage
from UsQolej.settings import EMAIL_HOST_USER


class EnHomeListView(ListView):
    template_name='index_en.html'


    def get(self,request):
        enaboutcollege=EnAboutCollege.objects.first()
        enprofessions=EnProfessions.objects.all()
        staffs=EnStaffs.objects.all()
        questions=EnQuestions.objects.all()
        contactus=EnContactUs.objects.first()
        context={
            'link':'Vardenis Badeyan State College',
            'enaboutcollege':enaboutcollege,
            'enprofessions':enprofessions,
            'staffs':staffs,
            'questions':questions,
            'contactus':contactus,
            


                }

        return render(request,self.template_name,context)
    
class EnProfDetail(DetailView):
    template_name='detail_en.html'

    def get(self,request,id):
        enprofessions=EnProfessions.objects.all()
        ensubprofessions=EnProfessions.objects.filter(pk=id)
        for i in ensubprofessions:
            k=str(i.name)

        context={
            'link':k,
            'enprofessions':enprofessions,
            'ensubprofessions':ensubprofessions,
                }
        
        return render(request,self.template_name,context)

class EnMijinListView(ListView):
    template_name='Mijin_en.html'


    def get(self,request):
        professions=EnProfessions.objects.all()

        context={
            'link':'professions',
            'professions':professions,
            
                }
        
        return render(request,self.template_name,context)
    
class DimordDetailView(DetailView):
    template_name='Dimord_en.html'

    def get(self,request):
        dimord=EnDimord.objects.first()

        context={
            'link':'Applicant',
            'dimord':dimord,
                }
        
        return render(request,self.template_name,context)

def download_pdf(request, filename):
    pdf_path = os.path.join(settings.MEDIA_ROOT, 'pdf', filename)
    if os.path.exists(pdf_path):
        with open(pdf_path, 'rb') as pdf_file:
            response = FileResponse(pdf_file, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename=' + filename
            return response
    else:
        return HttpResponseNotFound("The requested PDF was not found.")
    
class DownloadListView(ListView):
    template_name='download_en.html'

    def get(self,request):
        p=Paginator(EnPDFiles.objects.all(),6)
        page=request.GET.get('page')
        pdfiles=p.get_page(page)
        myvideo=EnMyVideo.objects.first()

        context={
            'link':'library',
            'pdfiles':pdfiles,
            'myvideo':myvideo,

                }
        
        return render(request,self.template_name,context)

def EnSearchWord(request):

    pdfiles=EnPDFiles.objects.filter(name__icontains=request.GET.get('p'),)
    return render(request,'download_en.html',{
                                        'link':'library',
                                        'pdfiles':pdfiles,
})

class EnContactUsPage(DetailView):
    template_name='contact_us_en.html'

    def get(self,request):
        form=EnContactModelForm

        context={
            'link':'Contact Us',
            'form':form,
        }

        return render(request,self.template_name,context)

    def post(self,request):
        form=EnContactModelForm(request.POST)
        if form.is_valid():
                email=EmailMessage(
                subject=f'Նոր նամակ ARM-ZONA-ից',
                body=f"Անուն ազգանուն-{request.POST.get('name')} \n Ենթատեքստ - {request.POST.get('subject')} \n Նամակ - {request.POST.get('message')}",
                from_email=EMAIL_HOST_USER,
                to=['vardenisibsqolej@gmail.com'],
                )
                email.send()
                form.save()
                return redirect('home_en')
        else:
            return EnContactModelForm()
        

class EnAshxatakazm(ListView):
    template_name='ashxatakazm_en.html'


    def get(self,request):
        staffs=EnStaffs.objects.all()

        context={
            'link':'Stuffs',
            'staffs':staffs,

                }
        
        return render(request,self.template_name,context)



class EnAshxDetail(DetailView):
    template_name='ashx_detail_en.html'

    def get(self,request,id):
        stuff=EnStaffs.objects.filter(pk=id)


        context={
            'link':'Stuffs',
            'stuff':stuff,

                }
        
        return render(request,self.template_name,context)