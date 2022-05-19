from django.shortcuts import render
from products.models import Product
from products.forms import ProductForm


def create_product_form(request):
    form = ProductForm(request.POST or None)
    msg = ""
    if form.is_valid():
        form.save()
        print("Data is saved in DB")
        msg = "Data is saved in DB"
        form = ProductForm()
        
    context = {
        "message" : msg,
        "prod_form" : form,
        }   
   
    return render(request, "create_product.html", context)

# Create your views here.
def view_product_page(request, prId):
    prod = Product.objects.get(id=prId)
    '''
    context = {
        "title" : prod.title,
        "description" : prod.description,
        "price" : prod.price,
        }
     '''
    context = {
        "prod" : prod,
        }
    return render(request, "product.html", context)