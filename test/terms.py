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

class PropertyValueOf(Predicate):
    property = ConstantField
    value = ConstantField
    owner = ConstantField

class TransitionTrigger(Predicate):
    id = IntegerField
    device_klass = ConstantField
    state = ConstantField

class _TransitionTrigger(Predicate):
    id = IntegerField
    device = ConstantField
    state = ConstantField

class TransitionChange(Predicate):
    id = IntegerField
    target_klass = ConstantField
    state = ConstantField

class _TransitionChange(Predicate):
    id = IntegerField
    target = ConstantField
    state = ConstantField
