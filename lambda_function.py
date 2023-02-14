import tflite_runtime.interpreter as tflite
from keras_image_helper import create_preprocessor

# preprocess
preprocessor = create_preprocessor('resnet50', target_size=(224, 224))

# tf-lite interpreters
interpreter = tflite.Interpreter(model_path='kitchenware-model.tflite')
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']


classes = [
    'cup',
    'fork',
    'glass',
    'knife',
    'plate',
    'spoon']

# url = 'https://images.unsplash.com/photo-1578679664605-80268ff31300?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MjB8fGZvcmt8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60'

def predict(url):
    X = preprocessor.from_url(url)

    interpreter.set_tensor(input_index, X)
    interpreter.invoke()
    preds = interpreter.get_tensor(output_index)

    float_predictions = preds[0].tolist()

    return dict(zip(classes, float_predictions))


def lambda_handler(event, context):
    url = event['url']
    result = predict(url)
    return result