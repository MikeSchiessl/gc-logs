# gc-logs
The tool was built to provide GC logs to ULS.
It fetches Guardicore logs from the GC API.

---
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

### Audit Logs
Setup the .edgerc file as described [here](#authentication)
```bash
akamai-gc events audit --follow
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
---
# Advanced topics
## Credentials via ENV VARS
Either use environmental variables OR the .edgerc file

| Variable                   | Default | Description                                                                                      |
|----------------------------|---------|--------------------------------------------------------------------------------------------------|
| CENTRA_MANAGEMENT_HOSTNAME                | none    | Alternative to EDGERC - put the CENTRA management hostname here |
| CENTRA_MANAGEMENT_PORT | 443     | Alternative to EDGERC - put the CENTRA management port here |
| CENTRA_MANAGEMENT_USERNAME                | none    | Alternative to EDGERC - put the CENTRA username here |
| CENTRA_MANAGEMENT_PASSWORD                | none    | Alternative to EDGERC - put the CENTRA password here |




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

---
   
# 2DOS
- export "tags" and save to CSV
---
# Changelog
## v0.0.6
 - Fixed a bug that might happen when a user's password has expired (not leading to a proper error msg)
 - Added proper user-agent header to the auth request (was None before)

## v0.0.5
 - Fixed a bug in the authentication handling which led to an issue with GC v50.4  
   **Please update to this gc-logs version before upgrading your centra management to v50.4**

## v0.0.4(beta)
 - Added audit trail (thx for the nudge @Markus)

## v0.0.3(beta)
 - minor bugfixes

## v0.0.2(beta)
 - Added ENV VAR support for edgerc data

## v0.0.1(beta)
  - Bugfix --start and --end time
---
# Support
Solution is provided as-is, Akamai Support will only be able to help on the EAA Connector as Docker container.  
For questions or issues with this solution, please raise a GitHub ticket.