#!/usr/bin/env python3

import argparse
import os
import time
import config.version as version
import config.default_config as default_config

def init():
    # Argument Parsing
    parser = argparse.ArgumentParser(description=f"{version.__tool_name_long__}",
                                     formatter_class=argparse.RawTextHelpFormatter)

    # Version Information
    parser.add_argument('-v', '--version',
                        action='store',
                        type=bool,
                        default=False,
                        nargs='?',
                        const=True,
                        help=f'Display {version.__tool_name_short__} version and operational information')

    # Loglevel
    parser.add_argument('-l', '--loglevel',
                        action='store',
                        type=str.upper,
                        default=(os.environ.get('GC_LOGLEVEL') or default_config.default_log_level),
                        choices=default_config.log_levels_available,
                        help=f'Adjust the loglevel Default: {default_config.default_log_level}')

    # EDGERC
    parser.add_argument('--edgerc',
                             action='store',
                             type=str,
                             dest="credentials_file",
                             default=(os.environ.get('GC_EDGERC') or '~/.edgerc'),
                             help="Location of the credentials file (default is ~/.edgerc)")

    # EDGERC-SECTION
    parser.add_argument('--section',
                             action='store',
                             type=str,
                             dest="credentials_file_section",
                             default=(os.environ.get('GC_SECTION') or 'default'),
                             help="Credentials file Section's name to use ('default' if not specified).")

    # USER AGENT
    parser.add_argument('--user-agent-prefix',
                        action='store',
                        type=str,
                        dest='gc_user_agent_prefix',
                        default=f"GC-CLI {version.__version__}",
                        help="Change the User Agent when making requests"
                        )

    # TLS VALIDATIONT
    parser.add_argument('--skip-tls-validation',
                        action='store',
                        dest='skip_tls_validation',
                        type=bool,
                        nargs='?',
                        const=True,
                        default=(os.environ.get('GC_SKIP_TLS_VALIDATION') or False),
                        help="Do not verify the API Servers TLS Certificate - very insecure !!!"
                        )

    # Commands
    subparsers = parser.add_subparsers(help='sub-command help')

    ## EVENTS
    parser_events = subparsers.add_parser(name="events", aliases="e", help=(f"Show {version.__tool_name_long__} events"))

    ### NETLOG
    parser_events.add_argument(dest="event_action",
                                choices=['netlog','incident','agent','system'],
                               action='store',
                               help="Show Network Events")


    parser_events.add_argument('--start',
                               action='store',
                               type=int,
                               dest='event_starttime',
                               default=int(time.time()),
                               help="Fetch events from $starttime (UNIX TIMESTAMP)")

    parser_events.add_argument('--end',
                               action='store',
                               type=int,
                               dest='event_endtime',
                               default=int(time.time()),
                               help=''"Stop event collection at $endtime (UNIX TIMESTAMP)")

    parser_events.add_argument('-f', '--follow',
                               action='store',
                               dest='event_follow',
                               type=bool,
                               nargs='?',
                               default=False,
                               const=True,
                               help="Continuously follow (tail -f) the log")

    #print(parser.parse_args())
    return parser.parse_args()



# EOF
