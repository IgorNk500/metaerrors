"""Attention!
Do not use this module if you do not know the user's target operating system!

It only works with Windows"""

import os

STD = "0"
ERROR = "16"
WARN = "48"
INFO = "64"

std_title = ""
msg_format = "{name}: {msg}"


def show(msg: str, title: str = std_title, mode: str = STD, disable_output: bool = True):
    """Displays a pop-up"""
    os.system(f'mshta vbscript:Execute("MsgBox ""{msg}"", {mode}, ""{title}"":close")')


def warn(msg: str, title: str = std_title):
    show(msg, title, WARN)


def info(msg: str, title: str = std_title):
    show(msg, title, INFO)


def error(msg: str, title: str = std_title):
    show(msg, title, ERROR)


def metaraise(err: BaseException,
              title: str = "The program terminated with the error:",
              frmt: str = msg_format):
    """Raise Replacement"""
    msg = frmt.format(msg=err.__str__(), name=err.__class__.__name__)
    show(msg, title, ERROR)
