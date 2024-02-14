from django import forms


class GmailMessageForm(forms.Form):
    sender_email = forms.EmailField(label='Your Email')
    sender_password = forms.CharField(label='Your Password', widget=forms.PasswordInput)
    recipient_email = forms.EmailField(label='Recipient Email')
    subject = forms.CharField(label='Subject', max_length=100)
    message = forms.CharField(label='Message', widget=forms.Textarea)


class GmailInboxForm(forms.Form):
    email = forms.EmailField(label='Your Email')
    password = forms.CharField(label='Your Password', widget=forms.PasswordInput)