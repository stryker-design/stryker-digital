from django.shortcuts import render
from audit.models import Audit
# Create your views here.


def audit_list(request):
    audit_list = Audit.objects.all()
    # audit_list = Audit.objects.all().order_by("-created_at").all()
    context = {'audit_list': audit_list}
    return render(request, 'audit-list.html', context)

def audit_detail(request, slug):
    audit_detail = Audit.objects.get(slug=slug)
    context = {'audit_detail': audit_detail}
    return render(request, 'audit-detail.html', context)