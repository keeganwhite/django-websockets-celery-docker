import subprocess


def alive(ip):
    """
    Test if a host is reachable or not.
    :param ip: IP address of the host
    :return: True if reachable, False otherwise
    """
    result = False
    command = ["/bin/fping", ip, ]
    p = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if p.returncode != 0:
        return result
    else:
        result = True
        return result
