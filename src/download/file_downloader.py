import subprocess


def download_file(url: str, save_dir: str) -> None:
    """download file to local directory from designated URL.

    Args:
        url (str): URL of the file
        save_dir (str): local directory
    """
    commands = ["wget", "-P", save_dir, url]
    subprocess.run(commands)
