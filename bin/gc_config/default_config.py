#!/usr/bin/env python3

# Generic Settings
## CLI default loglevel
default_log_level = 'INFO'
## CLI available loglevels
log_levels_available = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
## How often do we want to retry an auth before failing
max_auth_attempts = 3

# Events
## Loop time in seconds
loop_time = 30

## NETLOG
### Netlog events per page
netlog_page_size = 10000
### Netlog Delay from $now to ensure 100% of logs are received on the backend (time in seconds)
netlog_log_delay = 1200
### Loop time in seconds
netlog_loop_time = 30

## INCIDENT
### Incident events per page
incident_page_size= 1000
### Delay from $now to ensure 100% of logs are received on the backend (time in seconds)
incident_log_delay = 1200
### Loop time in seconds
incident_loop_time = 30

## AGENT
### Agent Status events per page
agent_page_size= 10000
### Delay from $now to ensure 100% of logs are received on the backend (time in seconds)
agent_log_delay = 600
### Loop time in seconds
agent_loop_time = 30

## System Status events per page
system_page_size= 10000
### Delay from $now to ensure 100% of logs are received on the backend (time in seconds)
system_log_delay = 600
### Loop time in seconds
system_loop_time = 30

## AUDIT config
audit_page_size = 1000
audit_log_delay = 600
audit_loop_time = 30