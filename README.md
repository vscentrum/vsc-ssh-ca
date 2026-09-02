# VSC SSH certificate authorities

This repo contains all the VSC SSH certificate authorities in use.
- `leuven.pub`: the KULeuven CA.
- `brussel.pub`: the VUB CAs. There are two for redundancy reason.

For more information on the use, read https://docs.vscentrum.be/accounts/mfa_login.html

To use, first make sure to have an ssh agent running.
- KULeuven: `ssh vscXXXXX@firewall.vscentrum.be` and follow the flow.
- VUB:
    - Install the step-cli from smallstep: https://smallstep.com/docs/step-ca/installation/
    - Bootstrap: `step ca bootstrap --context VSC --team VSC --team-url=https://hpc.vub.be/_static/VSC-CA.json`
    - Request a certificate: `step ssh login --context VSC`

To use at server side you need to add a file in `/etc/ssh/sshd_config.d/` with contents:
```
Match User vsc?????
    TrustedUserCAKeys /etc/ssh/certs/vsc-ca.pub
```
