import example as e

colors = [
    [1, 0, 0, 'warm'],
    [0, 1, 0, 'cool'],
    [0, 0, 1, 'cool'],
    [0, 1, 1, 'cool'],
    [1, 1, 0, 'warm'],
    [1, 0, 1, 'warm'],
    [0, 0, 0, 'cool'],
    [0.5, 0.5, 0.5, 'cool'],
    [1, 1, 1, 'cool'],
    [1, 1, 0.5, 'warm'],
    [0.5, 0, 0, 'warm'],
    [1, 0.5, 0.5, 'warm'],
]

tree = e.buildtree(colors)
e.printtree(tree)
e.drawtree(tree, "ex1_original_tree.jpg")

e.prune(tree, 0.1)
e.printtree(tree)
e.drawtree(tree, "ex1_prune_tree.jpg")
