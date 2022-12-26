from unittest import TestCase, skip

from clorm import FactBase
from clorm import monkey
monkey.patch() # must call this before importing clingo

from scott_clingo import ScottClingo
import scott_terms as terms


class LitOccupiedLocations(TestCase, ScottClingo):
    pass


class SecurityAlertLocationIsInsecure(TestCase, ScottClingo):
    pass
