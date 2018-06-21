def convertLatLon(var):
    return str(int(var))[:2]+'.'+str(int(var))[2:4]



def getJson(inputData):
    retVal = []
    for uno in inputData:
        try:
            timestamp = uno['_source']['DATA_AGG']
            latitude = convertLatLon(uno['_source']['lat'])
            longitude = convertLatLon(uno['_source']['lng'])
            regione = uno['_source']['REGIONE']
            importo = uno['_source']['IMPORTO']
            procedura = uno['_source']['PROCEDURA']
            ribasso = uno['_source']['RIBASSO']
            elem =     {
                        'timestamp':timestamp,
                        'latitude':latitude,
                        'longitude':longitude,
                        'regione':regione,
                        'importo':importo,
                        'procedura':procedura,
                        'ribasso':ribasso,
                       }
            retVal.append(elem)
        except Exception  as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print message
    return retVal
    
    
import json
with open('una.json') as f:
    data = json.load(f)

print len(getJson(data))
