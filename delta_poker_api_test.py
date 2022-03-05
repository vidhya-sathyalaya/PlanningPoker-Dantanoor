import json
from gui_client_util import GUI_Helper
from fastapi import status

util = GUI_Helper()

def test_post_justification():
    issue_data = {
            'name': 'xyz',
            'justification': "Test justification"
        }
        
        
    response = util.send_request(method='put',
                                     route='/issue/justify',
                                     data=issue_data)

    assert response.status_code == 200         



def test_get_justification():
    response = util.send_request(method='get',
                                     route='/issue/justification')
    assert(response.status_code == status.HTTP_200_OK)

    if response.status_code == status.HTTP_200_OK:
            response_dict = json.loads(response.text)
            assert(response_dict['result_message']['justification'] ==  ["Test justification"])                     

test_post_justification()
test_get_justification()

