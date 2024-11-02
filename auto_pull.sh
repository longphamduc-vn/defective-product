#!/bin/bash
REPO_DIR="D:\Analysis\defective-product"
cd $REPO_DIR

while true; do
    git pull origin main
    sleep 5  # Wait for 60 seconds before the next pull
done
