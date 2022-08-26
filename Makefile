test-unit:
	pytest-3 test/test_unit_sosa.py test/test_unit_kb.py

run:
	clingo src/*.lp 0
