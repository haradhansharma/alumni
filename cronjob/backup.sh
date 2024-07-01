#!/bin/bash
# Backup the PostgreSQL database
PGPASSWORD=$BK_DBPASS pg_dump -h $BK_DBHOST -U $BK_DBUSER $BK_DBNAME > /backups/backup.sql
