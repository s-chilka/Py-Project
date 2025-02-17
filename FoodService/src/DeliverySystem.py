import datetime
import random

class DeliverySystem:
    def __init__(self, num_vehicles, max_delivery_delay, distance_unit, base_return_time):
        self.num_vehicles = num_vehicles
        self.max_delivery_delay = max_delivery_delay  # in minutes
        self.distance_unit = distance_unit  # 'miles' or 'km'
        self.base_return_time = base_return_time # in minutes
        self.deliveries = []
        self.processed_entries = []
        self.vehicle_itineraries = {}

        for i in range(self.num_vehicles):
            self.vehicle_itineraries[f"V{i+1}"] = []

    def optimize_deliveries(self, orders):
        self.deliveries = orders
        print("Using Sector-Based Delivery Algorithm (Placeholder - Needs Improvement)")

        start_time = datetime.datetime.now().replace(microsecond=0)
        current_time = start_time
        delivery_number = 1

        for order in self.deliveries:
            vehicle_id = self.assign_vehicle(order)  # Assign vehicle (can be improved)
            delivery_time = self.calculate_delivery_time(order['distance'])

            estimated_arrival = current_time + datetime.timedelta(minutes=delivery_time)
            delay = (estimated_arrival - current_time).total_seconds() / 60

            if delay > self.max_delivery_delay:
                print(f"WARNING: Delivery for order {order['order']} exceeds max delay by {delay - self.max_delivery_delay} minutes!")

            self.processed_entries.append({
                's_no': delivery_number,
                'vehicle': vehicle_id,
                'sector': order['sector'],
                'distance': order['distance'], # Include distance
                'order': order['order'],
                'name': order['name'],
                'phone': order['phone'],
                'address': order['address'],
                'delivery_time': estimated_arrival.strftime("%I:%M %p")
            })
            self.vehicle_itineraries[vehicle_id].append(order) # Add to vehicle itinerary

            current_time = estimated_arrival
            delivery_number += 1

        print(f"Start Time: {start_time.strftime('%I:%M %p')}")
        print("S.no\tVehicle\tSector\tDistance\tOrder#\tName\tPhone\t\tAddress\t\tDelivery")
        for entry in self.processed_entries:
            print(f"{entry['s_no']}\t{entry['vehicle']}\t{entry['sector']}\t{entry['distance']}\t{entry['order']}\t{entry['name']}\t{entry['phone']}\t{entry['address']}\t{entry['delivery_time']}")

        self.print_vehicle_itineraries(start_time)


    def assign_vehicle(self, order):
        # Placeholder: Replace with a better assignment strategy (e.g., nearest vehicle, capacity, etc.)
        # Basic Round Robin:
        vehicle_index = (self.deliveries.index(order)) % self.num_vehicles  # Use order index for RR.
        return f"V{vehicle_index + 1}"

    def calculate_delivery_time(self, distance):
        # Placeholder: Replace with a more realistic calculation (traffic, speed, etc.)
        speed = 60 if self.distance_unit == 'km' else 40  # Example speed
        return distance / speed * 60  # in minutes

    def print_vehicle_itineraries(self, start_time):
        for vehicle_id, itinerary in self.vehicle_itineraries.items():
            print(f"\n{vehicle_id} Itinerary:")
            current_time = start_time
            for order in itinerary:
                delivery_time = self.calculate_delivery_time(order['distance'])
                estimated_arrival = current_time + datetime.timedelta(minutes=delivery_time)
                current_time = estimated_arrival # Update current time.
                print(f"  Order {order['order']}: {order['address']} ({estimated_arrival.strftime('%I:%M %p')})")
            return_time = current_time + datetime.timedelta(minutes=self.base_return_time)
            print(f"  Return to Base Time: {return_time.strftime('%I:%M %p')}")

# Generate random test cases
def generate_random_orders(num_orders, distance_unit):
    sectors = ['NW', 'NE', 'SW', 'SE']
    orders = []
    for i in range(num_orders):
        order = {
            'sector': random.choice(sectors),
            'distance': random.randint(1, 10),  # Random distance
            'order': 1000 + i,  # Unique order number
            'name': f"Customer {i}",
            'phone': f"(555){random.randint(100, 999)}-{random.randint(1000, 9999)}",
            'address': f"{random.randint(100, 999)} {random.choice(['Main', 'Oak', 'Pine'])} St, OR {random.randint(97000, 97999)}"
        }
        orders.append(order)
    return orders

# Example Usage:
num_vehicles = 2
max_delay = 15 # minutes
distance_unit = 'miles'
base_return_time = 30 # minutes
delivery_system = DeliverySystem(num_vehicles, max_delay, distance_unit, base_return_time)

# Generate and process random orders:
num_test_cases = 1
for i in range(num_test_cases):
    random_orders = generate_random_orders(random.randint(5, 10), distance_unit) # Random number of orders
    print(f"\n--- Test Case {i+1} ---")
    delivery_system.optimize_deliveries(random_orders)

#generated Program Output
Using Sector-Based Delivery Algorithm (Placeholder - Needs Improvement)
Start Time: 12:46 PM
S.no	Vehicle	Sector	Distance	Order#	Name	Phone		Address		Delivery
1	V1	SE	9	1000	Customer 0	(555)517-8143	279 Oak St, OR 97844	12:59 PM
2	V2	SW	1	1001	Customer 1	(555)765-7638	691 Oak St, OR 97924	01:01 PM
3	V1	NW	10	1002	Customer 2	(555)902-5309	290 Pine St, OR 97554	01:16 PM
4	V2	NW	10	1003	Customer 3	(555)367-4571	324 Oak St, OR 97923	01:31 PM
5	V1	NE	1	1004	Customer 4	(555)127-5037	200 Main St, OR 97518	01:32 PM
6	V2	SE	6	1005	Customer 5	(555)654-2116	571 Main St, OR 97251	01:41 PM
7	V1	SW	6	1006	Customer 6	(555)232-6089	864 Pine St, OR 97808	01:50 PM
8	V2	NE	7	1007	Customer 7	(555)852-3249	138 Oak St, OR 97154	02:01 PM
9	V1	SE	9	1008	Customer 8	(555)888-2245	663 Oak St, OR 97117	02:14 PM
10	V2	NW	4	1009	Customer 9	(555)815-5990	575 Oak St, OR 97174	02:20 PM

V1 Itinerary:
  Order 1000: 279 Oak St, OR 97844 (12:59 PM)
  Order 1002: 290 Pine St, OR 97554 (01:14 PM)
  Order 1004: 200 Main St, OR 97518 (01:16 PM)
  Order 1006: 864 Pine St, OR 97808 (01:25 PM)
  Order 1008: 663 Oak St, OR 97117 (01:38 PM)
  Return to Base Time: 02:08 PM

V2 Itinerary:
  Order 1001: 691 Oak St, OR 97924 (12:47 PM)
  Order 1003: 324 Oak St, OR 97923 (01:02 PM)
  Order 1005: 571 Main St, OR 97251 (01:11 PM)
  Order 1007: 138 Oak St, OR 97154 (01:22 PM)
  Order 1009: 575 Oak St, OR 97174 (01:28 PM)
  Return to Base Time: 01:58 PM
