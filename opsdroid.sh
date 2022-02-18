docker run --rm -ti -p 8080:8080 \
  -v `pwd`/configuration.yaml:/home/opsdroid/.config/opsdroid/configuration.yaml:ro \
  -v `pwd`/__init__.py:/skills/tops/__init__.py \
  -v `pwd`/matrix-store:/home/opsdroid/matrix \
  --env-file secrets.env \
  ghcr.io/opsdroid/opsdroid:latest
