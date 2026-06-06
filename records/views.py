from django.shortcuts import render, redirect,get_object_or_404

from records.models import Record
from records.forms import RecordForm


def records(request):
    records = Record.objects.all().order_by('-created_at')
    context = {'records': records}
    return render(request, "records/main.html", context)

def create_record(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = RecordForm()
    return render(request, 'records/create_record.html', {'form': form})

def update_record(request, pk):
    record = get_object_or_404(Record, pk=pk)
    if request.method == 'POST':
        form = RecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = RecordForm(instance=record)
    return render(request, 'records/update_record.html', {'form': form, 'record': record})


def delete_record(request, pk):
    record = get_object_or_404(Record, pk=pk)
    if request.method == 'POST':
        record.delete()
        return redirect('main')
    return render(request, 'records/delete_record.html', {'record': record})
