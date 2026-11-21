from django.shortcuts import render

def churn_rate(request):
    iv=int(request.POST.get('initialvalue','0'))
    lv=int(request.POST.get('lostvalue','0'))
    cr=(lv/iv)*100 if(request.method=="POST") else 0
    print(f"Initial_Customers: {iv} \n Lost_Customers: {lv} \n Churn Rate: {cr}")
    return render(request, "myapp/sri.html",{"iv": iv, "lv": lv, "cr": cr})
    
