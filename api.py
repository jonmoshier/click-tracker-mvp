import time
from flask import Flask, jsonify, request, Response
app = Flask(__name__)

eventDict = {}
click='click'
impression='impression'

@app.route('/analytics', methods=['GET','POST'])
def analytics():
    if request.method == 'POST':
        timestamp, user_id, event = int(request.args.get('timestamp')), request.args.get('user'), request.args.get('event')
        addDataToDictionary(user_id, timestamp, event)
        return Response(status=204)
    
    if request.method == 'GET':
        timestamp = int(request.args.get('timestamp'))
        result=getDataFromDictionary(timestamp) #list of tuples
        unique_user_count=len(set([(k) for k,v in result]))
        clicks_count=len([(v) for k,v in result if v == click])
        impressions_count=len([(v) for k,v in result if v == impression])
        return jsonify( unique_user=unique_user_count,
                        clicks=clicks_count,
                        impressions=impressions_count)

def addDataToDictionary(user_id, timestamp, event):
    key=getTimeKey(timestamp)
    if key not in eventDict:
        eventDict[key] = [(user_id, event),]
    else:
        eventDict[key].append((user_id, event))

def getDataFromDictionary(timestamp):
    key=getTimeKey(timestamp)
    if key not in eventDict:
        return []
    return eventDict[key]
    
def getTimeKey(timestamp):
    # various checks for valid timestamp should go here
    t=time.gmtime(int(timestamp))
    return "{}{}{}{}".format(t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour)

if __name__ == '__main__':
    app.run(debug=True)
