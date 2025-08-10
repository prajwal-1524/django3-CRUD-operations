from django.shortcuts import render, redirect, get_object_or_404
from myapp.models import Student
from myapp.forms import StudentForms  # Use proper import path

# Create your views here. 
def home(request, id=None): 
    #url ma update/ path diyepaxi with id=5 through post method request janxa , since /update/id ma views.home diyexam so home function ma janxa request , in home we have this ,  id=None if id aayena vani through request default none xa 

    # first check garnu parcha if POST request ho ki hoina 
    if request.method == 'POST':
        # aba POST request vako bela check garne if delete button click vako ho ki hoina
        if 'delete' in request.POST:
            # request.POST means the dictionary and its value is id,, and if in the url ma show garne dictionary ma delete xa vaney  vako ho ....
            student_to_delete = get_object_or_404(Student, id=request.POST['delete']) # it means if request.POST dictionary ma delete vanni key aako xa vaney and its value is id, tyo object lai tanera lyaunu  in student_to_delete object ma rakhnu vaneko ho 
            # id = request.POST[delete]   request.POST[delete] ko value id hunxa  
            student_to_delete.delete()  # tyo object tanera object.delete() function call garnu 
            return redirect('home')  # delete garisakepaxi home ma redirect garos

    if id:
        student_update = get_object_or_404(Student, id=id)
        # if request ma id aako xa vaney edit button click garepaxi, student_update object ma tyo user object info hold garne hoina vaney 404 show gardine  
        
        form = StudentForms(request.POST or None, instance=student_update)  # yesle updated form dine ho , tara if we donot have to edit the user , None le chai khali form dinxa , instance=student_update le .. tyo form ko name ,age ma student_update wala data show gardinxa 
    else:  #request.POST is a dictionary 
        form = StudentForms(request.POST or None)  # if we dont have to update the form normally submit garne or show garne

    # aba feri check garnu parcha if POST request ho ki hoina (yesto case ma form submit vako hunchha)
    if request.method == 'POST':
        form = form  # id aayo vaney mathiko if part ko form render hunxa hoina vane else part ko form save hunxa that is as it is
        if form.is_valid():  # this is inbuilt function of django 
            form.save()
            return redirect('home')

    students = Student.objects.all()
    context = {
        'students': students,
        'form': form  # Add comma here to fix syntax
    }
    return render(request, 'myapp/home.html', context)
