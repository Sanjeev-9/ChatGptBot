from flask import Flask,render_template,request,jsonify
from flask_cors import CORS

import APIcode
from chat import get_response

app = Flask(__name__)
app.debug = False
app._static_folder = os.path.abspath("static/")


@app.route("/predict",methods=["POST"])
def predict():
    text = request.get_json().get("message")
    response = get_response(text)
    message = {'answer': response}
    return jsonify(message)

@app.route('/search', methods=['POST'])
def search():
    Applidetails=APIcode.applidetails().to_json(orient='records')

    response = {'status': 'success', 'Applidetails': Applidetails}
    return jsonify(response)

@app.route('/getRecord',methods=['POST'])
def get_record():
    applicationname=request.get_json()
    print(applicationname)
    record_details=APIcode.create(applicationname)
    response={'status': 'success', 'valuelist': record_details['valuelist'],'searchresult':record_details['searchresult']}
    return jsonify(response)


@app.route('/submitForm',methods=['POST'])
def submitForm():
    RawData=request.get_json()
    appliactionname=RawData["ApplicationName"]
    Data=RawData["formData"]
    print(Data)
    print(appliactionname)
    RecordCreation=APIcode.CreateRecord(Data,appliactionname)
    response = {'status': 'success', 'message': "Tracking ID of Record : {}".format(RecordCreation)}
    return jsonify(response)


if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)
