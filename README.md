# SOSA<sup>c</sup>-Reasoner

## What can you find in this repo?
This repository contains the implementation of the ASP engine for generating SOSA<sup>c</sup> knowledge. It comprises the following:

- The `src/` directory, housing the source code. In this directory, you can find
a) the ASP program `sosac_engine.lp`, containing the rules for basic inferences about the SOSA<sup>c</sup> restrictions and annotations;
b) the ASP program `engine.lp`, containing rules for generating the SOSA<sup>c</sup> knowledge from a scenario's specification;
c) the Python programs `sosac_clingo.py` and `sosac_terms.py`, setting up the Clingo ORM Clorm for this project;
d) the ASP program `graphs.lp`, used for generating graphs that represent the calculated solution with Clingraph;
e) the Python program `eval_performance.py`, for running a performance evaluation based on configurable parameters; and
f) the `kb/` directory, containing knowledge about how devices work.

- The `scenarios/` directory, with deployment descriptions used for validating the engine. Each scenario consists of a `.lp` file:
a) the `minimal.lp` scenario, composed of a single room and a single device (useful for easily understanding the generated knowledge for a device);
b) the `sampler.lp` scenario, which has one device of each type deployed in three different rooms (allows seeing one example of every device type modelled in the available knowledge);
c) the `casas.lp` scenario, a realistic scenario derived from one of the datasets from the Center for Advanced Studies in Adaptive Systems (CASAS); and
d) the `temp_sensors.lp` scenario, featuring two different types of temperature
sensors, demonstrating that the default feature of interest can be changed.

- The `examples/` directory, showcasing a simple example of how generated SOSA<sup>c</sup> knowledge can be used for commonsense reasoning.

- The `docs/` directory, containing the `evaluation.csv` dataset that includes the results of a large-scale performance evaluation.

In the root directory, the `Makefile` includes the rules for running the engine, the examples, and so forth.

## Try it yourself
You need to install the following Python libraries and deb packages:

```bash
$ pip install clingo
$ pip install clorm
$ pip install clingraph
$ sudo apt install graphviz
```

### Generate SOSA<sup>c</sup> knowledge for a scenario
To initiate the knowledge generation process for any of the use cases you can find at `scenarios/` (minimal, sampler, casas), execute make <scenario_name>.out. This command will create:

1. a file `scenarios/output.lp` with the ASP atoms forming the SOSA<sup>c</sup> instance of the use case, and
2. a file `scenarios/graph_output.pdf` with a graph representing the generated knowledge.

The command `make <scenario_name>.lp` only generates the knowledge file.

### Run the commonsense example
To run the commonsense example included in the `examples/` directory, execute:

```bash
make run-example
```
### Evaluate the performance
You can conduct your own performance evaluation with:

```bash
make run-eval
```
The data obtained in an evaluation performed by the repo owners can be found at `docs/evaluation.csv`

### Test the engine
To run the unit tests, execute:
```bash
make test-unit
```
