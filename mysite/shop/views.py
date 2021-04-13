from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Product, Contact, Order, UpdateTracker
import json


# Create your views here.
def index(request):
    allProds = []
    getCats = Product.objects.values('category')
    cats = {item['category'] for item in getCats}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        allProds.append([prod, n])

    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    contacted = False
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, phone=phone, email=email, desc=desc)
        contact.save()
        contacted = True
    return render(request, 'shop/contact.html', {'contacted': contacted})


def checkout(request):
    if request.method == 'POST':
        orderJson = request.POST.get('orderJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amount', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        address = request.POST.get('address1', '')
        state = request.POST.get('state', '')
        city = request.POST.get('city', '')
        zipCode = request.POST.get('zip', '')
        order = Order(name=name, phone=phone, email=email, orderJson=orderJson, address=address, state=state,
                      zip=zipCode, city=city, amount=amount)
        order.save()
        update = UpdateTracker(order_id=order.order_id, update_desc="Your Order Has been Placed.")
        update.save()
        order_id = order.order_id
        ordered = True
        return render(request, 'shop/checkout.html', {'ordered': ordered, 'id': order_id})
    return render(request, 'shop/checkout.html')


def tracker(request):
    if request.method == 'POST':
        order_id = request.POST.get('id', '')
        email = request.POST.get('email', '')
        if request.is_ajax():
            try:
                order = Order.objects.filter(order_id=order_id, email=email)
                if len(order) > 0:
                    update = UpdateTracker.objects.filter(order_id=order_id)
                    updates = []
                    for item in update:
                        updates.append({'text': item.update_desc, 'time': item.timeNow})
                        updates_view = json.dumps({"status":"success", "updates": updates, "items": order[0].orderJson}, default=str)
                    return HttpResponse(updates_view)
                else:
                    return HttpResponse('{"status":"NoItem"}')
            except Exception as e:
                return HttpResponse('{"status":"error"}')
    return render(request, 'shop/tracker.html')


def queryCheck(query, item):
    if query in item.prod_name.lower() or query in item.prod_desc.lower() or query in item.category.lower():
        return True
    else:
        return False


def search(request):
    query = request.GET.get('search')
    allProds = []
    getCats = Product.objects.values('category')
    cats = {item['category'] for item in getCats}
    for cat in cats:
        prodTemp = Product.objects.filter(category=cat)
        prod = [items for items in prodTemp if queryCheck(query, items)]
        n = len(prod)
        if n != 0:
            allProds.append([prod, n])
    params = {'allProds': allProds, 'msg': ""}
    if len(allProds) == 0 or len(query) < 3:
        params = {'msg': "No search result found."}
    return render(request, 'shop/search.html', params)


def productview(request, myid):
    product = Product.objects.filter(id=myid)
    print(myid)
    return render(request, 'shop/productview.html', {'product': product[0]})
