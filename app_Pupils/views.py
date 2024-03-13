from django.shortcuts import render

# Create your views here.
students_dict = {
    "Bahodir": ["1-oy: 89", "2-oy: 60", "3-oy: 60", "4-oy: 68", "5-oy: 70", "6-oy: 100 "],
    "Baxtiyor": ["1-oy: 78", "2-oy: 77", "3-oy: 80", "4-oy: 82", "5-oy: 86", "6-oy: 90"],
    "Sardor": ["1-oy: 68", "2-oy: 60", "3-oy: 68", "4-oy: 75", "5-oy: 78", "6-oy: 80"],
    "Eldorbek": ["1-oy: 80", "2-oy: 62", "3-oy: 66", "4-oy: 70", "5-oy: 66", "6-oy: 78"],
    "Shahlo": ["1-oy: 72", "2-oy: 78", "3-oy: 75", "4-oy: 80", "5-oy: 76", "6-oy: 82"],
}

students_list = []
grades_list = []
for i, j in students_dict.items():
    students_list.append(i)
    grades_list.append(j)


def students(request):
    context = {
        "students": students_list
    }
    return render(request, "students.html", context)


def grades(request):
    context = {
        "grades": grades_list,
        "student": students_list
    }
    return render(request, 'grades.html', context)