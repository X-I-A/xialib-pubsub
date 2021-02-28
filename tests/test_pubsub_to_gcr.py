import gzip
import time
from xialib_pubsub import PubsubGcrPublisher


def test_check():
    pub = PubsubGcrPublisher()
    assert pub.check_destination("", "mock-pubsub-gcr-zmfr66omva-ew.a.run.app")
    time.sleep(2)
    assert pub.check_destination("", "mock-pubsub-gcr-zmfr66omva-ew.a.run.app")
    assert not pub.check_destination("", "dummy-pubsub-gcr-zmfr66omva-ew.a.run.app")

def test_data():
    pub = PubsubGcrPublisher()
    header = {'topic_id': 'test-001', 'table_id': 'aged_data', 'aged': 'True',
              'data_encode': 'gzip', 'data_format': 'record', 'data_spec': 'x-i-a', 'data_store': 'body',
              'age': '1', 'start_seq': '20201113222500000000', 'meta-data': {}}
    body = gzip.compress("".encode())
    resp = pub.publish("", "mock-pubsub-gcr-zmfr66omva-ew.a.run.app", header, body)
    assert resp == "OK"
    resp = pub.publish("", "dummy-pubsub-gcr-zmfr66omva-ew.a.run.app", header, body)
    assert resp is None