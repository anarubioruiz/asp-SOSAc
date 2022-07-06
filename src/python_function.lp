#script (python)

import clingo

def concatenateStr(str1, str2, str3):
    return clingo.String("{0}_{1}_{2}".format(str1, str2, str3))
#end.
