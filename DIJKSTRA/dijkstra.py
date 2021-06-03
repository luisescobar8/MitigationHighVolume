from dijkstar import Graph, find_path
from inspect import getmembers, isfunction
from flask import Flask, jsonify, request
import json
import pandas as pd

app = Flask(__name__)
graph = Graph()
@app.route("/shortestPath/", methods=['GET','POST'])
def getShortestPath():
    if request.method == 'POST':
        values = request.json
        #Agrega a la grafica los edges que existen
        for i in range(len(values['links'])):
            graph.add_edge(values['links'][i]['src'] , values['links'][i]['dst'], values['links'][i]['bw'] )
            print( "LINK SRC "+ values['links'][i]['src'] + " LINK DST "+ values['links'][i]['dst'] + " BW " + str(values['links'][i]['bw'])  )
        #switch origen a switch destino
        print( "ORIGEN ",values['edges'][0]['location'] ,"DESTINO ", values['edges'][1]['location'] )
        result = find_path(graph, values['edges'][0]['location'] , values['edges'][1]['location']  )
        result = getattr( result , 'nodes'   )
        jsonStr = json.dumps(result)
        print( result  )
        #df = pd.DataFrame.from_dict(values, orient='index')        
        return jsonStr, 202
    #return jsonify( find_path(graph,params['Source'], params['Destination'])), 202

if __name__ == "__main__":
	#getShortestPath()
	app.run(debug=True, host='0.0.0.0', port = 8081)

#A 1
#B 2
#C 3
#D 4
#E 5
#F 6
# print( " Nodes ", getattr( find_path(graph,"A", "E") , 'nodes'   )    )
# print( " Edges ", getattr( find_path(graph,"A", "E") , 'edges'   )    )
# print( "  Costs ", getattr( find_path(graph,"A", "E") , 'costs'   )    )
# print( "  Total costs ", getattr( find_path(graph,"A", "E") , 'total_cost'   )    )
# print(getmembers(find_path, isfunction))

    #    tags = []
    #     for tag in values:
    #         tags.append(tag)

    #     # print each tag name e your content
    #     for i in range(len(tags)):
    #         print(tags[i] + ': ' + str(values[tags[i]]))

    # graph.add_edge("A", "B", 10)
    # graph.add_edge("A", "C", 15)
    # graph.add_edge("B", "D", 12)
    # graph.add_edge("B", "F", 15)
    # graph.add_edge("C", "E", 10)
    # graph.add_edge("D", "E", 2)
    # graph.add_edge("D", "F", 1)
    # graph.add_edge("F", "E", 5)
    #print( find_path(graph,"A", "E")   )