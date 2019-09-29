import os
import json
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    iam_apikey='ejliqAzwzws4ICSiOthvI0MSUmal-R00BmistPaYAV50')
# check_class receives an input the name of a JPG file in /assets and returns its
# predicted category: "No_class", "MLH_table" or "Courant_paint"
def check_class(filename):
    PATH = os.getcwd() + '/assets/'+filename+'.jpg'
    print(PATH)
    with open(PATH, 'rb') as images_file:
        classes = visual_recognition.classify(
            images_file,
            threshold='0.6',
        classifier_ids='Boomba_v0_1140204870').get_result()
    out = classes['images'][0]['classifiers'][0]['classes']
    if out == []:
        return 'No_class'
    else:
        return out[0]['class']