from django.shortcuts import redirect
from django.shortcuts import render
from .models import *
from django.views.generic import ListView,DetailView
from django.conf import settings
from django.http import FileResponse, HttpResponseNotFound
from django.core.paginator import Paginator
import os
from .forms import *
from django.core.mail import EmailMessage
from UsQolej.settings import EMAIL_HOST_USER


class HomeListView(ListView):
    template_name='index.html'

    def get(self,request):
        aboutcollege=AboutCollege.objects.first()
        professions=Professions.objects.all()
        professionsf=Professions.objects.first()

        staffs=Staffs.objects.all()
        questions=Questions.objects.all()
        contactus=ContactUs.objects.first()
        titletext=TitleText.objects.first()

        context={
            'link':'Վարդենիսի Բադեյան Պետական Քոլեջ',
            'aboutcollege':aboutcollege,
            'professions':professions,
            'staffs':staffs,
            'questions':questions,
            'contactus':contactus,
            'titletext':titletext,
            'professionsf':professionsf,
            

                }

        return render(request,self.template_name,context)
    


class ProfDetail(DetailView):
    template_name='detail.html'

    def get(self,request,id):
        professions=Professions.objects.all()
        subprofessions=Professions.objects.filter(pk=id)
        for i in subprofessions:
            k=str(i.name)

        context={
            'link':k,
            'professions':professions,
            'subprofessions':subprofessions,

                }
        
        return render(request,self.template_name,context)
    

class MijinListView(ListView):
    template_name='Mijin.html'


    def get(self,request):
        professions=Professions.objects.all()

        context={
            'link':'Մասնագիտություններ',
            'professions':professions,

                }
        
        return render(request,self.template_name,context)
    
class DimordDetailView(DetailView):
    template_name='Dimord.html'

    def get(self,request):
        dimord=Dimord.objects.first()

        context={
            'link':'Դիմորդ',
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
    template_name='download.html'

    def get(self,request):
        p=Paginator(PDFiles.objects.all(),6)
        page=request.GET.get('page')
        pdfiles=p.get_page(page)
        myvideo=MyVideo.objects.first()
        context={
            'link':'Գրադարան',
            'pdfiles':pdfiles,
            'myvideo':myvideo,
            
                }
        
        return render(request,self.template_name,context)

def SearchWord(request):

    pdfiles=PDFiles.objects.filter(name__icontains=request.GET.get('p'),)
    return render(request,'download.html',{
                                        'link':'Գրադարան',
                                        'pdfiles':pdfiles,
})



class ContactUsPage(DetailView):
    template_name='contact_us.html'

    def get(self,request):
        form=ContactModelForm
        

        context={
            'link':'կապ մեզ հետ',
            'form':form,
        }

        return render(request,self.template_name,context)

    def post(self,request):
        form=ContactModelForm(request.POST)
        if form.is_valid():
                email=EmailMessage(
                subject=f'Նոր նամակ VSC-ից',
                body=f"Անուն ազգանուն-{request.POST.get('name')} \n Ենթատեքստ - {request.POST.get('subject')} Նամակ - {request.POST.get('message')}",
                from_email=EMAIL_HOST_USER,
                to=['vardenisibsqolej@gmail.com'],
                )
                email.send()
                form.save()
                return redirect('home_hy')
        else:
            return ContactModelForm()
        

class Ashxatakazm(ListView):
    template_name='ashxatakazm.html'


    def get(self,request):
        staffs=Staffs.objects.all()

        context={
            'link':'Աշխատակազմ',
            'staffs':staffs,

                }
        
        return render(request,self.template_name,context)



class AshxDetail(DetailView):
    template_name='ashx_detail.html'

    def get(self,request,id):
        stuff=Staffs.objects.filter(pk=id)


        context={
            'link':'Աշխատակազմ',
            'stuff':stuff,

                }
        
        return render(request,self.template_name,context)