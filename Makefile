test-unit:
	pytest-3 test/test_unit_sosa.py test/test_unit_kb.py

run:
	clingo src/engine.lp src/sosa_engine.lp src/kb/*.lp 0

run-casas:
	clingo src/engine.lp src/sosa_engine.lp src/kb/*.lp scenarios/casas.lp 0

run-sampler:
	clingo src/engine.lp src/sosa_engine.lp src/kb/*.lp scenarios/sampler.lp 0

gen_graphs:
	clingo src/graphs.lp 0 --outf=2 | clingraph --out=render --type=digraph --dir graphs

run-eval:
	cd src/; \
	python3 eval_performance.py 1 5 10 evaluation.csv
