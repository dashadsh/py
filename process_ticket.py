from datetime import datetime

"""
Purpose: Transform a raw support ticket into a standardized format with additional data
"""
def process_ticket(ticket):
    # 1. Add current timestamp when ticket was processed
    # 2. Convert email to lowercase (standardization)
    # 3. Validate status (only allow: new, in_progress, resolved)
    # 4. Add email validation flag

	# Expected output:
    # [
    #     {'id': 'T3', 'priority': 'high'},
    #     {'id': 'T2', 'priority': 'medium'},
    #     {'id': 'T1', 'priority': 'low'}
    # ]

	processed = ticket.copy()
	processed['processed_at'] = datetime.now().isoformat()
	processed['customer_email'] = ticket['customer_email'].lower()

	allowed_statuses = ['new', 'in_progress', 'resolved']
	if processed['status'] not in allowed_statuses:
		processed['status'] = 'new'

	processed['is_valid_email'] = '@' in processed['customer_email']

	return processed

def main():
	raw_ticket = {
		'id': 'T123',
		'status': 'new',
		'priority': 'high',
		'customer_email': 'MAIL@mail.com'
	}
	processed_ticket = process_ticket(raw_ticket)
	print(processed_ticket)

if __name__ == '__main__':
	main()


# Explain why you're making a copy (to avoid modifying the original data)
# Mention that you're handling potential errors
# Explain why you're formatting the email (consistency in data)