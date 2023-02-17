from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from utils.email import send_email_as_html


@csrf_exempt
@require_http_methods(['POST'])
def send_contact_email(request):
    fname = request.POST.get('fname')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    message = request.POST.get('msg')
    send_email_as_html('info@petpls.com', 'Contact Us', 'email/contact_email.html',
                       {'fname': fname, 'phone': phone, 'email': email, 'message': message})
    return JsonResponse(data={})
