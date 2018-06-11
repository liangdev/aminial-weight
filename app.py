#-* coding:UTF-8 -*
#!/usr/bin/env python


from flask import Flask, request, jsonify
app = Flask(__name__)


import db
import analyze


@app.route("/weight", methods=['POST'])
def add_weight():
    body = request.get_json(silent=True)
    sql = """
    insert into animal_weights
    (id,weight,weigh_date)
    values
    (null,?,?)
    """
    db.execute(sql, [body['weight'], body['weigh_date']])
    return jsonify({'success': True})


@app.route("/weight", methods=['GET'])
def get_weights():
    sql = 'select * from animal_weights'
    result = db.select_all(sql)
    print('result', result)
    return jsonify(result)


@app.route("/estimated_weight", methods=['GET'])
def get_estimated_weight():
    date = request.args.get('date')
    print('get_estimated_weight', date)
    estimate_weight = analyze.estimate_weight(date)
    return jsonify({
        'estimated_weight': estimate_weight
    })


@app.route("/animal_health", methods=['GET'])
def get_animal_health():
    health_score = analyze.animal_health()
    return jsonify({
        'health_score': health_score
    })


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5188)
