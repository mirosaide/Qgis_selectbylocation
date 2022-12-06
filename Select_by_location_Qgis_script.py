from qgis.core import QgsVectorLayer, QgsProject


def towerfields():
    currentCellTowerFields = QgsFields()
    currentCellTowerFields.append(QgsField("tower_id", QVariant.Int))
    currentCellTowerFields.append(QgsField("cell_id", QVariant.Int))
    currentCellTowerFields.append(QgsField("cell_centroid_lon", QVariant.Double))
    currentCellTowerFields.append(QgsField("cell_centroid_lat", QVariant.Double))
    currentCellTowerFields.append(QgsField("tower_lon", QVariant.Double))
    currentCellTowerFields.append(QgsField("tower_lat", QVariant.Double))
    currentCellTowerFields.append(QgsField("radio", QVariant.String))
    currentCellTowerFields.append(QgsField("tower_to_cell_centroid_dist_km", QVariant.Double))
    return currentCellTowerFields
    
    
def options_save():
    crs = QgsProject.instance().crs()
    transform_context = QgsProject.instance().transformContext()
    save_options = QgsVectorFileWriter.SaveVectorOptions()
    save_options.driverName = "ESRI Shapefile"
    save_options.fileEncoding = "UTF-8"
    return save_options

def add_layers(list_layers):
    for i in list_layers:
        project.addMapLayer(i)
    return

def map_layername(layername):
    return project.mapLayersByName(layername)[0]

def vlayer_selected(layer_select,field,parameter):
    return layer_select.selectByExpression(f'"{field}" = {parameter}')
    
def update_usprovider(select_layer,update_layer):
    features = select_layer.getSelectedFeatures()
    for feature in features:
        update_layer.addFeature(feature)
    update_layer.updateExtents()

#Europe
def create_split_polygon(type,name):
    splitPolygon = QgsVectorLayer(type,name, "memory")
    splitPolygonProvider = splitPolygon.dataProvider()
    splitPolygonFeature = QgsFeature()
    splitPolygonFeature.setGeometry(QgsGeometry.fromPolygonXY([[
    QgsPointXY(-180.000000000,81.858710028),
    QgsPointXY(-180.000000000,-54.462497654),
    QgsPointXY(180.000000000,-54.462497654),
    QgsPointXY(180.000000000,81.858710028)
    ]]))
    splitPolygonProvider.addFeature(splitPolygonFeature)
    splitPolygon.updateExtents()
    return splitPolygon
  
 '''
 #Oceania
def create_split_polygon(type,name):
    splitPolygon = QgsVectorLayer(type,name, "memory")
    splitPolygonProvider = splitPolygon.dataProvider()
    splitPolygonFeature = QgsFeature()
    splitPolygonFeature.setGeometry(QgsGeometry.fromPolygonXY([[
    QgsPointXY(93.6,27.4),
    QgsPointXY(93.6,-60.1),
    QgsPointXY(185.6,-60.1),
    QgsPointXY(185.6,27.4)
    ]]))
    splitPolygonProvider.addFeature(splitPolygonFeature)
    splitPolygon.updateExtents()
    return splitPolygon
 
 #Asia
def create_split_polygon(type,name):
    splitPolygon = QgsVectorLayer(type,name, "memory")
    splitPolygonProvider = splitPolygon.dataProvider()
    splitPolygonFeature = QgsFeature()
    splitPolygonFeature.setGeometry(QgsGeometry.fromPolygonXY([[
    QgsPointXY(17,60),
    QgsPointXY(17,-15),
    QgsPointXY(154,-15),
    QgsPointXY(154,60)
    ]]))
    splitPolygonProvider.addFeature(splitPolygonFeature)
    splitPolygon.updateExtents()
    return splitPolygon
 #Africa
def create_split_polygon(type,name):
    splitPolygon = QgsVectorLayer(type,name, "memory")
    splitPolygonProvider = splitPolygon.dataProvider()
    splitPolygonFeature = QgsFeature()
    splitPolygonFeature.setGeometry(QgsGeometry.fromPolygonXY([[
    QgsPointXY(-34,41.6),
    QgsPointXY(-34,-41.8),
    QgsPointXY(66,-41.8),
    QgsPointXY(66,41.6)
    ]]))
    splitPolygonProvider.addFeature(splitPolygonFeature)
    splitPolygon.updateExtents()
    return splitPolygon
 
 #south america
 def create_split_polygon(type,name):
    splitPolygon = QgsVectorLayer(type,name, "memory")
    splitPolygonProvider = splitPolygon.dataProvider()
    splitPolygonFeature = QgsFeature()
    splitPolygonFeature.setGeometry(QgsGeometry.fromPolygonXY([[
    QgsPointXY(-102.9,16.9),
    QgsPointXY(-102.9,-61.6),
    QgsPointXY(-24.7,-61.6),
    QgsPointXY(-24.7,16.9)
    ]]))
    splitPolygonProvider.addFeature(splitPolygonFeature)
    splitPolygon.updateExtents()
    return splitPolygon 
#North america
def create_split_polygon(type,name):
    splitPolygon = QgsVectorLayer(type,name, "memory")
    splitPolygonProvider = splitPolygon.dataProvider()
    splitPolygonFeature = QgsFeature()
    splitPolygonFeature.setGeometry(QgsGeometry.fromPolygonXY([[
    QgsPointXY(-184,90),
    QgsPointXY(-184,2.7),
    QgsPointXY(0.5,2.7),
    QgsPointXY(0.5,90)
    ]]))
    splitPolygonProvider.addFeature(splitPolygonFeature)
    splitPolygon.updateExtents()
    return splitPolygon
'''


