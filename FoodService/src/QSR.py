import datetime

class Order:
    """
    Represents a customer order.

    Attributes:
        ticket_number (int): Unique ticket number.
        customer_details (dict): Customer information (name, phone).
        items_ordered (list): List of item names.
        time_ordered (datetime): Time the order was placed.
        pick_up_time (datetime): Estimated pick-up time.
        status (str): Current status of the order (e.g., "Placed", "Fetching", "Delivered").
        total_price (float): Total price of the order

    """
    def __init__(self, ticket_number, customer_details, items_ordered, time_ordered, menu):
        self.ticket_number = ticket_number
        self.customer_details = customer_details
        self.items_ordered = items_ordered
        self.time_ordered = time_ordered
        self.status = "Placed"
        self.total_price = self.calculate_total_price(menu)
        self.pick_up_time = self.calculate_pick_up_time(menu)

    def calculate_total_price(self, menu):
      total = 0
      for item_name in self.items_ordered:
        for menu_item in menu:
          if menu_item['name'] == item_name:
            total += menu_item['price']
            break
      return total

    def calculate_pick_up_time(self, menu):
        total_prep_time = 0
        for item_name in self.items_ordered:
            for menu_item in menu:
                if menu_item['name'] == item_name:
                    total_prep_time += menu_item['preparation_time']
                    break
        return self.time_ordered + datetime.timedelta(minutes=total_prep_time)

class OrderPlacement:
    """Handles order placement."""

    def __init__(self, menu):
        self.menu = menu
        self.ticket_counter = 1

    def place_order(self, customer_details, items_ordered):
        """Places an order."""

        # Validate items
        for item_name in items_ordered:
            found = False
            for menu_item in self.menu:
                if menu_item['name'] == item_name:
                    found = True
                    break
            if not found:
                raise ValueError(f"Invalid menu item: {item_name}")

        ticket_number = self.ticket_counter
        self.ticket_counter += 1
        time_ordered = datetime.datetime.now()
        order = Order(ticket_number, customer_details, items_ordered, time_ordered, self.menu)

        return order

class KitchenOperation:
    """Handles kitchen operations."""

    def fetch_order(self, order):
        order.status = "Fetching"
        return order

    def prep_order(self, order):
        order.status = "Preparing"
        return order

    def cook_order(self, order):
        order.status = "Cooking"
        return order

class AssemblyPackaging:
    """Handles assembly and packaging."""

    def assemble_order(self, order):
        order.status = "Assembling"
        return order

    def package_order(self, order):
        order.status = "Packaging"
        return order

class DispatchDelivery:
    """Handles dispatch and delivery."""

    def dispatch_order(self, order):
        order.status = "Dispatching"
        return order

    def deliver_order(self, order):
        order.status = "Delivered"
        return order


def generate_report(orders):
    """Generates and prints an order report."""
    print("Ticket#\tTime\tName\tPhone\tItem\tPrice\tPickup\tStatus")
    for order in orders:
        items_str = ", ".join(order.items_ordered)
        pickup_status = "done" if order.status == "Delivered" else "wait" if order.status in ["Fetching", "Preparing", "Cooking", "Assembling", "Packaging", "Dispatching"] else "prep"
        print(f"{order.ticket_number}\t{order.time_ordered.strftime('%I:%M %p')}\t{order.customer_details['name']}\t{order.customer_details['phone']}\t{items_str}\t{order.total_price}\t{order.pick_up_time.strftime('%I:%M %p')}\t{pickup_status}")



# Sample Menu
menu = [
    {'name': 'Burger', 'price': 10.99, 'preparation_time': 15},
    {'name': 'Pizza', 'price': 12.99, 'preparation_time': 20},
    {'name': 'Salad', 'price': 7.99, 'preparation_time': 10},
    {'name': 'Fries', 'price': 4.99, 'preparation_time': 5},
    {'name': 'Soda', 'price': 2.99, 'preparation_time': 2}
]

# Sample Orders (10 sample orders)
sample_orders = [
    {'customer_details': {'name': 'Alice', 'phone': '555-1212'}, 'items_ordered': ['Burger', 'Fries']},
    {'customer_details': {'name': 'Bob', 'phone': '555-2121'}, 'items_ordered': ['Pizza']},
    {'customer_details': {'name': 'Charlie', 'phone': '555-3131'}, 'items_ordered': ['Salad', 'Soda']},
    {'customer_details': {'name': 'David', 'phone': '555-4141'}, 'items_ordered': ['Burger', 'Pizza']},
    {'customer_details': {'name': 'Eve', 'phone': '555-5151'}, 'items_ordered': ['Fries', 'Soda']},
    {'customer_details': {'name': 'Frank', 'phone': '555-6161'}, 'items_ordered': ['Salad']},
    {'customer_details': {'name': 'Grace', 'phone': '555-7171'}, 'items_ordered': ['Burger']},
    {'customer_details': {'name': 'Henry', 'phone': '555-8181'}, 'items_ordered': ['Pizza', 'Fries']},
    {'customer_details': {'name': 'Ivy', 'phone': '555-9191'}, 'items_ordered': ['Salad', 'Soda', 'Burger']},
    {'customer_details': {'name': 'Jack', 'phone': '555-0101'}, 'items_ordered': ['Fries', 'Pizza']}
]

# Example Usage:
order_placement = OrderPlacement(menu)
orders_processed = []

for order_data in sample_orders:
  try:
      order = order_placement.place_order(order_data['customer_details'], order_data['items_ordered'])

      kitchen = KitchenOperation()
      order = kitchen.fetch_order(order)
      order = kitchen.prep_order(order)
      order = kitchen.cook_order(order)

      assembly = AssemblyPackaging()
      order = assembly.assemble_order(order)
      order = assembly.package_order(order)

      delivery = DispatchDelivery()
      order = delivery.dispatch_order(order)
      order = delivery.deliver_order(order)

      orders_processed.append(order)
  except ValueError as e:
      print(f"Error placing order: {e}")

generate_report(orders_processed)
