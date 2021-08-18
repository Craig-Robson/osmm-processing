import subprocess
from os import listdir, mkdir
from os.path import isfile, join

path = '<path to folder with data in>'
grid = 'nu'

files = [f for f in listdir(join(path, grid)) if isfile(join(path,grid, f))]
print(files)

## convert .gml.gz files to shapefiles - TopographicArea Layer only

mkdir(join(path, grid, 'shp')) # create a destination folder (/shp)

for file in files:
    file_name = file.split('.')[0]
    subprocess.run(["ogr2ogr", join(path, grid, 'shp', '%s_topo.shp' %file_name), join(path, grid, '%s.gml.gz' %file_name), "TopographicArea"])

## merge files together
i = True
for file in files:
    file_name = file.split('.')[0]
    if i:
        subprocess.run(["ogr2ogr", "-f", "ESRI Shapefile", join(path, grid, 'shp', "%s_topo.shp" % grid),
                        join(path, grid, 'shp', "%s_topo.shp" % file_name)])
        i = False
    else:
        subprocess.run(
            ["ogr2ogr", "-f", "ESRI Shapefile", "-update", "-append", join(path, grid, 'shp', "%s_topo.shp" % grid),
             join(path, grid, 'shp', "%s_topo.shp" % file_name)])