def clip(to_be_clipped,clip_mask):
    out_clip = processing.run("native:clip",{
    'INPUT': to_be_clipped,
    'OVERLAY': clip_mask,
    'OUTPUT': 'memory:'
    })
    return out_clip

def extractbylocation(to_be_extracted,extract_mask):
    extracted = processing.run("native:extractbylocation", \
    {'INPUT': to_be_extracted,'PREDICATE': 6, 'INTERSECT': extract_mask, \
    'OUTPUT': 'memory:'})
    return extracted


def create_grid(layer):
    grid_created = processing.run("native:creategrid",{
    'TYPE': 2,
    'EXTENT': layer.id(),
    'HSPACING': 20,
    'VSPACING': 20,
    'HOVERLAY': 0,
    'VOVERLAY': 0,
    'CRS': 'EPSG:4326',
    'OUTPUT': 'memory:'
    })
    return grid_created

def towers_pop():
    allCellTowers = QgsVectorLayer("Point","All cell towers","memory")
    allCellTowersProvider = allCellTowers.dataProvider()    
    allCellTowersProvider.addAttributes(towerfields())  
    allCellTowers.updateFields()
    return allCellTowers
    
def cell_var(cell):
    cid = str(cell.attribute('id'))
    cell_centroid = cell.geometry().centroid().asPoint()
    cell_centroid_lon = cell_centroid.x()
    cell_centroid_lat = cell_centroid.y()
    return cid, cell_centroid, cell_centroid_lon, cell_centroid_lat

def temp_cell(cid,cell):
    tempCell = QgsVectorLayer("Polygon","Cell " + cid, "memory")
    tempCellProvider = tempCell.dataProvider()
    tempCellProvider.addFeature(cell)
    tempCellProvider.updateExtents()
    return tempCell


def temp_cell_towers(cid,cell):
    tempCellTowers = QgsVectorLayer("Point","Cell " + cid + " towers","memory")
    tempCellTowersProvider = tempCellTowers.dataProvider()
    tempCellTowersProvider.addAttributes(towerfields())
    tempCellTowers.updateFields()
    return tempCellTowers
    
def create_gpkg_cells(list_grids,out_path):
    for cell in cells.getFeatures():
        for grid_number in list_grids:
            if cell.attribute('id') == grid_number:
                print('ID: ', cell.attribute('id'))
                print('Area: ', cell.geometry().area())
                print('Perimeter: ', cell.geometry().length())
                #print('Centroid: ', cell.geometry().centroid())
                cid,cell_centroid,cell_centroid_lon,cell_centroid_lat = cell_var(cell)
                tempCell = temp_cell(cid,cell)
                tempCellTowers = temp_cell_towers(cid,cell)
                extractedTempCellTowers = extractbylocation(to_be_extracted,tempCell)['OUTPUT']
                count = extractedTempCellTowers.featureCount()
                print('Essa é a contagem de pontos em cada célula: ',extractedTempCellTowers.featureCount())
                if extractedTempCellTowers.featureCount():
                    extractedTempCellTowersProvider = extractedTempCellTowers.dataProvider()
                    extractedTempCellTowersProvider.addAttributes(towerfields())  
                    extractedTempCellTowers.updateFields()
                    caps=extractedTempCellTowers.dataProvider().capabilities()
                    for feature in extractedTempCellTowers.getFeatures():
                        towerLoc = feature.geometry().asPoint()
                        if caps & QgsVectorDataProvider.ChangeAttributeValues:
                            measure = d.convertLengthMeasurement(d.measureLine(towerLoc, cell_centroid),QgsUnitTypes.DistanceKilometers)
                            attrs={15:feature.id(),16:grid_number,17:cell_centroid_lon,18:cell_centroid_lat,19:towerLoc.x(),20:towerLoc.y(),21:measure}
                            extractedTempCellTowers.dataProvider().changeAttributeValues({feature.id():attrs})
                    project.addMapLayer(extractedTempCellTowers)
                    path = out_path +str(grid_number).zfill(3)+'.gpkg'
                    QgsVectorFileWriter.writeAsVectorFormatV2(extractedTempCellTowers,path,QgsProject.instance().transformContext(),QgsVectorFileWriter.SaveVectorOptions())
                else:
                    print('Cell: ', grid_number, ' has no towers')
                    
    return
    






