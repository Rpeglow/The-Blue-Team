from django import forms
from django.contrib.auth.models import User
from .models import UserInformation
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

class UserInformationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs["label_suffix"] = ""
        super().__init__(*args, **kwargs)

    STATE_CHOICES = (
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),
    )

    state = forms.ChoiceField(choices=STATE_CHOICES)

    # Fields required for Django User creation
    username = forms.RegexField(
        regex=r'^[\w.@+-]{1,150}$',
        max_length=150,
        widget=forms.TextInput(),
        validators=[
            RegexValidator(
                r'^[\w.@+-]{1,150}$',
                'Enter a valid username. This value may contain only letters, digits, and @/./+/-/_ characters.',
                'invalid_username'
            )
        ]
    )
    email = forms.EmailField(widget=forms.EmailInput(attrs={'autocomplete': 'email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}))

    #setting autocomplete attributes for the rest of the fields
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'autocomplete': 'given-name'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'autocomplete': 'family-name'}))
    phone = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'autocomplete': 'tel'}))

    class Meta:
        model = UserInformation
        exclude = ['user'] 
        fields = '__all__'
        widgets = {
            'tagline': forms.Textarea(attrs={'placeholder': 'Turning Bytes into Opportunities...'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match. Please confirm your password.")

        return cleaned_data
        
    def save(self, commit=True):
        # Save UserInformation fields
        user_info = super().save(commit=False)
        
        # Create Django User instance and set attributes
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password']
        )

        user_info.user = user  # Assign the user to the UserInformation model

        if commit:
            user.save()
            user_info.save()

        return user_info
