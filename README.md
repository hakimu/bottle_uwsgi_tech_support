### This is a Bottle app being served by uWSGI.

This is the application entry point.

```
app = application = bottle.Bottle()
```

The command to run the app with the Python agent is:

```
NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program uwsgi --http :8080 --wsgi-file bottle_app.py --single-interpreter --enable-threads
```

