from django.shortcuts import render
from .documents import MyModelDocument

def search(request):

    q = request.GET.get('q')

    if q:
        mymodels = MyModelDocument.search().query('multi_match', query=q, fields=['name','year','country','productionID'])
        # mymodels = MyModelDocument.search().query('match', name=q)
        # mymodels = MyModelDocument.search().query('match', year=q)
        # mymodels = MyModelDocument.search().query('match', country=q)
        # mymodels = MyModelDocument.search().query('match', productID=q)
    else:
        mymodels = ''

    return render(request, 'search.html', {'mymodels': mymodels})