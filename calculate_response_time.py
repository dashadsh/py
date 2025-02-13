from datetime import datetime
"""
Purpose: Calculate how long it took to respond to a customer ticket (in minutes)
"""
def calculate_response_time(created_at, responded_at):
    # What we need to do:
    # 1. Convert time strings to datetime objects
    # 2. Calculate time difference
    # 3. Convert difference to minutes
    
    # Expected output:
    # 30 (because 30 minutes between 2:00 PM and 2:30 PM)
	try:
		# Convert strings to datetime objects
		created = datetime.fromisoformat(created_at)
		responded = datetime.fromisoformat(responded_at)
		time_diff = responded-created
		# Convert the time difference to minutes
		# https://docs.python.org/3/library/datetime.html#datetime.timedelta.total_seconds
		minutes = time_diff.total_seconds() / 60  # total_seconds() returns the difference in seconds
		return round(minutes)  # Round the result to the nearest minute
	
	except Exception as e:
		return None

def main():
	created_at = "2024-02-12T14:00:00"    # Ticket created at 2 PM
	responded_at = "2024-02-12T14:30:00"   # Response sent at 2:30 PM

	res = calculate_response_time(created_at, responded_at)
	print(res)

if __name__ == '__main__':
	main()
# Explain why you're using try/except (handling invalid datetime strings)
# Mention why you're rounding the result