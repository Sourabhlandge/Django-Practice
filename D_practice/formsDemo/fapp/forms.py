from django import forms
from django.core import validators


# def starts_with_s(value):
# if value[0].lower()!='s': also applicable
# raise forms.ValidationError('Name Should be start with s')
#   if value.isalpha()!=True:
#     raise forms.ValidationError('Name Should Contains only Alphabet Symbols')
# def gmail_varification(value):
#   if value[len(value)-9:] != 'gmail.com':
#      raise forms.ValidationError('Must Be gmail')

class StudentRegistrationForm(forms.Form):
    # name = forms.CharField(validators=[starts_with_s])
    name = forms.CharField()
    enroll = forms.IntegerField()
    # email = forms.EmailField(validators=[gmail_varification])
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    rpassword = forms.CharField(widget=forms.PasswordInput)
    feedback = forms.CharField(widget=forms.Textarea,
                               validators=[validators.MaxLengthValidator(40), validators.MinLengthValidator(10)])
    bot_handler = forms.CharField(required=False,widget=forms.HiddenInput)




    def clean(self):
        print("Total Form Validation")
        cleaned_data = super().clean()
        inputname = cleaned_data['name']
        if len(inputname) < 10:
            raise forms.ValidationError('Name should contains minimum 7 Char')
        inputenroll = cleaned_data['enroll']
        if len(str(inputenroll))!=3:
            raise forms.ValidationError('Roll no should contains exactly 3 digit ')
        inputpassword = cleaned_data['password']
        inputrpassword = cleaned_data['rpassword']
        if inputpassword != inputrpassword:
            raise forms.ValidationError('Password not Matched')
        bot_handler_value = cleaned_data['bot_handler']
        if len(bot_handler_value)>0:
            raise forms.ValidationError('Thanks Bot!!!')
# def clean_name(self):
#    inputname = self.cleaned_data['name']
#    print('Validating Name')
#    if len(inputname)<4:
#        raise forms.ValidationError('The length of name filed should  >=4')
#    return inputname
# def clean_enroll(self):
#   inputenroll = self.cleaned_data['enroll']
#   print('Validating Enrollment')
#   return inputenroll
# def clean_email(self):
#    inputemail = self.cleaned_data['email']
#    print('Validating Email')
#    return inputemail
# def clean_feedback(self):
#   inputfeedback = self.cleaned_data['feedback']
#   print('Validating Feedback')
#    return inputfeedback
