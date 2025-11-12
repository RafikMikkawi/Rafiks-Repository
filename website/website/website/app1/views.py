from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Movie
from .forms import MovieForm
# from .forms import CreateStudentForm,CreateCourseForm,GPAForm
# from .models import Student,Course_Taken


# def index(request):
# 	return render(request,'index.html')

# def add_student(request):
# 	if request.method == 'POST':
# 		form = CreateStudentForm(request.POST)
# 		if form.is_valid():
# 			studentform = form.cleaned_data
# 			first = studentform['Student_id']
# 			last = studentform['Student_name']
# 			Student.objects.create(Student_id=first,Student_name=last)
# 			return render(request, 'index.html')
# 	else:
# 		form = CreateStudentForm()
# 	S=Student.objects.all()
# 	return render(request, 'add_student.html', {'form': form,'S':S})


# def add_course(request):
# 	if request.method == 'POST':
# 		form = CreateCourseForm(request.POST)
# 		if form.is_valid():
# 			courseform = form.cleaned_data
# 			Student_id = courseform['Student_id']
# 			Course_id = courseform['Course_id']
# 			Semester = courseform['Semester']
# 			Number_of_credits = courseform['Number_of_credits']
# 			Grade = courseform['Grade']
# 			Course_Taken.objects.create(Student_id=Student_id,Course_id=Course_id,Semester=Semester,Number_of_credits=Number_of_credits,Grade=Grade)

# 			listing = Course_Taken.objects.filter(Student_id=Student_id)
# 			summ = 0.0
# 			credits = 0
# 			for l in listing:
# 				summ =summ+ l.Grade * l.Number_of_credits
# 				credits =credits+ l.Number_of_credits
# 			avg = summ / credits
# 			for e in Student.objects.all():
# 				if e.Student_id==Student_id:
# 					e.object.set(gpa=avg)
# 			return render(request, 'index.html')
# 	else:
# 		form = CreateCourseForm()
# 	S=Course_Taken.objects.all()
# 	return render(request, 'add_course.html', {'form': form,'S':S})
	

# def report(request):
# 	if request.method == 'POST':
# 		form = GPAForm(request.POST)

# 		if form.is_valid():
# 			courseform = form.cleaned_data
# 			Student_id = courseform['Student_id']
						
# 			for e in Student.objects.all():
# 				if e.Student_id==Student_id:
# 					A=e
# 			return render(request, 'report_student.html', { 'form': form,'A':A})
		
# 	else:
# 		form= GPAForm()
# 	return render(request,'report_student.html',{'form':form})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from .forms import MovieForm

def index(request):
    movies = Movie.objects.all()
    return render(request, 'index.html', {'movies': movies})

def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MovieForm()
    return render(request, 'add_movie.html', {'form': form})

def edit_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MovieForm(instance=movie)
    return render(request, 'edit_movie.html', {'form': form})

def delete_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        movie.delete()
        return redirect('index')
    return render(request, 'delete_movie.html', {'movie': movie})

		