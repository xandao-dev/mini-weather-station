import gc
from machine import Timer
from libs.constants import MEM_CLEAN_INTERVAL

def int_or_none(value):
	try:
		return int(value)
	except (ValueError, TypeError):
		return None


def mem_clean_routine():
	def clean():
		free_mem = gc.mem_free()
		gc.collect()
		free_mem_after = gc.mem_free()
		print(f"MCR: Memory cleaned, before: {free_mem}, after: {free_mem_after}")

	Timer(-1).init(period=MEM_CLEAN_INTERVAL, mode=Timer.PERIODIC, callback=clean)