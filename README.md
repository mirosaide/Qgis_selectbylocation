# Qgis_selectbylocation

With this python script, I demonstrated how to perform select by location of mobile towers for a given grid.

As input the user must use a shapefile (.shp) of the world map and as the second input the user must use a .gpkg file that corresponds to the world dwide mobile towers location.

First, the script divides a given continent into grids of a chosen shape and size - for this example it was a square shape with 20 by 20 degrees of dimensions. After that, you can select mobile towers that are within each grid and save it into a CSV file.
