# gc-logs
Provide GC logs to ULS

## Usage
```bash
akamai-gc --help
```

## Authentication
To use guardicore CLI, a proper authentication needs to be provided.
Therefore please create an .edgerc file or extend an already existing akamai .edgerc file with the following contents.
The default search location for the edgerc file is `~/.edgerc`.  
```bash
[default]
gc_hostname = your_host_name.guardicore.com
gc_username = your_api_username
gc_password = your_api_password
```
