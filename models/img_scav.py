import os
import json
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    iam_apikey='ejliqAzwzws4ICSiOthvI0MSUmal-R00BmistPaYAV50')
def check_class(filename):
    PATH = os.getcwd() + '/assets/'+filename+'.jpg'
    print(PATH)
    with open(PATH, 'rb') as images_file:
        classes = visual_recognition.classify(
            images_file,
            threshold='0.6',
        classifier_ids='Boomba_v0_1140204870').get_result()
    #print(json.dumps(classes, indent=2))
    return classes['images'][0]['classifiers'][0]['classes'][0]