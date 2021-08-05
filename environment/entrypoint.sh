#!/bin/bash

set -e
jupyter lab --ip='*' --NotebookApp.token='tomtom' --allow-root --port=8000 &
exec "$@"