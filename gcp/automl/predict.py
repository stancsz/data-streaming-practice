"""
service account
https://cloud.google.com/vision/automl/object-detection/docs/before-you-begin?_ga=2.120276168.-1787115836.1599186329


usage
```
$ python predict.py YOUR_LOCAL_IMAGE_FILE 528868274275 ICN3389119248293953536
```

# REST API Equivalent
request.json
```
{
  "payload": {
    "image": {
      "imageBytes": "YOUR_BASE64_ENCODED_IMAGE_BYTES"
    }
  }
}
```

# Execute the request
```
curl -X POST -H "Content-Type: application/json" \
  -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
  https://automl.googleapis.com/v1beta1/projects/528868274275/locations/us-central1/models/ICN3389119248293953536:predict \
  -d @request.json
```

"""

import sys

from google.cloud import automl_v1beta1
from google.cloud.automl_v1beta1.proto import service_pb2


# 'content' is base-64-encoded image data.
def get_prediction(content, project_id, model_id):
  prediction_client = automl_v1beta1.PredictionServiceClient()

  name = 'projects/{}/locations/us-central1/models/{}'.format(project_id, model_id)
  payload = {'image': {'image_bytes': content }}
  params = {}
  request = prediction_client.predict(name, payload, params)
  return request  # waits till request is returned

if __name__ == '__main__':
  file_path = sys.argv[1]
  project_id = sys.argv[2]
  model_id = sys.argv[3]

  with open(file_path, 'rb') as ff:
    content = ff.read()

  print get_prediction(content, project_id, model_id)