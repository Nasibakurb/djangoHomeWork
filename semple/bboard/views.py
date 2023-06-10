from django.shortcuts import render, redirect,  get_object_or_404
from django.views.generic import ListView
from .models import SMS
from .forms import SMSForm


def read_sms(request):
    pass

def get_sms(request):
    pass


def create_sms(request):
    if request.method == 'POST':
        form = SMSForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sms_list')
    else:
        form = SMSForm()
    return render(request, 'create_sms.html', {'form': form})

def delete_sms(request, sms_id):
    sms = get_object_or_404(SMS, pk=sms_id)
    if request.method == 'POST':
        sms.delete()
        return redirect('sms_list')
    return render(request, 'delete_sms.html', {'sms': sms})

class SMSListView(ListView):
    model = SMS
    template_name = 'sms_list.html'
    context_object_name = 'sms_list'




# def send_sms(phone_number, message):
#     client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
#     client.messages.create(
#         body=message,
#         from_=settings.TWILIO_PHONE_NUMBER,
#         to=phone_number
#     )
# send_sms('+77771669948', 'Здравствуйте, меня зовут Насиба.')


