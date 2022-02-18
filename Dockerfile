FROM ghcr.io/opsdroid/opsdroid:latest

COPY ./configuration.yaml /home/opsdroid/.config/opsdroid/configuration.yaml
COPY ./__init__.py /skills/tops/__init__.py