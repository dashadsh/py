"""
Purpose: Check if an email address has valid format
"""
def is_valid_customer_email(email):
    # 1. Check if email has @
    # 2. Check if there's text before @
    # 3. Check if there's a domain after @
    # 4. Check if domain has at least one dot

    # Expected output:
    # True for valid emails
    # False for invalid emails
	if not isinstance(email, str):
		return False

	if "@" not in email or email.count("@") != 1: # otherwise will raise TypeError
		return False
	
	local, domain = email.split("@")

	if not local or not domain:
		return False
	
	if "." not in domain:
		return False
	
	return True	

def main():
    # Input examples:
	email1 = "customer@email.com"    # Valid
	email2 = "invalid.email"         # Invalid (no @)
	email3 = "@nodomain.com"         # Invalid (no username)
	email4 = "user@"                 # Invalid (no domain)
	email5 = 1

	result1 = is_valid_customer_email(email1)
	result2 = is_valid_customer_email(email2)
	result3 = is_valid_customer_email(email3)
	result4 = is_valid_customer_email(email4)
	result5 = is_valid_customer_email(email5)

	print(result1, result2, result3, result4, result5)

	# Mention this is a basic validation (real email validation is more complex)
	# Explain why you're checking for string type first

if __name__ == '__main__':
	main()