## Clearing instances and remove layers
project = QgsProject.instance()
project.removeAllMapLayers()

## inputs paths
countries_path = 'path of the world map'
ustowers_path = 'path of the mobile towers locations'
## Run layers
countries = QgsVectorLayer(countries_path, 'World countries', 'ogr')
us_towers = QgsVectorLayer(ustowers_path, 'US Cell Towers', 'ogr')
## fields to use after extraction
currentCellTowerFields = towerfields()
## save options to exportAsLayers
save_options = options_save()
## Adding Country layer
add_layers([countries])
## Creating usLayerProvider
usLayer = QgsVectorLayer("Polygon", "The US","memory")
usLayerProvider = usLayer.dataProvider()
## Mapping layer name countriesLayer and select by expression
countriesLayer = map_layername("World countries")
## Selecting layer by expression
vlayer_selected(countriesLayer,'CONTINENT','\'Europe\'')
## updating usLayerProvider
update_usprovider(countriesLayer,usLayerProvider)
## Remove Selection Country layer and remove countries
countriesLayer.removeSelection()
project.removeMapLayer(countries)
## Add UsLayer to map and rename variable to_be_clipped
project.addMapLayer(usLayer)
to_be_clipped = project.mapLayersByName('The US')[0]
## create split polygon, add to map and rename variable to clip_mask
split_polygon = create_split_polygon("Polygon", "US Mainland Split Polygon")
project.addMapLayer(split_polygon)
clip_mask = project.mapLayersByName('US Mainland Split Polygon')[0]
## clip and add main_land_us
main_land_us = clip(to_be_clipped,clip_mask)
project.addMapLayer(main_land_us['OUTPUT'])
## Remove unused layers
project.removeMapLayer(usLayer)
project.removeMapLayer(split_polygon)
## Refresh canvas
iface.zoomFull()
## Adding Us Towers to map
project.addMapLayer(us_towers)
## Extract towers by location and add to canvas
to_be_extracted = us_towers
project.mapLayersByName('output')[0].setName('US Mainland')
extract_mask = project.mapLayersByName('US Mainland')[0]
mainLandTowers = extractbylocation(to_be_extracted,extract_mask)
project.addMapLayer(mainLandTowers['OUTPUT'])
project.mapLayersByName('output')[0].setName('US Mainland Cell Towers')
## Creating grid layer, add in canvas and define variable
us_mainland = project.mapLayersByName("US Mainland")[0]
createdGrid = create_grid(us_mainland)
project.addMapLayer(createdGrid['OUTPUT'])
project.mapLayersByName('output')[0].setName('Grid cells')
cells = project.mapLayersByName('Grid cells')[0]
## Creating towers layer to be populate
allCellTowers = towers_pop()
## Creating variable to be extracted
us_mainland_towers = project.mapLayersByName('US Mainland Cell Towers')[0]
to_be_extracted = us_mainland_towers
## Extracting points for each cell and saving as geopackage considering a range
list_grids = range(1,34)
d = QgsDistanceArea()
d.setEllipsoid('WGS84')
out_path = 'output path of the data'
create_gpkg_cells(list_grids,out_path)



def create_csv(folder):
    for root, directory, files in os.walk(folder):
        for file in files:
            if file.endswith('.gpkg'):
                layer = QgsVectorLayer(os.path.join(folder, file), "geo", "ogr")
                QgsVectorFileWriter.writeAsVectorFormat(layer, folder+file[:-5]+'.csv',
                "utf-8", driverName = "csv", layerOptions = ['GEOMETRY=AS_XYZ'])
    
    return
   
    

folder = 'output path of the folder'


create_csv(folder)


