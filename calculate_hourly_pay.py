def calculate_hourly_pay(hours_worked=0, hourly_rate=0):
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
        amount = hours_worked * hourly_rate
    else:
        # Pay with overtime
        amount = 40 * hourly_rate + (hours_worked - 40) * 1.5 * hourly_rate

    return amount

# Test the function with different scenarios
print("Pay: $", calculate_hourly_pay())                    # No arguments provided
print("Pay: $", calculate_hourly_pay(50))                  # Only hours_worked provided
print("Pay: $", calculate_hourly_pay(hourly_rate=60))       # Only hourly_rate provided
print("Pay: $", calculate_hourly_pay(hourly_rate=60, hours_worked=90))  # Both arguments provided
