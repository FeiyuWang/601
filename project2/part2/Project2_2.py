import os
from google.cloud import language_v1
from Project2_1 import get_trending_tweets


credential_path = r"json file location"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path


def classify_text(text_content):
    client = language_v1.LanguageServiceClient()
    type_ = language_v1.Document.Type.PLAIN_TEXT
    language = "en"
    document = {"content": text_content, "type_": type_, "language": language}
    response = client.classify_text(request = {'document': document})
    for category in response.categories:
        print(u"Category name: {}".format(category.name))
        print(u"Confidence: {}".format(category.confidence))


classify_text(get_trending_tweets())
