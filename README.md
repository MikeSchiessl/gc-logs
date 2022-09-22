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

# Advanced topics
## Self signed certificates
In order to work with self-signed certificates, you have 2 options:
- You skip the TLS certificate (this is very insecure)
  Either use the `--skip-tls-validation` flag on the command line or
  set the following ENV variable on your system
  ```bash
  export GC_SKIP_TLS_VALIDATION=True
  ```
 
- You provide the root CA of your self signed certifcate to the python process 
  ```bash
  export REQUESTS_CA_BUNDLE=/path/to/your/certificate.pem
  ```

# 2DOS
- export "tags" and save to CSV
