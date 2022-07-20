from unittest import TestCase, skip

from clorm import FactBase
from clorm import monkey
monkey.patch() # must call this before importing clingo

from utils import ClingoTest
import terms


class LitOccupiedLocations(TestCase, ClingoTest):
    pass


class SecurityAlertLocationIsInsecure(TestCase, ClingoTest):
    pass
