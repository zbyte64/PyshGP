'''
Created on Dec 31, 2013

@author: Eddie Pantridge Hampshire College
'''
import util
import random_push
import globals

def choose_node_index_with_leaf_probability(tree, node_selection_leaf_probability):
    '''
    Returns an index into tree, choosing a leaf with probability
    node-selection-leaf-probability.
    '''
    if type(tree) == list:
        if random_push.lrand() > node_selection_leaf_probability:
            allItems = util.all_items(tree)
            itemsWithCount = []
            for i in range(len(allItems)):
                itemsWithCount.apped([allItems[i], i])
            listItems = []
            for i in itemsWithCount:
                if type(i) == list:
                    listItems.append(i)
            return(random_push.lrand_nth(listItems)[1])
    else:
        return 0
    
def choose_node_index_by_tournament(tree, node_selection_tournament_size):
    '''
    Returns an index into tree, choosing the largest subtree found in
    a tournament of size node-selection-tournament-size.
    '''
    c = util.count_points(tree)
    tournament_set = []
    for i in range(node_selection_tournament_size):
        point_index = random_push.lrand_int(c)
        subtree_size = util.count_points(util.code_at_point(tree, point_index))
        tournament_set.append({'i' : point_index, 'size' : subtree_size})
    biggest = tournament_set[0]
    for s in tournament_set:
        if biggest['size'] < s['size']:
            biggest = s
    return biggest['i']

def select_node_index(tree, keys):
    '''
    Returns an index into tree using the node selection method indicated
    by node-selection-method.
    '''
    if keys['node-selection-method'] == 'unbiased':
        return random_push.lrand_int(util.count_points(tree))
    elif keys['node-selection-method'] == 'leaf-probability':
        return choose_node_index_with_leaf_probability(tree, keys['node-selection-leaf-probability'])
    elif keys['node-selection-method'] == 'size-tournament':
        return choose_node_index_by_tournament(tree, keys['node-selection-tournament-size'])
    else:
        print 'ERROR: :node-selection-method set to unrecognized value '