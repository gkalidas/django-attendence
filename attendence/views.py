from django.http import HttpResponse

def loginMassage(request):
    return HttpResponse('Welcome to the CRENEXA attendence tracking system, how may I help may?')
