#!/bin/bash

# Check if tree is installed
if ! command -v tree &> /dev/null
then
    echo "tree command could not be found. Please install it and run this script again."
    exit
fi

# Define the output file
OUTPUT_FILE="README.md"

# Define the pattern for files and directories to exclude
EXCLUDE_PATTERN='.venv|__pycache__|*.pyc|*.pyo|*.pyd|.pytest_cache|*.egg-info|*.eggs|node_modules|migrations'

# Generate the directory structure excluding the defined patterns and save it to the output file
echo "# Project Structure" > $OUTPUT_FILE
echo "This document provides an overview of the project structure." >> $OUTPUT_FILE
echo "" >> $OUTPUT_FILE
echo "## Table of Contents" >> $OUTPUT_FILE
echo "- [Backend](#backend)" >> $OUTPUT_FILE
echo "- [Backups](#backups)" >> $OUTPUT_FILE
echo "- [Cronjobs](#cronjobs)" >> $OUTPUT_FILE
echo "- [Frontend](#frontend)" >> $OUTPUT_FILE
echo "- [NGINX](#nginx)" >> $OUTPUT_FILE
echo "- [Other Files](#other-files)" >> $OUTPUT_FILE
echo "" >> $OUTPUT_FILE

# Add Backend Section
echo "## Backend" >> $OUTPUT_FILE
echo "Django Rest API project" >> $OUTPUT_FILE
echo "\`\`\`" >> $OUTPUT_FILE
tree -a -I "$EXCLUDE_PATTERN" backend >> $OUTPUT_FILE
echo "\`\`\`" >> $OUTPUT_FILE
echo "" >> $OUTPUT_FILE

# Add Frontend Section
echo "## Backups" >> $OUTPUT_FILE
echo "Postgrey SQL backup and restore system by cronjob service" >> $OUTPUT_FILE
echo "\`\`\`" >> $OUTPUT_FILE
tree -a -I "$EXCLUDE_PATTERN" backups >> $OUTPUT_FILE
echo "\`\`\`" >> $OUTPUT_FILE
echo "" >> $OUTPUT_FILE

# Add Cronjobs Section
echo "## Cronjobs" >> $OUTPUT_FILE
echo "Periodicly backing up postgre database" >> $OUTPUT_FILE
echo "\`\`\`" >> $OUTPUT_FILE
tree -a -I "$EXCLUDE_PATTERN" cronjob >> $OUTPUT_FILE
echo "\`\`\`" >> $OUTPUT_FILE
echo "" >> $OUTPUT_FILE

# Add Frontend Section
echo "## Frontend" >> $OUTPUT_FILE
echo "Vue Project For Frontend" >> $OUTPUT_FILE
echo "\`\`\`" >> $OUTPUT_FILE
tree -a -I "$EXCLUDE_PATTERN" frontend >> $OUTPUT_FILE
echo "\`\`\`" >> $OUTPUT_FILE
echo "" >> $OUTPUT_FILE

# Add NGINX Section
echo "## NGINX" >> $OUTPUT_FILE
echo "Serving frontend and backend service by this nginx" >> $OUTPUT_FILE
echo "\`\`\`" >> $OUTPUT_FILE
tree -a -I "$EXCLUDE_PATTERN" nginx >> $OUTPUT_FILE
echo "\`\`\`" >> $OUTPUT_FILE
echo "" >> $OUTPUT_FILE

# # Add Configuration Files Section
# echo "## Configuration Files" >> $OUTPUT_FILE
# echo "\`\`\`" >> $OUTPUT_FILE
# tree -a -I "$EXCLUDE_PATTERN" . | grep -E "\.env|\.gitignore|docker-compose.yml|Dockerfile" >> $OUTPUT_FILE
# echo "\`\`\`" >> $OUTPUT_FILE
# echo "" >> $OUTPUT_FILE

# Add Other Directories
echo "## Other Files" >> $OUTPUT_FILE
echo "\`\`\`" >> $OUTPUT_FILE
tree -a -I "$EXCLUDE_PATTERN|backend|backups|frontend|cronjob|nginx" >> $OUTPUT_FILE
echo "\`\`\`" >> $OUTPUT_FILE
echo "" >> $OUTPUT_FILE

# Print a message indicating where the output was saved
echo "Project structure has been saved to $OUTPUT_FILE"
