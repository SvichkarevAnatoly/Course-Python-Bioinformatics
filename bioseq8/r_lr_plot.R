set.seed(0)
xVal <- rnorm(100)
yVal <- 2.0 + -0.7 * xVal + rnorm(100, 0, 0.2)

# saving plot in png format
png(filename = 'rplot.png', width = 1000, height = 600, units = "px")
plot(xVal, yVal) # points
abline(lm(yVal ~ xVal)) # line regression
dev.off() # end add to file