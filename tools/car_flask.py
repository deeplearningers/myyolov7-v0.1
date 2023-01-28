import flask
from flask import request, Response, jsonify

flask_app = flask.Flask("flask_app")
@flask_app.route('/car-num', methods=["POST", "GET"])
def car_num():
    data={
        "method": "carNum",
        "numInformation": [{"fullImgPath": "/u01/img/12345_full.jpg","smallImgPath": "/u01/img/1_small.jpjg","carNum": "0_b2r8n0","smallImgPosition": [200, 200, 300, 300]},
                           {"fullImgPath": "/u01/img/12345_full.jpg","smallImgPath": "/u01/img/2_small.jpg","carNum": "0_b2r8n0","smallImgPosition": [100, 100, 300, 300]}
                           ]
    }
    print(data)
    return jsonify(data)
if __name__ == '__main__':
    flask_app.run(port=4000,host='0.0.0.0')