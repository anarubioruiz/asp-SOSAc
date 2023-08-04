clean:
	$(RM) scenarios/*.output.lp
	$(RM) scenarios/*.graph.pdf
	$(RM) -r .pytest_cache

docker-build:
	docker build --no-cache -t sosac-reasoner .

DOCKER_RUN=docker run -v $(shell pwd):/app -p 80:80 sosac-reasoner

docker-run:  # make docker-run CMD="make minimal.lp"
	$(DOCKER_RUN) $(CMD)

# -----------------------------------------

GRAPH_GEN_RUN=clingo src/graphs.lp
SOSAC_INFERENCE_RUN=clingo src/engine.lp src/sosac_engine.lp src/kb/*.lp

%.lp:
	$(MAKE) $*.output.lp $*.graph.pdf

%.output.lp:
	$(SOSAC_INFERENCE_RUN) scenarios/$*.lp 0 -V0 --out-atomf=%s. | head -n 1 > scenarios/$*.output.lp

%.graph.pdf:
	$(GRAPH_GEN_RUN) scenarios/$*.output.lp 0 --outf=2 | \
	clingraph --out=render --type=digraph --dir scenarios/ --name-format='$*.graph'

run-example:
	$(SOSAC_INFERENCE_RUN) examples/commonsense.lp -c time=night -c remove_device=sb01

SIZE_FROM=1
SIZE_OFFSET=100
NUM_CASES=10
ITERATIONS=5
OUTPUT_FILE=docs/from$(SIZE_FROM)offset$(SIZE_OFFSET)-$(NUM_CASES)cases$(ITERATIONS)times-evaluation.csv

run-eval: # make run-eval SIZE_FROM=1 SIZE_OFFSET=100 NUM_CASES=10 ITERATIONS=5
	python3 src/eval_performance.py \
	${SIZE_FROM} ${SIZE_OFFSET} ${NUM_CASES} ${ITERATIONS} ${OUTPUT_FILE}

test-unit:
	pytest-3 test/test_unit_sosa.py test/test_unit_kb.py
