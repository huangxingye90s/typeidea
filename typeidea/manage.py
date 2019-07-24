#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    # os.environ.setdefault("DJANGO_SETTINGS_MODULE", "typeidea.settings")
    # 通过　TYPEIDEA_PROFILE 来控制 Django 加载不同的 settings 文件
    # 以此达到开发环境使用 develop.py 这个配置，而线上使用 product.py 这个配置的目的
    profile = os.environ.get('TYPEIDEA_PROFILE', 'develop')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'typeidea.settings.%s' % profile)
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
