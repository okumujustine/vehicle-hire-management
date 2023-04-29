from django.shortcuts import render


def order_list(request):
    return render(request, "order/order_list.html", context={})
