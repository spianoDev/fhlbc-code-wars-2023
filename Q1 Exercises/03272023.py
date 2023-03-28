# Sam wants to know how many times the variable i gets incremented after n seconds,
# but he has no idea how to stop the loop.
#
# Help him so that the function can return i after n seconds.
#
# 0 <= n <= 3
#
# (Artifacts for the delay is allowed up to 0.5 seconds)
# NB: The value i is not so important in this kata because it is dependent on the state of server in practice.
#
# But if n==0, the expected value for i is 0.
from datetime import datetime, timedelta


def increment_loop(n):
    begin = datetime.now()
    end = begin + timedelta(seconds=(n))
    i = 0
    while end > datetime.now():
        i += 1
    print(i)
    return i


increment_loop(0.5)
