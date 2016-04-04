import example as e
import exercise1 as ex1

test_colors = [
    [1, 1, 0],
    [0.5, 0.5, 0.5],
    [0.5, 0.5, None]
]

if __name__ == '__main__':
    tree = e.buildtree(ex1.train_colors)
    e.printtree(tree)

    print
    print "for " + str(test_colors[0]) + " predicted branch with " + str(e.classify(test_colors[0], tree))
    print "for " + str(test_colors[1]) + " predicted branch with " + str(e.classify(test_colors[1], tree))
    print "for " + str(test_colors[2]) + " predicted branch with " + str(e.mdclassify(test_colors[2], tree))
