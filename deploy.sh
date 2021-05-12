#!/bin/bash
set -e -o pipefail

echo "START DEPLOY"

zip lambda.zip ./lambda_function.py

aws lambda update-function-code --function-name line-bot-water-push --zip-file fileb://lambda.zip

exit 0