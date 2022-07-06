from clorm import Predicate, ConstantField

class InstanceOf(Predicate):
    instance = ConstantField
    klass = ConstantField

class SubclassOf(Predicate):
    child_klass = ConstantField
    parent_klass = ConstantField

class MemberOf(Predicate):
    instance = ConstantField
    klass = ConstantField
