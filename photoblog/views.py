from stevelosh.photoblog.models import Entry
from django.shortcuts import get_object_or_404, render_to_response

def entry(request, year=None, month=None, day=None, slug=None):
    if year == None and month == None and day == None and slug == None:
        entry = Entry.objects.all().order_by('-pub_date')[0]
    else:
        entry = get_object_or_404(Entry, slug=slug, pub_date__year=year, 
                                  pub_date__month=month, pub_date__day=day,)
    
    return render_to_response('photoblog/entry.html', { 'entry': entry })