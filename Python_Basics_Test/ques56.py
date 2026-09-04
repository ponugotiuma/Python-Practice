#Write a Python program to calculate compound growth of monthly users for one year using a given growth rate.
initial_users = 10000
monthly_growth_rate = 0.05  
months = 12

current_users = initial_users

print(f"Starting Users: {initial_users:,}\n")
print(f"{'Month':<10}{'Users':<15}{'Growth This Month':<20}")
print("-" * 45)

for month in range(1, months + 1):
    growth = current_users * monthly_growth_rate
    current_users += growth
    print(f"Month {month:<4}{round(current_users):<15,}{round(growth):<20,}")

print("-" * 45)
print(f"Final Users after {months} months: {round(current_users):,}")
total_growth = current_users - initial_users
growth_percentage = (total_growth / initial_users) * 100
print(f"Total Growth: {round(total_growth):,} users ({growth_percentage:.2f}%)")
