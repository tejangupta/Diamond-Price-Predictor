from flask import Flask, request, render_template, jsonify
from diamond.pipeline.prediction import CustomData, PredictionPipeline
from diamond import logger
import os

application = Flask(__name__)
app = application


@app.route('/', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        data = CustomData(
            carat=float(request.form.get('carat')),
            depth=float(request.form.get('depth')),
            table=float(request.form.get('table')),
            x=float(request.form.get('x')),
            y=float(request.form.get('y')),
            z=float(request.form.get('z')),
            cut=request.form.get('cut'),
            color=request.form.get('color'),
            clarity=request.form.get('clarity')
        )

        final_new_data = data.get_data_as_dataframe()
        predict_pipeline = PredictionPipeline()

        logger.info('Starting prediction...')
        pred = predict_pipeline.predict(final_new_data)
        logger.info('Prediction completed.')

        estimated_price = round(pred[0], 2)
        logger.info(f'Estimated Price: {estimated_price}')

        return jsonify(estimated_price)


@app.route('/train')
def training():
    os.system('python main.py')
    return render_template('results.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
