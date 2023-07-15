from django import forms

class userForm(forms.Form):
    first_name=forms.CharField(help_text="Enter your first name" , min_length=1)
    last_name=forms.CharField(help_text="Enter your last name" )
    email=forms.EmailField(help_text="Enter your email")
    password=forms.CharField(help_text="Choose a password",widget=forms.PasswordInput, min_length= 6)
    confirm_password=forms.CharField(help_text="Confirm the password" ,widget=forms.PasswordInput, min_length=6)    
       
    

class codeForm(forms.Form):
    code=forms.IntegerField(help_text="introduce text", max_value=9999,min_value=1000)

class loginForm(forms.Form):
    email=forms.EmailField(help_text="Enter your email")
    password=forms.CharField(help_text="Enter your password",widget=forms.PasswordInput)

class bioForm(forms.Form):
    bio=forms.CharField(help_text='introduce a small description of yourself',widget=forms.Textarea(attrs={"rows":"6"}))
      