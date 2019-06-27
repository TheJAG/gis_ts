import json
import urllib.request


class ProrailReader:
    def __init__(self):
        # base_uri = 'https://mapservices.prorail.nl/arcgis/rest/services/Spoortakken_001/MapServer/4'
        url = 'https://mapservices.prorail.nl/arcgis/rest/services/Spoortakken_001/MapServer/4/query?objectIds=1&f=pjson'
        response = urllib.request.urlopen(url).read()
        result_dict = json.loads(response)
        print(result_dict)


# {
#  "cells": [
#   {
#    "cell_type": "code",
#    "execution_count": 10,
#    "metadata": {
#     "collapsed": true,
#     "show_input": true
#    },
#    "outputs": [],
#    "source": [
#     "import urllib2\n",
#     "import json\n",
#     "import time"
#    ]
#   },
#   {
#    "cell_type": "code",
#    "execution_count": 11,
#    "metadata": {
#     "collapsed": false,
#     "show_input": true
#    },
#    "outputs": [
#     {
#      "name": "stdout",
#      "output_type": "stream",
#      "text": [
#       "{u'features': [{u'geometry': {u'paths': [[[184625.17599999905, 339986.8295999989], [184626.70100000128, 339987.26999999955], [184630.61300000176, 339988.2280000001], [184633.74500000104, 339988.85599999875], [184640.16299999878, 339989.87099999934], [184643.83799999952, 339990.3440000005], [184652.84200000018, 339991.15399999917], [184688.37799999863, 339993.5179999992], [184694.62200000137, 339994.0520000011], [184708.73699999973, 339995.4530000016], [184714.52800000086, 339996.1810000017], [184737.9609999992, 339999.43200000003], [184746.65199999884, 340000.55999999866], [184774.1160000004, 340004.37900000066], [184800.3280000016, 340008.4389999993], [184810.04300000146, 340010.15399999917], [184821.92799999937, 340012.438000001], [184839.12900000066, 340015.9780000001], [184856.28700000048, 340019.7170000002], [184868.97899999842, 340022.6860000007], [184880.4200000018, 340025.6409999989], [184892.26399999857, 340028.83199999854], [184945.35700000077, 340043.65100000054]]]}, u'attributes': {u'VERSIE': u'02'}}], u'fieldAliases': {u'VERSIE': u'VERSIE'}, u'fields': [{u'alias': u'VERSIE', u'length': 5, u'type': u'esriFieldTypeString', u'name': u'VERSIE'}], u'displayFieldName': u'VERSIE', u'spatialReference': {u'wkid': 28992, u'latestWkid': 28992}, u'geometryType': u'esriGeometryPolyline'}\n"
#      ]
#     }
#    ],
#    "source": [
#     "base_uri = 'https://mapservices.prorail.nl/arcgis/rest/services/Spoortakken_001/MapServer/4'\n",
#     "\n",
#     "url = 'https://mapservices.prorail.nl/arcgis/rest/services/Spoortakken_001/MapServer/4/query?objectIds=1&f=pjson'\n",
#     "response = urllib2.urlopen(url).read()\n",
#     "result_dict = json.loads(response)\n",
#     "print(result_dict)\n"
#    ]
#   },
#   {
#    "cell_type": "code",
#    "execution_count": 12,
#    "metadata": {
#     "collapsed": false,
#     "show_input": true
#    },
#    "outputs": [
#     {
#      "name": "stdout",
#      "output_type": "stream",
#      "text": [
#       "3\n"
#      ]
#     }
#    ],
#    "source": [
#     "max_records = 1000\n",
#     "total = 3000\n",
#     "chunks = total / max_records\n",
#     "print(chunks)"
#    ]
#   },
#   {
#    "cell_type": "code",
#    "execution_count": 15,
#    "metadata": {
#     "collapsed": false,
#     "show_input": true
#    },
#    "outputs": [
#     {
#      "name": "stdout",
#      "output_type": "stream",
#      "text": [
#       "1000\n",
#       "1000\n",
#       "1000\n"
#      ]
#     }
#    ],
#    "source": [
#     "f = open(\"d:/temp/guru99.txt\",\"w+\")\n",
#     "\n",
#     "for count in range(0, chunks):\n",
#     "    url = \"https://mapservices.prorail.nl/arcgis/rest/services/Spoortakken_001/MapServer/4/query?where=ID>{}&text=&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&relationParam=&outFields=&returnGeometry=true&returnTrueCurves=true&maxAllowableOffset=&geometryPrecision=&outSR=&returnIdsOnly=false&returnCountOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&gdbVersion=&returnDistinctValues=false&resultOffset=&resultRecordCount=&f=pjson\".format(str(count * 1000))\n",
#     "    response = urllib2.urlopen(url).read()\n",
#     "    result_dict = json.loads(response)\n",
#     "    f.write(str(result_dict['features']))\n",
#     "    print(len(result_dict['features']))\n",
#     "\n",
#     "#(0..chunks).each do |c|\n",
#     "#  x = base_uri + 'where=objectIds>' + (c * 1000).to_s + '&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&relationParam=&outFields=&returnGeometry=true&returnTrueCurves=false&maxAllowableOffset=&geometryPrecision=&outSR=&returnIdsOnly=false&returnCountOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&gdbVersion=&returnDistinctValues=false&resultOffset=&resultRecordCount=&f=pjson'\n",
#     "#  y = URI.escape(x)\n",
#     "#  uri = URI(y)\n",
#     "#  http = Net::HTTP.new(uri.host, uri.port)\n",
#     "#  req = Net::HTTP::Get.new(uri.request_uri)\n",
#     "#  res = http.request(req)\n",
#     "#  IO.write('layer5_' + (c + 1).to_s + '.geojson', res.body)\n",
#     "#end"
#    ]
#   },
#   {
#    "cell_type": "code",
#    "execution_count": null,
#    "metadata": {
#     "collapsed": true,
#     "show_input": true
#    },
#    "outputs": [],
#    "source": []
#   }
#  ],
#  "metadata": {
#   "kernelspec": {
#    "display_name": "Python 2",
#    "language": "python",
#    "name": "python2"
#   },
#   "language_info": {
#    "codemirror_mode": {
#     "name": "ipython",
#     "version": 2
#    },
#    "file_extension": ".py",
#    "mimetype": "text/x-python",
#    "name": "python",
#    "nbconvert_exporter": "python",
#    "pygments_lexer": "ipython2",
#    "version": "2.7.14"
#   }
#  },
#  "nbformat": 4,
#  "nbformat_minor": 0
# }
