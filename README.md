# 🛡️ Oscar Constanzo Audit & Patch Tool (CVE-2026-41940)

[![Python Version](https://img.shields.io/badge/python-3.14-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Professional Security Auditing & Incident Response Suite for cPanel Infrastructure.**

---

## 📖 Description

This tool was developed by Oscar Constanzo Quezada, AKA Underhost to identify and remediate the CVE-2026-41940 vulnerability in cPanel servers. The flaw allows an **Authentication Bypass** via HTTP session header injection, enabling an attacker to gain full administrative (root) privileges without a valid password.

---

## 🚀 Key Features

*   **THIS TOOL IS CREATED IN SPANISH 🇨🇱
*   **Signature Audit:** Fast scanning to detect vulnerable cPanel versions.
*   **Risk Assessment:** Integrated technical impact analysis explaining the danger to the infrastructure.
*   **Response Manual:** A 5-phase guide for system sanitization and hardening.
*   **Persistence:** Persistent scanning loop for multiple targets.

---
⚠️ Legal Disclaimer
THIS TOOL IS PROVIDED FOR EDUCATIONAL AND ETHICAL AUDITING PURPOSES ONLY.[cite: 1] The author is not responsible for any misuse, damage, or unauthorized access. Use this software on networks only with explicit permission.


## 🛠️ Installation
```bash
# Clone the repository
git clone [https://github.com/Underh0st/CPanel-Audit-Remediation-Tool.git](https://github.com/Underh0st/CPanel-Audit-Remediation-Tool.git)

# Install dependencies
pip3 install colorama requests urllib3

# Run the script
python3 ART.py

```

📋 Remediation Protocol
The tool guides the administrator through a professional incident response protocol.

1.Isolation: Restrict access to management ports (2082-2087) via firewall.

2.Patching: Force core update using /scripts/upcp --force.

3.Sanitization: Physical purge of /var/cpanel/sessions/raw/ to invalidate stolen tokens.

4.Threat Hunting: Locate persistence (backdoors) using find /home -mtime -1 -ls.

5.Hardening: Enable cPHulk and Multi-Factor Authentication (MFA).

Author
Oscar Constanzo Q. (Underhost) - Security Logic & Development
