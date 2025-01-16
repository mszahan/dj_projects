from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from .models import Profile
from weasyprint import HTML

def accept(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        summary = request.POST.get('summary', '')
        degree = request.POST.get('degree', '')
        school = request.POST.get('school', '')
        University = request.POST.get('university', '')
        previous_work = request.POST.get('previous_work', '')
        skills = request.POST.get('skills', '')

        profile = Profile(name=name, email=email, phone=phone, summary=summary, degree=degree, school=school,
                          University=University, previous_work=previous_work, skills=skills )
        profile.save()
        
    return render(request, 'accept.html')


def cv(request, id):
    user_profile = Profile.objects.get(pk=id)
    #render the html content using the template
    html_content = render_to_string('cv.html', {'user':user_profile})

    #generate the pdf from the html content
    pdf_file = HTML(string=html_content, base_url=request.build_absolute_uri()).write_pdf()
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename={user_profile.name}_cv.pdf'
    return response
