"""
Purpose: Place tickets in a list based on priority (high priority first)
"""
def add_to_queue(tickets, new_ticket):
    # 1. Insert high priority tickets at the start
    # 2. Medium priority in the middle
    # 3. Low priority at the end
    
    # Expected output:
    # [
    #     {'id': 'T3', 'priority': 'high'},
    #     {'id': 'T2', 'priority': 'medium'},
    #     {'id': 'T1', 'priority': 'low'}
    # ]

	valid_priorities = ['high', 'medium', 'low']

	if new_ticket['priority'] not in valid_priorities:
		print(f"Invalid priority: {new_ticket['priority']}")
	elif new_ticket['priority'] == 'high':
		tickets.insert(0, new_ticket)
	elif new_ticket['priority'] == 'low':
		tickets.append(new_ticket)
	else:
		tickets.insert(len(tickets) // 2, new_ticket)
		
	return tickets

tickets = [
	{'id': 'T1', 'priority': 'low'},
	{'id': 'T2', 'priority': 'medium'}
	]

new_ticket = {'id': 'T3', 'priority': 'high'}

def main():
	res = add_to_queue(tickets, new_ticket)
	print(res)

if __name__ == '__main__':
	main()

# Explain the priority mapping approach
# Mention that you're handling invalid priorities
# Discuss time complexity if asked