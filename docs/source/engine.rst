Engine 
===================================

TODO



Basic Engine
-------------

.. py:method:: instanceOf(Individual, Klass)

    TODO

    :param Individual: TODO
    :param Klass: TODO

    **Example**

    .. code-block:: prolog

        instanceOf(kitchen, location).
        instanceOf(motion_sensor1, motion_sensor).
        instanceOf(blind_motor1, blind_motor).

.. py:method:: memberOf(Individual, Klass)

    TODO

    :param Individual: TODO
    :param Klass: TODO
    :caption: CAPTION_TEXT

    **Example**

    .. code-block:: prolog
        :caption: memberOf.lp

        klass(animal).
        subclassOf(cat, animal).
        instanceOf(Gumball, cat).
        #show me mberOf/2 

    .. 

    .. code-block:: bash

        $ clingo --text memberOf.lp 0
        memberOf(Gumball, cat).
        memberOf(Gumball, animal).


.. py:method:: subclassOf(Klass1, Klass2)

    TODO

    :param Klass2: TODO
    :param Klass2: TODO

    **Example**

    .. code-block:: prolog

        subclassOf(motion_sensor, sensor).
        subclassOf(blind_motor, actuator).


Rules Engine
-------------


