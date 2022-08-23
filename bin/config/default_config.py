#!/usr/bin/env python3

# Generic Settings
## CLI default loglevel
default_log_level = 'INFO'
## CLI available loglevels
log_levels_available = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
## How often do we want to retry an auth before failing
max_auth_attempts = 3


# Events
## Delay from $now to ensure 100% of logs are received on the backend (time in seconds)
log_delay = 1200
## Loop time in seconds
loop_time = 30
## Events per PAge
page_size = 10000