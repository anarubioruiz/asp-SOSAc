from clorm import Predicate, ConstantField, IntegerField

class InstanceOf(Predicate):
    instance = ConstantField
    klass = ConstantField

class SubclassOf(Predicate):
    child_klass = ConstantField
    parent_klass = ConstantField

class MemberOf(Predicate):
    instance = ConstantField
    klass = ConstantField

class TransitionTrigger(Predicate):
    id = IntegerField
    device = ConstantField
    device_state = ConstantField

class TransitionChange(Predicate):
    id = IntegerField
    target = ConstantField
    target_state = ConstantField

class PropertyValueOf(Predicate):
    property = ConstantField
    value = ConstantField
    target = ConstantField
    