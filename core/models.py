# core/models.py

from django.db import models

class Customer(models.Model):
    """
    Represents a customer in the system.
    """
    name = models.CharField(max_length=200, verbose_name="Customer Name")
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    total_orders = models.IntegerField(default=0)
    last_order_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    """
    Represents a product in the inventory.
    """
    name = models.CharField(max_length=200, verbose_name="Product Name")
    sku = models.CharField(max_length=50, unique=True, verbose_name="SKU")
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField(default=0, verbose_name="In Stock")

    def __str__(self):
        return self.name

class Order(models.Model):
    """
    Represents a customer order.
    """
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ]

    order_id = models.CharField(max_length=50, unique=True, verbose_name="Order ID")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    order_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order #{self.order_id} - {self.customer.name}"

class OrderItem(models.Model):
    """
    Represents a single item within an order.
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} for Order #{self.order.order_id}"
