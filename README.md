# Qgis_selectbylocation

With this python script, I demonstrated how to perform select by location of mobile towers for a given grid.

As input the user must use a shapefile (.shp) of the world map and as the second input the user must use a .gpkg file that corresponds to the world dwide mobile towers location.

First, the script divides a given continent into grids of a chosen shape and size - for this example it was a square shape with 20 by 20 degrees of dimensions. After that, you can select mobile towers that are within each grid and save it into a CSV file.

In order to run the code, one must first download the data from OpenCellid, then process it into QGis (must the version 3.24 or above) to transform the data into a file with the (.gpkg) extension. Once the path of the data is set properly the script will run properly.
Computational resources are also needed -  core i5 or above, RAM of 8 GB or Above, and storage of 100 GB or above. I would also advise to run in on Linux rather than windows.

Once the script outputs data, then the user can set the path of this data to the second script in the Jupyter notebook (Sum integrated power) file.
