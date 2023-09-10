from django import forms


# Signup Form:
class SignupForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput,
    )
    password_confirmation = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput,
    )


# Login Form:
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(
        max_length=50,
        # override default <input type='text>
        widget=forms.PasswordInput,
    )
