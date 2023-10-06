#!/usr/bin/env bash

while true
do
    echo "What is the commit message (or type 'exit' to quit)"
    read commit_message

    if [ "$commit_message" == "exit" ]
    then
        echo "Exiting the script"
        exit 0
    elif [ -n "$commit_message" ]
    then
        git add .
        git commit -m "$commit_message"
        git push
        break  # Exit the loop when a commit is successful
    else
        echo "Commit message cannot be empty. Please provide a valid message."
    fi
done

