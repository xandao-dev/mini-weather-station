def intOrNone(value):
	try:
		return int(value)
	except (ValueError, TypeError):
		return None
