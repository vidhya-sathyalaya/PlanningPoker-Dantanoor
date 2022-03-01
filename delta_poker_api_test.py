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

test_post_justification()

