import json

with open(r'Z:\Hackathon\Input data\level1.json') as file:
    data = json.load(file)

neighbourhoods=data['neighbourhoods']
restaurant_distances=data['restaurants']['r0']['neighbourhood_distances']
vehicle_capacity=data['vehicles']['v0']['capacity']

n_neighbourhoods=len(neighbourhoods)
orders = [(f"n{i}", neighborhood['order_quantity'], neighborhood['distances']) for i, neighborhood in neighborhoods.items()]
orders.sort(key=lambda x: sum(x[2]))

def allocate_delivery_slots(orders, vehicle_capacity):
    slots = []
    current_slot = {'neighborhoods': [], 'total_distance': 0, 'total_orders': 0}

    for order in orders:
        neighborhood, order_quantity, distances = order
        if current_slot['total_orders'] + order_quantity <= vehicle_capacity:
            current_slot['neighborhoods'].append(neighborhood)
            current_slot['total_orders'] += order_quantity
            current_slot['total_distance'] = sum(distances)
        else:
            slots.append(current_slot)
            current_slot = {'neighborhoods': [neighborhood], 'total_distance': sum(distances), 'total_orders': order_quantity}

    if current_slot['neighborhoods']:
        slots.append(current_slot)

    return slots

delivery_slots = allocate_delivery_slots(orders, vehicle_capacity)

output={"v0":{}}
for idx,slot in enumerate(delivery_slots):
    output["v0"][f"path{idx+1}"]