import numpy
from PIL import Image


def selfOrganisingMap(inputs, spread, size, steps=1000):
    nRows, nCols = size
    vecLen = len(inputs[0])
    somap = numpy.random.rand(nRows, nCols, vecLen)

    influence = numpy.dstack([spread] * vecLen)  # One for each feature
    infWidth = (len(influence) - 1) // 2
    makeMesh = numpy.ix_  # Ugly

    for s in xrange(steps):

        decay = numpy.exp(-s / float(steps))

        for vector in inputs:
            diff = somap - vector
            diff2 = diff * diff
            dist2 = diff2.sum(axis=2)

            index = dist2.argmin()
            row = index // nRows
            col = index % nRows

            rows = [x % nRows for x in range(row - infWidth, row + 1 + infWidth)]
            cols = [y % nCols for y in range(col - infWidth, col + 1 + infWidth)]

            mesh = makeMesh(rows, cols)
            somap[mesh] -= diff[mesh] * influence * decay

    return somap


if __name__ == '__main__':
    import time

    # from PIL import Image

    spread = numpy.array([[0.0, 0.10, 0.2, 0.10, 0.0],
                          [0.1, 0.35, 0.5, 0.35, 0.1],
                          [0.2, 0.50, 1.0, 0.50, 0.2],
                          [0.1, 0.35, 0.5, 0.35, 0.1],
                          [0.0, 0.10, 0.2, 0.10, 0.0]])

    n_sizes = [20, 100]
    nsteps = [0, 1, 10, 100]
    with open("ex12_out.txt", mode='w') as out:
        for n_size in n_sizes:
            rows, cols = size = (n_size, n_size)
            testInput = numpy.random.rand(rows * cols, 3)
            for i_nsteps in nsteps:
                t0 = time.time()
                somap = selfOrganisingMap(testInput, spread, size, i_nsteps)
                t1 = time.time()
                out.write("for " + str(n_size) + " size " +
                          str(i_nsteps) + " iter " +
                          "time taken = %.3f" % (t1 - t0) + '\n')

                colors = somap * 255
                colors = colors.astype(numpy.uint8)
                img = Image.fromarray(colors, 'RGB')
                img.save("somap" + str(n_size) + "-" + str(i_nsteps) + ".png", 'PNG')
                # img.show()
