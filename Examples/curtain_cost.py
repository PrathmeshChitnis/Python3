"""
User wants a curtain for his square window,
the height of his window is 24 meters, your shop charges
$0.75 / sq_cm, find the total cost of curtain for the window
and let the user know.
"""

print("Cost of the curtain is :- $0.75/sq_cm")
print("Required curtain cloth is - 24 sq_meters")
cost_per_square_meter = 0.75 * 1000
window_area = 24 ** 2
print("Total cost per sq_meter is :- " + str(cost_per_square_meter))
print("The total cost of the curtain is - " + str(cost_per_square_meter * window_area))
