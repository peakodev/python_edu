#!/bin/sh

# Load environment variables from .env file
set -a
. ./.env
set +a

STORAGE="/app/$STORAGE_DIR"
FILE="$STORAGE/$DATA_FILE"

# Check if storage directory exists, create it if not
if [ ! -d "$STORAGE" ]; then
  mkdir -p $STORAGE
fi

# Check if data.json file exists, create it if not
if [ ! -f "$FILE" ]; then
  echo "{}" > $FILE
fi

# Run the main application
exec python main.py