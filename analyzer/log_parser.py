import re
from collections import defaultdict

def parse_logs(log_text):
    """
    Parses raw log text and extracts failed login attempts.
    Returns suspicious IPs and counts.
    """

    failed_login_pattern = r"Failed password.*from (\d+\.\d+\.\d+\.\d+)"
    ip_attempts = defaultdict(int)

    for line in log_text.split("\n"):
        match = re.search(failed_login_pattern, line)
        if match:
            ip = match.group(1)
            ip_attempts[ip] += 1

    return ip_attempts


def detect_bruteforce(ip_attempts, threshold=5):
    """
    Detects possible brute-force attacks based on attempt threshold.
    """

    suspicious_ips = {
        ip: count
        for ip, count in ip_attempts.items()
        if count >= threshold
    }

    return suspicious_ips
