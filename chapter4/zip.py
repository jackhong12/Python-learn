# zip stops when the shortest sequence is done

days = ['Monday', 'Tuesday', 'Wendesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']

for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day, '-', fruit, '-', drink, '-', dessert) 
