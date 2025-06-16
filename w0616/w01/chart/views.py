from django.shortcuts import render
from chart.models import TotalSales

# Create your views here.
def chlist(request):
    profit = [19, 20, 21, 22, 23, 24]
    #profit = [20, 15, 7, 25, 27, 30]
    qs = TotalSales.objects.filter(year=2025)
    print(qs)
    print(list(qs.values()))
    context = {'profit':profit,'list':qs,'list_list':list(qs.values())}
    print(profit)
    return render(request,'chlist.html',context)