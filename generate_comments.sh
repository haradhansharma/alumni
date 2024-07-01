#!/bin/bash

# Function to extract comments and format them as markdown
extract_comments() {
    local directory=$1
    local output_file=$2

    echo "# Documentation for $directory" > "$output_file"
    echo "" >> "$output_file"

    # Find all files in the specified directory, excluding specified files and directories
    find "$directory" -type f \
        ! \( -iname "*.md" -o -iname "*.ico" -o -iname "*.webp"  -o -iname "*.jpeg" -o -iname "*.jpg" -o -iname "*.png" -o -iname "*.json" -o -iname "*.conf" -o -iname "Dockerfile" -o -iname "*.js" -o -iname "*.css" -o -iname "*.scss" -o -iname "*.map" -o -iname "*.env" -o -iname "*.txt" -o -iname "*.yml" -o -iname "*.sh" -o -iname "*.gitignore" -o -iname "*.dockerignore" -o -iname "*.pyc" -o -iname "*.pyo" -o -iname "*.pyd" -o -iname ".pytest_cache" -o -iname "*.egg-info" -o -iname "*.crt" -o -iname "*.key" \) \
        -not \( -path "*/node_modules/*" -o -path "*/migrations/*" -o -path "*/.pytest_cache/*" -o -path "*/__pycache__/*" -o -path "*/.venv/*" \) | while read -r file; do

        echo "Processing $(basename "$file")..."
        echo "## $(basename "$file")" >> "$output_file"
        echo "### $(dirname "$file")" >> "$output_file"
        echo "\`\`\`" >> "$output_file"
        
        # Extract comments from the file
        awk '/^([ \t]*#|\/\/|\/\*|<!--)/ {print}' "$file" >> "$output_file"
        
        echo "\`\`\`" >> "$output_file"
        echo "" >> "$output_file"
    done

    echo "Comments for $directory have been extracted and saved to $output_file"
}

# Define the directories and output files
declare -A services=(
    ["backups"]="backup_comments.md"
    ["cronjob"]="cronjob_comments.md"
    ["frontend"]="frontend_comments.md"
    ["backend"]="backend_comments.md"
    ["nginx"]="nginx_comments.md"
)

# Loop through each service directory and extract comments
for dir in "${!services[@]}"; do
    output_file="${services[$dir]}"
    echo "Starting to extract comments for $dir..."
    extract_comments "$dir" "$output_file"
    echo "Finished extracting comments for $dir."
done

echo "All comments have been extracted and saved to their respective files."
