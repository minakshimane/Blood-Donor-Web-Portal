from django import forms
from django.forms import ValidationError
from BloodDonor.models import Donor,Admin


import  datetime
class RegisterForm(forms.ModelForm):
    group_values = (
        ('A+', 'A+'),
        ('O+', 'O+'),
        ('B', 'B+'))
    CHOICES=(
        ('Male','Male'), ('Female','Female')

)
    name = forms.CharField(max_length=30, widget= forms.TextInput
                           (attrs={'class':'form-control'}))
    username = forms.CharField(max_length=30,widget= forms.TextInput
                           (attrs={'class':'form-control'}))
    password = forms.CharField(max_length=30,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    gender = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class':'form-check-input'}), choices=CHOICES)
    email = forms.EmailField(max_length=100,widget=forms.EmailInput(attrs={'class':'form-control'}))
    contact = forms.IntegerField()
    bloodgroup = forms.ChoiceField(choices=group_values,widget=forms.Select(attrs={'class':'form-control'}))
    country = forms.CharField(max_length=30,widget=forms.Select(attrs={"id":"country",'class':'form-control'}))
    state = forms.CharField(max_length=50,widget=forms.Select(attrs={"id":"state",'class':'form-control'}))
    city = forms.CharField(max_length=50,widget=forms.Select(attrs={"id":"city",'class':'form-control'}))
    age = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
    weight = forms.DecimalField(max_digits=5, decimal_places=2,widget=forms.TextInput(attrs={'class':'form-control'}))
    ldd = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control'}))

    def clean_contact(self):
        no = self.cleaned_data["contact"]  # is used to get data from input field
        if len(str(no)) == 10:
            return no
        else:
            raise ValidationError("Invalid Contact Number")
    def clean_username(self):
        un=self.cleaned_data["username"]
        if un != Donor.username:
            return un
        else:
            raise ValidationError("Username is allready in use")

    class Meta:
        model = Donor
        fields = "__all__"

class AdminForm(forms.ModelForm):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)
    class Meta:
        model = Admin
        fields = "__all__"



