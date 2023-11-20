from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect,  get_object_or_404
from django.urls import reverse
from .models import Profesori
from .models import Kurset
from .forms import ProfesoriForm, KursetForm
from .forms import SubjectFrom
from django.contrib import messages
from .models import Subject
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login
from .forms import StudentRegistrationForm
from django.contrib.auth.views import LoginView
from django.http import FileResponse
import os




def dashboard(request):
    return render(request, 'stafi/dashboard.html')


def index(request):
    return render(request, 'stafi/index.html',{
        'stafi': Profesori.objects.all()
    })


def view_profesori(request, staf_id):
    staf = Profesori.objects.get(pk=staf_id)
    return redirect('index')


def add(request):
    if request.method=='POST':
        form=ProfesoriForm(request.POST)
        if form.is_valid():
            new_emri = form.cleaned_data['emri']
            new_mbiemri = form.cleaned_data['mbiemri']
            new_cel = form.cleaned_data['cel']
            new_email = form.cleaned_data['email']

        new_profesori = Profesori(
            emri=new_emri,
            mbiemri=new_mbiemri,
            cel=new_cel,
            email=new_email
        )

        new_profesori.save()
        return render(request, 'stafi/add.html', {
            'form': ProfesoriForm(),
            'success': True
        })
    else:
        form=ProfesoriForm()
        return render(request, 'stafi/add.html', {
            'form': ProfesoriForm()
        })

def edit(request, staf_id):
    staf = Profesori.objects.get(pk=staf_id)
    if request.method=='POST':
        form = ProfesoriForm(request.POST, instance=staf)
        if form.is_valid():
            form.save()
            return render(request, 'stafi/edit.html', {
                'form': form,
                'success': True
            })
    else:
        form=ProfesoriForm(instance=staf)
        return render(request, 'stafi/edit.html', {
            'form':form
        })




def delete(request, staf_id):
    success_flag = False
    if request.method=='POST':
        staf = Profesori.objects.get(pk=staf_id)
        staf.delete()
        success_flag = True
    return render(request, 'stafi/index.html', {'success_flag': success_flag})



def website(request):
    stored_messages = messages.get_messages(request)
    if request.method == 'POST':
        form = KursetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('website'))
        else:
           print(form.errors)
           return HttpResponse('Form not valid')

    else:
        form = KursetForm()
        return render(request, 'stafi/website.html', {
            'form': form,
            'kurset': Kurset.objects.all(),
            'messages': stored_messages
        })


def view_website(request, kurs_id):
    kurs = Kurset.objects.get(pk=kurs_id)
    return redirect('website')


def shtoLende(request):
    new_leksioni = ''
    new_petagogu = ''
    new_kredite = 0

    if request.method=='POST':
        form=KursetForm(request.POST)
        if form.is_valid():
            new_leksioni = form.cleaned_data['leksioni']
            new_petagogu = form.cleaned_data['petagogu']
            new_kredite = form.cleaned_data['kredite']

        new_kurset = Kurset(
            leksioni=new_leksioni,
            petagogu=new_petagogu,
            kredite=new_kredite,

        )

        new_kurset.save()
        return render(request, 'stafi/shtoLende.html', {
            'form': KursetForm(),
            'success': True
        })
    else:

        form=KursetForm()
    return render(request, 'stafi/shtoLende.html', {
            'form':form,
            'new_leksioni': new_leksioni,
            'new_petagogu': new_petagogu,
            'new_kredite': new_kredite,
        })


def editLendet(request, kurs_id):
    kurs = Kurset.objects.get(pk=kurs_id)

    if request.method=='POST':
        form = KursetForm(request.POST, instance=kurs)
        if form.is_valid():
            form.save()

            return render(request, 'stafi/editLendet.html', {
            'form':form,
            'success': True
        })
    else:
        form = KursetForm(instance=kurs)
    return render(request, 'stafi/editLendet.html', {
            'form':form,

        })


def deleteLendet(request, kurs_id):
    success_flag = False
    if request.method == 'POST':
        kurs = Kurset.objects.get(pk=kurs_id)
        kurs.delete()
        success_flag = True
    return render(request, 'stafi/website.html', {'success_flag': success_flag})




def subjects_list(request):
    mesazhet = messages.get_messages(request)
    subjects = Subject.objects.all()
    return render(request, 'stafi/subjects_list.html', {
        'subjects': subjects,
       'messages': mesazhet
    })

def subject_details(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    kurs = subject.kurset_set.all()
    return render(request, 'stafi/website.html', {'subject': subject, 'kurset': kurs})



def details(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    kurs = subject.kurset_set.all()
    return render(request, 'stafi/details.html', {'subject': subject, 'kurset': kurs})


def shto(request):
    if request.method == 'POST':
        form = SubjectFrom(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'stafi/shto.html', {
                  'form': form,
                  'success': True
    })
    else:
        form = SubjectFrom()
    return render(request, 'stafi/shto.html', {
        'form': form

    })



@login_required
def custom_home(request):
    if request.user.is_staff:
        return render(request, 'stafi/dashboard.html')



@login_required
def custom_dashboard(request):
    if request.user.is_staff:
     return render(request, 'stafi/dashboard.html')


def custom_logout(request):
    logout(request)
    return redirect('choose_login')




def register_student(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_student = True
            user.save()
            login(request, user)
            return redirect('student_dashboard')
    else:
        form = StudentRegistrationForm()
    return render(request, 'registration/register_student.html', {'form': form})


@login_required
def student_dashboard(request):
    if request.user.is_authenticated:
        if request.user.is_student:
            subjects = Subject.objects.all()
            return render(request, 'stafi/student_dashboard.html', {'subjects': subjects})
        else:
            return redirect('dashboard')
    else:
        return redirect('login_student')





class CustomLoginView(LoginView):
    template_name = 'registration/login_student.html'

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            if self.request.user.is_student:
                return redirect('student_dashboard')
        return super().form_valid(form)

    def get_success_url(self):
        return None



def choose_login(request):
    return render(request, 'stafi/choose_login.html')




def serve_lesson_file(request, subject_id, leksioni):

    kurset = get_object_or_404(Kurset, subject_id=subject_id, leksioni=leksioni)
    lesson_file_path = os.path.join('pdfs', leksioni)
    response = FileResponse(open(lesson_file_path, 'rb'))
    return response

