import sys
import os
from git import InvalidGitRepositoryError


class ConfigError(Exception):
    def __init__(self, message: str):
        self.message = message


class BackendError(Exception):
    def __init__(self, message: str):
        self.message = message


def check_config(func):
    def decorator(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except ConfigError:
            sys.exit(f"Call 'dstack config' first")

    return decorator


def check_git(func):
    def decorator(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except InvalidGitRepositoryError:
            sys.exit(f"{os.getcwd()} is not a Git repo")

    return decorator


def check_backend(func):
    def decorator(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except BackendError:
            sys.exit(f"{os.getcwd()} is not a Git repo")

    return decorator
