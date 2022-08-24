# gc-logs
Provide GC logs to ULS

## Usage

### Network logs
Setup the .edgerc file as described [here](#authentication)
```bash
akamai-gc events netlog --follow
```

### Incidents
Setup the .edgerc file as described [here](#authentication)
```bash
akamai-gc events incident --follow
```

### Agent Logs
Setup the .edgerc file as described [here](#authentication)
```bash
akamai-gc events agent --follow
```

### System Logs
Setup the .edgerc file as described [here](#authentication)
```bash
akamai-gc events system --follow
```

## Authentication
To use guardicore CLI, a proper authentication needs to be provided.
Therefore please create an .edgerc file or extend an already existing akamai .edgerc file with the following contents.
The default search location for the edgerc file is `~/.edgerc`. 

Please make sure you enter the hostname **without** any scheme (http:// or https://)
```bash
[default]
gc_hostname = your_host_name.guardicore.com       # Do not prepend http(s)://
gc_username = your_api_username
gc_password = your_api_password
```


# 2DOS
- add auto - auth renewal if failed