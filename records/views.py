from django.shortcuts import render, redirect,get_object_or_404

from records.forms.search_form import SearchForm
from records.models import Record
from records.forms.record_form import RecordForm
from records.constants import STATUS_ACTIVE


def records(request):
    search = SearchForm(request.GET)
    records = Record.objects.filter(status=STATUS_ACTIVE).order_by('-created_at')
    if search.is_valid():
        query = search.cleaned_data.get('query')
        if query:
            records = records.filter(name__icontains=query)

    context = {'records': records,
               'search': search,
               }
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
        confirm_email = request.POST.get('confirm_email')
        if confirm_email == record.email:
            record.delete()
            return redirect('main')
        else:
            return render(request, 'records/delete_record.html', {
                'record': record,
                'error': 'Неверная почта'
            })
    return render(request, 'records/delete_record.html', {'record': record})
