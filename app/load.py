import os
from django.contrib.gis.utils import LayerMapping

from geoapp.models import Establecimiento, Escuelas

# Auto-generated `LayerMapping` dictionary for Establecimiento model
establecimiento_mapping = {
    'gml_id': 'gml_id',
    'id_est': 'ID',
    'tipo': 'TIPO',
    'tipo_descr': 'TIPO_DESCR',
    'nombre_est': 'NOMBRE_EST',
    'lat_est': 'LAT',
    'long_est': 'LONG',
    'codigo_sni': 'CODIGO_SNI',
    'geom': 'POINT',
}

establecimiento_shp = os.path.abspath(os.path.join('data', 'establecimientos.shp'))

def run(verbose=True):
    lm = LayerMapping(Establecimiento, establecimiento_shp, establecimiento_mapping)
    lm.save(strict=True, verbose=verbose)

# Auto-generated `LayerMapping` dictionary for Escuelas model
escuelas_mapping = {
    'gml_id': 'gml_id',
    'codigo': 'CODIGO',
    'nom_dep': 'NOM_DEP',
    'nom_prov': 'NOM_PROV',
    'cat_sec': 'CAT_SEC',
    'nom_mun': 'NOM_MUN',
    'observacio': 'OBSERVACIO',
    'cod_le': 'COD_LE',
    'cantue': 'CANTUE',
    'point_x': 'POINT_X',
    'point_y': 'POINT_Y',
    'cod_prin': 'COD_PRIN',
    'nom_prin': 'NOM_PRIN',
    'cod_sie': 'COD_SIE',
    'establecim': 'ESTABLECIM',
    'geom': 'POINT',
}

escuelas_shp = os.path.abspath(os.path.join('data', 'EstabEducativos.shp'))

def run_escuelas(verbose=True):
    lm = LayerMapping(Escuelas, escuelas_shp, escuelas_mapping)
    lm.save(strict=True, verbose=verbose)