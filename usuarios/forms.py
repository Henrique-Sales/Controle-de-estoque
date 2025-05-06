from django import forms

class loginForm(forms.Form):
    nome = forms.CharField(
        label="Login",
        max_length=100,
        required=True,

        widget=forms.TextInput(
            attrs={
                "class" : "form-control"
            }
        )

    )

    senha = forms.CharField(
    label="Senha",  
    max_length=70,
    required=True,
    widget=forms.PasswordInput(
        attrs={
            "class" : "form-control"
        }
    )
    )