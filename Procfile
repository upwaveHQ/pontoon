web: newrelic-admin run-program gunicorn pontoon.wsgi:application --log-file -
worker: newrelic-admin run-program celery --app=pontoon.base.celeryapp worker --loglevel=info --without-gossip --without-mingle --without-heartbeat --concurrency=2
automl-warmup: newrelic-admin run-program python pontoon/machinery/automl_warmup.py
