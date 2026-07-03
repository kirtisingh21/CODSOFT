print("========== FOOD RECOMMENDATION SYSTEM ==========")

budget = int(input("Enter your budget (in Rs): "))

print("Choose your taste:")
print("1. Spicy")
print("2. Sweet")
print("3. Healthy")

taste = input("Enter your choice (1-3): ")

print("Recommended Food:")

if budget < 100:
    if taste == "1":
        print("• Samosa")
        print("• Veg Roll")
    elif taste == "2":
        print("• Gulab Jamun")
        print("• Ice Cream")
    elif taste == "3":
        print("• Fruit Salad")
        print("• Vegetable Soup")
    else:
        print("Invalid Choice")
elif budget <= 300:
    if taste == "1":
        print("• Veg Biryani")
        print("• Chilli Paneer")
    elif taste == "2":
        print("• Brownie")
        print("• Pastry")
    elif taste == "3":
        print("• Grilled Sandwich")
        print("• Veg Salad")
    else:
        print("Invalid Choice")
else:
    if taste == "1":
        print("• Paneer Tikka")
        print("• Malai Chaap")
    elif taste == "2":
        print("• Cheesecake")
        print("• Chocolate Lava Cake")
    elif taste == "3":
        print("• Smoothie Bowl")
        print("• Quinoa Salad")
    else:
        print("Invalid Choice")
print("Enjoy your meal!")
                    
    
