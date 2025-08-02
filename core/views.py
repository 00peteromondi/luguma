# core/views.py

from django.shortcuts import render
from .models import Customer, Product, Order

def dashboard(request):
    """
    Renders the main dashboard page with key metrics.
    """
    total_sales = sum(order.total_amount for order in Order.objects.all())
    new_orders_count = Order.objects.filter(status='Pending').count()
    low_stock_items = Product.objects.filter(stock_quantity__lt=10) # Example low stock threshold
    active_customers_count = Customer.objects.count()
    recent_activity = Order.objects.order_by('-order_date')[:5] # Get 5 most recent orders

    context = {
        'total_sales': total_sales,
        'new_orders_count': new_orders_count,
        'low_stock_items': low_stock_items.count(),
        'active_customers_count': active_customers_count,
        'recent_orders': recent_activity,
        'products_quick_view': Product.objects.all()[:3],
    }
    return render(request, 'dashboard.html', context)

def orders(request):
    """
    Renders the orders page with a list of all orders.
    """
    all_orders = Order.objects.select_related('customer').all()
    context = {'all_orders': all_orders}
    return render(request, 'orders.html', context)

def products(request):
    """
    Renders the products page with a list of all products.
    """
    all_products = Product.objects.all()
    context = {'all_products': all_products}
    return render(request, 'products.html', context)

def customers(request):
    """
    Renders the customers page with a list of all customers.
    """
    all_customers = Customer.objects.all()
    context = {'all_customers': all_customers}
    return render(request, 'customers.html', context)

def reports(request):
    """
    Renders the reports page.
    """
    # Placeholder for more advanced reporting logic
    context = {}
    return render(request, 'reports.html', context)
