from django.shortcuts import render, redirect, get_object_or_404
from .models import JobApplication
from .forms import JobForm
from rest_framework import viewsets
from .models import JobApplication
from .serializers import JobSerializer

# CREATE
def add_job(request):
    form = JobForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('job_list')
    return render(request, 'job_form.html', {'form': form})

# UPDATE
def update_job(request, id):
    job = get_object_or_404(JobApplication, id=id)
    form = JobForm(request.POST, request.FILES, instance=job)
    if form.is_valid():
        form.save()
        return redirect('job_list')
    return render(request, 'job_form.html', {'form': form})

# DELETE
def delete_job(request, id):
    job = get_object_or_404(JobApplication, id=id)
    job.delete()
    return redirect('job_list')
# READ
def job_list(request):
    status = request.GET.get('status')

    if status:
        jobs = JobApplication.objects.filter(status=status)
    else:
        jobs = JobApplication.objects.all()

    total = jobs.count()
    interviews = jobs.filter(status='Interview').count()
    offers = jobs.filter(status='Offer').count()

    return render(request, 'job_list.html', {
        'jobs': jobs,
        'total': total,
        'interviews': interviews,
        'offers': offers
    })
class JobViewSet(viewsets.ModelViewSet):
    queryset = JobApplication.objects.all()
    serializer_class = JobSerializer

    def get_queryset(self):
        queryset = JobApplication.objects.all()
        status = self.request.query_params.get('status')

        if status:
            queryset = queryset.filter(status=status)

        return queryset