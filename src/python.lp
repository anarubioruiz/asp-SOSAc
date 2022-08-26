#script (python)

import clingo
from uuid import uuid4
import base64

def gen_id():
    return clingo.String(base64.b64encode(uuid4().bytes).decode())

#end.
