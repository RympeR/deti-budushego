import os
import re
import random
import string
from django.core.validators import validate_email


def id_generator(size=12, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def get_filename(filename, request):
    return filename.upper()

def set_unique_file_name(file):
    if file:
        end_extension = file.rsplit('.', 1)[1]
        file_name = id_generator() + '.' + end_extension
        return file_name
    else:
        return None


def attachment(instance, filename):
    instance.original_file_name = filename
    # file = set_unique_file_name(filename)
    return os.path.join('attachment', filename)


def preview(instance, filename):
    instance.original_file_name = filename
    # file = set_unique_file_name(filename)
    return os.path.join('preview', filename)


def user_avatar(instance, filename):
    instance.original_file_name = filename
    # file = set_unique_file_name(filename)
    return os.path.join('user', filename)
