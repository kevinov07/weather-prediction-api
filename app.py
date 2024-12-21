
from flask import Flask, request 
from flask_restful import Resource, Api
import keras
import matplotlib.pyplot as plt
from skimage.transform import resize
import numpy as np

app = Flask(__name__)
api = Api(app)

model = keras.models.load_model('modelo.h5')

class_labels = {
    0: "dew",
    1: "fogsmog",
    2: "frost",
    3: "glaze",
    4: "hail",
    5: "lightning",
    6: "rain",
    7: "rainbow",
    8: "rime",
    9: "sandstorm",
    10: "snow"
}


class root(Resource):
  
  def get(self):
    return {'message': 'Welcome to weather predition API'}, 200
  
  def post(self):
    return {'message': 'Welcome to weather predition API'}, 200

class predict(Resource):
  def get(self):
    dato = request.args.get('dato')
    if dato is None:
      return {'message': 'no image has been sent'}, 400
    else:
      return {'message': 'image sent successfully: {}'.format(dato)}, 200
    
  def post(self):
    print('entra')
    file = request.files['image']
    if file is None:
      return {'message': 'no image has been sent'}, 400
    else:
      img = plt.imread(file)
      img = resize(img, (200, 200))
      probabilities = model.predict(img.reshape(1, 200, 200, 3))[0]
      class_index = probabilities.argmax()
      class_name = class_labels.get(class_index, 'Unknown')
      return {'result': f'The class is: {class_name}',
              'probabilities': f'Probabilities: {probabilities.tolist()}'
              }, 200
    
api.add_resource(root, '/')
api.add_resource(predict, '/predict')



if __name__ == '__main__':
  app.run(debug=True)

