# Function to calculate hourly pay with overtime
def calculate_hourly_pay(hours_worked, hourly_rate):
    """
    Calculate hourly pay for an employee, considering overtime.

    Args:
        hours_worked (float): Number of hours worked.
        hourly_rate (float): Hourly rate of pay.

    Returns:
        float: Hourly pay amount.
    """
    if hours_worked <= 40:
        # Regular pay without overtime
        amount = hourly_rate * hours_worked
    else:
        # Pay with overtime
        regular_hours = 40
        overtime_hours = hours_worked - regular_hours
        overtime_rate = 1.5 * hourly_rate
        amount = (hourly_rate * regular_hours) + (overtime_hours * overtime_hours)
    
    return amount

# Example usage
hours_worked_user1 = float(input("Enter hours worked : "))
hourly_rate_user1 = float(input("Enter hourly rate : "))

hours_worked_user2 = float(input("Enter hours worked : "))
hourly_rate_user2 = float(input("Enter hourly rate : "))

# Call the function to calculate hourly pay
hourly_pay_user1 = calculate_hourly_pay(hours_worked_user1, hourly_rate_user1)
hourly_pay_user2 = calculate_hourly_pay(hours_worked_user2, hourly_rate_user2)

# Display the result
print("Hourly pay for User 1: $", hourly_pay_user1)
print("Hourly pay for User 2: $", hourly_pay_user2)


print("Pay: $", calculate_hourly_pay())
print("Pay: $", calculate_hourly_pay (50))
print("Pay: $", calculate_hourly_pay (hourly_rate = 60))
print("Pay: $", calculate_hourly_pay (hourly_rate = 60, hours_worked = 90))

