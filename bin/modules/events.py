#!/usr/bin/env python3
import time

import modules.aka_log as aka_log
import modules.generic as generic
import config.default_config as default_config


def netlog(given_args=None, gc_edgerc=None):
    starttime = given_args.event_starttime
    endtime = given_args.event_endtime
    follow_mode = given_args.event_follow
    user_agent = given_args.gc_user_agent_prefix
    gc_authtoken = None



    while True:
        aka_log.log.debug(f"Netlog starttime: {starttime}, Endtime: {endtime}, follow mode: {follow_mode}")
        if not gc_authtoken:
            gc_authtoken = generic.gc_get_auth_token(gc_edgerc=gc_edgerc)['access_token']
            my_headers = {'Authorization': f"bearer {gc_authtoken}"}

        # Walk pages
        walk_pages = True
        my_page = 1
        while walk_pages:

            my_params = {
                'from_time': starttime * 1000,
                'to_time': endtime * 1000,
                'sort': '-slot_start_time',
                'offset': (my_page - 1) * default_config.page_size,
                'limit': default_config.page_size
            }


            my_result = generic.api_request(method="GET", scheme="https://", url=gc_edgerc['gc_hostname'], path='/api/v3.0/connections', params=my_params, headers=my_headers, payload=None, user_agent=user_agent)

            for line in my_result['objects']:
                print(line)

            if my_result['to'] >= my_result['total_count']:
                walk_pages = False
            my_page = my_page + 1


        if follow_mode:
            starttime = endtime
            endtime = endtime + default_config.loop_time
            time.sleep(default_config.loop_time)
        else:
            break
