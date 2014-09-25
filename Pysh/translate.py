'''
Created on Sep 18, 2014

@author: Eddie Pantridge, Hampshire College F2012
'''
import util
import Pysh.instructions.common

def delete_prev_paren_pair(prog):
    '''
     Deletes the last closed paren pair from prog, which may be a partial program.
    '''
    reversed_prog = prog[::-1]
    new_prog = []
    number_close_parens = 0
    found_first_close = False
    looping = True
    while looping:
        #Check if reversed-prog is empty, in which case we are done
        if len(reversed_prog) == 0:
            return new_prog[::-1]
        #Check if done, which is if we've found the first :close, the paren-stack is empty, and the first item in reversed-prog is :open
        elif found_first_close and number_close_parens == 0 and reversed_prog[0] == ':open':
            temp = new_prog + reversed_prog[1:]
            return temp[::-1]
        #Check if looking for the correct :open but found an :open for a different paren
        elif found_first_close and 0 < number_close_parens and reversed_prog[0] == ':open':
            reversed_prog = reversed_prog[1:]
            new_prog = new_prog + [reversed_prog[0]]
            number_close_parens -= 1
        #Check if looking for correct :open but found another :close
        elif found_first_close and reversed_prog[0] == ':close':
            reversed_prog = reversed_prog[1:]
            new_prog = new_prog + [reversed_prog[0]]
            number_close_parens += 1
        #Check if just found first :close. In which case skip it and set the found-first-close flag
        elif not found_first_close and reversed_prog[0] == ':close':
            reversed_prog = reversed_prog[1:]
            number_close_parens = 0
            found_first_close = True
        #Otherwise, just put the item onto new-prog and keep looking with same other variables
        else:
            reversed_prog = reversed_prog[1:]
            new_prog = new_prog + [reversed_prog[0]]
            
def translate_plush_genome_to_push_program(argmap):
    '''
    Takes as input an individual (or map) containing a Plush genome (:genome)
    and translates it to the correct Push program with
    balanced parens. The linear Plush genome is made up of a list of instruction
    maps, each including an :instruction key as well as other epigenetic marker
    keys. As the linear Plush genome is traversed, each instruction that requires
    parens will push :close and/or :close-open onto the paren-stack, and will
    also put an open paren after it in the program. For example, an instruction
    that requires 3 paren groupings will push :close, then :close-open, then :close-open.
    When a positive number is encountered in the :close key of the
    instruction map, it is set to num-parens-here during the next recur. This
    indicates the number of parens to put here, if need is indicated on the
    paren-stack. If the top item of the paren-stack is :close, a close paren
    will be inserted. If the top item is :close-open, a close paren followed by
    an open paren will be inserted.
    If the end of the program is reached but parens are still needed (as indicated by
    the paren-stack), parens are added until the paren-stack is empty.
    Instruction maps that have :silence set to true will be ignored entirely.
    '''
    if argmap['program'] != None:
        return argmap['program']
    else:
        prog = []
        gn = argmap['genome']
        num_parens_here = 0
        paren_stack = []
        
        while(True):
            # Check if need to add close parens here
            if 0 < num_parens_here:
                if paren_stack[0] == ':close':
                    prog = prog + [':close']
                elif paren_stack[0] == ':close-open':
                    prog = prog + [':close']
                    prog = prog + [':open']
                num_parens_here -= 1
                paren_stack[1:]
            # Check if at end of program but still need to add parens
            elif len(gn) == 0 and len(paren_stack) > 0:
                num_parens_here = len(paren_stack)
            # Check if done
            elif len(gn) == 0:
                util.open_close_sequence_to_list(prog)
            # If here, ready for next instruction
            else:
                number_parens_group