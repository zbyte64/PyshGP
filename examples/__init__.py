import Pysh.pushgp.pyshgp
import Pysh.random_push
import Pysh.pushgp
import Pysh.interpreter

def err_func(program):
    inputs = []
    for i in len(range(100)):
        inputs.append(Pysh.random_push.lrand_int(100))
    for i in inputs:
        state = Pysh.interpreter.run_push(program,
                                          Pysh.pushstate.push_item(i, 'integer', Pysh.pushstate.make_push_state()))
        top_bool = Pysh.pushstate.top_item('boolean', state)
        if top_bool != 'no-stack-item':
            if i % 2 == top_bool:
                return 0
            else:
                return 1
        else:
            return 1000

argmap = {'use-single-thread' : True,
          'error-function' : err_func}

Pysh.pushgp.pyshgp.pushpg(argmap)