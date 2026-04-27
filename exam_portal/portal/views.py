from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import ExamForm


# 🔐 LOGIN VIEW
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid Credentials'})

    return render(request, 'login.html')


# 📊 DASHBOARD (PROTECTED)
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


# 🚪 LOGOUT
def user_logout(request):
    logout(request)
    return redirect('login')


# 📝 EXAM FORM (PROTECTED)
@login_required
def exam_form(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        course = request.POST.get('course')
        year = request.POST.get('year')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        # Save data
        ExamForm.objects.create(
            full_name=full_name,
            course=course,
            year=year,
            address=address,
            phone_number=phone
        )

        return render(request, 'success.html')

    return render(request, 'exam_form.html')


# 📋 VIEW SUBMITTED FORMS (PROTECTED)
@login_required
def view_forms(request):
    data = ExamForm.objects.all()
    return render(request, 'view_forms.html', {'data': data})