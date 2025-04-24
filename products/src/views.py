from django.http import HttpResponse
from django.shortcuts import render

def products (request):
    products = [{
        "name": "Rexona",
        "availableQuantity": 2,
        "unitPrice":  5.00,
    }, {
          "name": "MacBook",
        "availableQuantity": 6,
        "unitPrice": 30000,
    }, {
           "name": "Iphone 16",
        "availableQuantity": 5,
        "unitPrice": 5999,
    },
     {
           "name": "Mouse Logitech",
        "availableQuantity": 6,
        "unitPrice": 200,
    },
      {
           "name": "Cadeira Gamer",
        "availableQuantity": 1,
        "unitPrice": 800,
    },]
    return render(request, 'products.html', {'products': products})
     