import json

with open(r'Z:\Hackathon\Input data\level1a.json') as file:
    data = json.load(file)

neighborhoods = data['neighbourhoods']
restaurant_distances = data['restaurants']['r0']['neighbourhood_distance']
vehicle_capacity = data['vehicles']['v0']['capacity']

n_neighbourhoods = len(neighborhoods)
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
output = {"v0": {}}

for idx, slot in enumerate(delivery_slots):
    output["v0"][f"path{idx+1}"] = [neighborhood.replace("nn", "n") for neighborhood in ["r0"] + slot['neighborhoods'] + ["r0"]]

output_string = json.dumps(output, separators=(',', ':'))
with open('outfile1a.json', 'w') as json_file:
    json_file.write(output_string)
print(output)
