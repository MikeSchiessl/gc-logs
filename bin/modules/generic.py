import requests



def _api_request(self, method="GET", path=None, params=None, payload=None, expected_status_list=[200]):
    try:
        my_url = self.api_url + path
        my_headers = {'DOLAPIKEY': self.api_token}
        my_request = requests.request(method=method.upper(), url=my_url, params=params, headers=my_headers,
                                      json=payload)
        # my_request = urequests.request(method=method, url=my_url, headers=my_headers, json=payload)
        ##log.debug("test")
        ##log.debug("[%s][APIREQ] - Request URL: %s" %(self.name, str(my_request.request.url)))
        if my_request.status_code in expected_status_list and my_request.text:
            return my_request.json()
        else:
            print(f"Request error (status, text):  {my_request.status_code} {my_request.text}")
            # log.critical("[" + self.name + "][APIREQ] - Request error (status, text): " + str(my_request.status_code) + " " + str(my_request.text))
            # return False
    except Exception as error:
        print(f"ERROR: {error}")