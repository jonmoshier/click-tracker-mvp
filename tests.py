import api
import unittest
from flask import json

multiplier=100
class TestCases(unittest.TestCase):
    def setUp(self):
        self.app = api.app.test_client()
        for i in range(0,1*multiplier):
            resp=self.app.post('/analytics?timestamp=1488433206&user=alice&event=click')
            resp=self.app.post('/analytics?timestamp=1488433206&user=alice&event=impression')
            resp=self.app.post('/analytics?timestamp=1488433206&user=bob&event=click')
            resp=self.app.post('/analytics?timestamp=1488433206&user=charles&event=click')
    def tearDown(self):
        pass
    def test_post(self):
        resp=self.app.post('/analytics?timestamp=100&user=neanderthal&event=click')
        assert resp.status_code==204
    def test_get(self):
        resp=self.app.get('/analytics?timestamp=1488433206')
        data=json.loads(resp.data.decode())
        assert data['clicks']==3*multiplier 
        assert data['impressions']==1*multiplier
        assert data['unique_user']==3
    def test_getempty(self):
        resp=self.app.get('analytics?timestamp=1488430006')
        data=json.loads(resp.data.decode())
        assert data['clicks']==0
        assert data['impressions']==0
        assert data['unique_user']==0
        
if __name__ == '__main__':
    unittest.main()
