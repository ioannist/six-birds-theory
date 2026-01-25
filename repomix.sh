#!/bin/bash

# Script to run repomix with auto-incrementing version numbers
# Output pattern: repomix_v<N>.txt
# Version is tracked in .repomix-version file (committed to git for sync)

# Set the base filename
BASE_NAME="repomix"
EXTENSION=".txt"
VERSION_FILE=".repomix-version"

# Read current version from tracked file, or start at -1 if file doesn't exist
if [ -f "$VERSION_FILE" ]; then
    CURRENT_VERSION=$(cat "$VERSION_FILE")
    # Validate it's a number
    if ! [[ "$CURRENT_VERSION" =~ ^[0-9]+$ ]]; then
        echo "⚠ Version file contains invalid data, resetting to -1"
        CURRENT_VERSION=-1
    fi
else
    CURRENT_VERSION=-1
fi

# Increment version (if no version exists, start at 0)
NEXT_VERSION=$((CURRENT_VERSION + 1))

# Create output filename
OUTPUT_FILE="${BASE_NAME}_v${NEXT_VERSION}${EXTENSION}"

# Store previous version filename for deletion
PREVIOUS_FILE=""
if [ $CURRENT_VERSION -ge 0 ]; then
    PREVIOUS_FILE="${BASE_NAME}_v${CURRENT_VERSION}${EXTENSION}"
fi

echo "Running repomix with auto-versioning..."
echo "Output will be saved to: $OUTPUT_FILE"

# Run repomix using existing config
repomix -o "$OUTPUT_FILE"

if [ $? -eq 0 ]; then
    echo "✓ Successfully created $OUTPUT_FILE"

    # Update version file
    echo "$NEXT_VERSION" > "$VERSION_FILE"
    echo "✓ Updated version to v$NEXT_VERSION"

    # Delete previous version if it exists
    if [ -n "$PREVIOUS_FILE" ] && [ -f "$PREVIOUS_FILE" ]; then
        rm "$PREVIOUS_FILE"
        echo "✓ Deleted previous version: $PREVIOUS_FILE"
    fi
else
    echo "✗ Error running repomix"
    exit 1
fi