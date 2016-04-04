import example as e

my_data = [
    ['slashdot', 'USA', 'yes', 18, 'None'],
    ['google', 'France', 'yes', 23, 'Premium'],
    ['digg', 'USA', 'yes', 24, 'Basic'],
    ['kiwitobes', 'France', 'yes', 23, 'Basic'],
    ['google', 'UK', 'no', 21, 'Premium'],
    ['(direct)', 'New Zealand', 'no', 12, 'None'],
    ['(direct)', 'UK', 'no', 21, 'Basic'],
    ['google', 'USA', 'no', 24, 'Premium'],
    ['slashdot', 'France', 'yes', 19, 'None'],
    ['digg', 'USA', 'no', 18, 'None'],
    ['google', 'UK', 'no', 18, 'None'],
    ['kiwitobes', 'UK', 'no', 19, 'None'],
    ['digg', 'New Zealand', 'yes', 12, 'Basic'],
    ['slashdot', 'UK', 'no', 21, 'None'],
    ['google', 'UK', 'yes', 18, 'Basic'],
    ['kiwitobes', 'France', 'yes', 19, 'Basic']]

tree = e.buildtree(my_data)
e.printtree(tree)
# e.drawtree(tree)
print e.classify(['(direct)', 'USA', 'yes', 5], tree)

# e.prune(tree, 0.1)
# e.printtree(tree)
print e.mdclassify(['google', None, 'yes', None], tree)
print e.mdclassify(['google', 'France', None, None], tree)

pass
