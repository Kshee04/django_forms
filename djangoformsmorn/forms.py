from django import forms


class StudentForm(forms.Form):
    firstname = forms.CharField(label="Enter first name", max_length=50)
    lastname = forms.CharField(label="Enter last name", max_length=50)
    email = forms.CharField(label="Enter email", max_length=30)
    admissionnumber=forms.CharField(label="Enter ADM No",max_length=20)
    stream=forms.CharField(label="Enter your class",max_length=15)
# class TeacherForm(forms.Form):
#     firstname = forms.CharField(label="Enter first name", max_length=50)
#     lastname = forms.CharField(label="Enter last name", max_length=50)
#     email = forms.CharField(label="Enter email", max_length=30)
#     number= forms.CharField(label="Enter phone number",max_length=15)
#     id= forms.CharField(label="Enter ID No",max_length=50)
#     nationality=forms.CharField(label="Enter your nationality",max_length=50)
