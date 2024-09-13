#!/usr/bin/env python3
import sys
import time

import modules.aka_log as aka_log
import modules.generic as generic
import gc_config.default_config as default_config
import json

def get_log(given_args=None, gc_edgerc=None, config_lopp_time=None, config_log_delay=None, config_page_size=500, route='/', params=None):
    starttime = int(given_args.event_starttime) - config_log_delay - config_lopp_time
    endtime = int(given_args.event_endtime) - config_log_delay
    follow_mode = given_args.event_follow
    user_agent = given_args.gc_user_agent_prefix
    gc_authtoken = None
    auth_attempt = 0
    my_params = params

   # sys.exit()

    while True:
        aka_log.log.debug(f"Starttime: {starttime}, Endtime: {endtime}, follow mode: {follow_mode}")
        if not gc_authtoken:
            if auth_attempt == 2:
                aka_log.log.critical(f"Authentication failed - exiting.")
                sys.exit(1)
            gc_authtoken = generic.gc_get_auth_token(gc_edgerc=gc_edgerc, tls_verify=not given_args.skip_tls_validation, user_agent=user_agent)['access_token']
            my_headers = {'Authorization': f"Bearer {gc_authtoken}"}

        # Walk pages
        walk_pages = True
        my_page = 1
        while walk_pages:
            my_params['from_time'] = starttime * 1000
            my_params['to_time'] = endtime * 1000
            my_params['offset'] = (my_page - 1) * config_page_size
            my_params['limit'] = config_page_size

            if given_args.skip_tls_validation:
                aka_log.log.debug(f"Skipping TLS Validation - this is insecure")
            else:
                aka_log.log.debug(f"Using TLS Validation - well done !")
            my_result = generic.api_request(method="GET", scheme="https://", url=gc_edgerc['gc_hostname'], path=route, params=my_params, headers=my_headers, payload=None, user_agent=user_agent, tls_verify=not given_args.skip_tls_validation)

            if my_result is not False and my_result is not None:
                for line in my_result['objects']:
                    print(json.dumps(line))

                if my_result['to'] >= my_result['total_count']:
                    walk_pages = False
                my_page = my_page + 1

            else:
                aka_log.log.debug(f"Unsetting 'auth token' - trying to auth.")
                gc_authtoken = None
                auth_attempt = auth_attempt + 1
                break


        if follow_mode:
            starttime = endtime
            endtime = endtime + config_lopp_time
            time.sleep(config_lopp_time)
        else:
            break

def netlog(given_args=None, gc_edgerc=None):
    get_log(given_args,
            gc_edgerc,
            config_log_delay=default_config.netlog_log_delay,
            config_lopp_time=default_config.netlog_loop_time,
            config_page_size=default_config.netlog_page_size,
            route='/api/v3.0/connections',
            params={'sort': '-slot_start_time'} )

def incident(given_args=None, gc_edgerc=None):
    get_log(given_args,
            gc_edgerc,
            config_log_delay=default_config.incident_log_delay,
            config_lopp_time=default_config.incident_loop_time,
            config_page_size=default_config.incident_page_size,
            route='/api/v3.0/incidents',
            params={})


def agent(given_args=None, gc_edgerc=None):
    get_log(given_args,
            gc_edgerc,
            config_log_delay=default_config.incident_log_delay,
            config_lopp_time=default_config.incident_loop_time,
            config_page_size=default_config.incident_page_size,
            route='/api/v3.0/agent-status/events',
            params={'severity': 'info,warning,error'} )

def system(given_args=None, gc_edgerc=None):
    get_log(given_args,
            gc_edgerc,
            config_log_delay=default_config.incident_log_delay,
            config_lopp_time=default_config.incident_loop_time,
            config_page_size=default_config.incident_page_size,
            route='/api/v3.0/system-events',
            params={} )

def audit(given_args=None, gc_edgerc=None):
    get_log(given_args,
            gc_edgerc,
            config_log_delay=default_config.audit_log_delay,
            config_lopp_time=default_config.audit_loop_time,
            config_page_size=default_config.audit_page_size,
            route='/api/v3.0/system/audit-log',
            params={})

