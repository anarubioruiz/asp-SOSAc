clean:
	rm scenarios/*output.*

test-unit:
	pytest-3 test/test_unit_sosa.py test/test_unit_kb.py

run-example:
	clingo src/engine.lp src/sosa_engine.lp src/kb/*.lp src/example/commonsense.lp -c time=night -c remove_device=sb01

run-%:
	$(MAKE) $*.output run-graphs

%.output:
	clingo src/engine.lp src/sosa_engine.lp src/kb/*.lp scenarios/$*.lp 0 -V0 --out-atomf=%s. | head -n 1 > scenarios/output.lp

run-graphs:
	clingo src/graphs.lp scenarios/output.lp 0 --outf=2 | clingraph --out=render --type=digraph --dir scenarios/ --name-format='graph_output'

SIZE_FROM=1000
SIZE_OFFSET=100
NUM_CASES=10
OUTPUT_FILE=evaluation.csv

run-eval:
	python3 src/eval_performance.py ${SIZE_FROM} ${SIZE_OFFSET} ${NUM_CASES} ${OUTPUT_FILE}
