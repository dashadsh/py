"""
Purpose: Find all tickets marked as 'resolved' and count them
"""
def filter_resolved_tickets(tickets):
    # # 1. Count how many tickets are resolved
    # # 2. Collect IDs of resolved tickets
    
    # # Expected output:
    # result = {
    #     'count': 2,  # Found 2 resolved tickets
    #     'ticket_ids': ['T2', 'T3']  # Their IDs
    # }

	# result = {}
	# result['count'] = 0
	# result['ticket_ids'] = []
	result = {
        'count': 0,
        'ticket_ids': []
    }

	for ticket in tickets:
		if ticket.get('status') == 'resolved': # safety for missing keys
		#if ticket['status'] == 'resolved':
			result['count'] += 1
			result['ticket_ids'].append(ticket['id'])

	return result

def main():
	tickets = [
		{'id': 'T1', 'status': 'new'},
		{'id': 'T2', 'status': 'resolved'},
		{'id': 'T3', 'status': 'resolved'},
		{'id': 'T4', 'status': 'in_progress'}
	]

	result = filter_resolved_tickets(tickets)
	print(result)

if __name__ == '__main__':
	main()

# Explain why you're using .get() (safety for missing keys)
# Mention that you're only storing IDs to save memory