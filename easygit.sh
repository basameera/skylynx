#!/bin/bash
# easygit Bash script, by bassandaruwan
# Easy handling of git pull, add, commit and push
# Usage:
#     1. bash easygit.sh -h
#         Get help
#     2. bash easygit.sh
#         Check git status
#     3. bash easygit.sh 'comment'
#         Git add, commit (with comment) and push
#     4. bash easygit.sh -c 'comment'
#         Only git add . and commit with 'comment'
#     5. bash easygit.sh -p
#         Only git push

echo
echo ===== Easy-Git =====
echo

version_revision() {
    today=$(date +"%y%m%d")
    file="revision.yaml"
    rm -f $file
    echo REVISION: $today >>$file
}

if [ $# -gt 0 ]; then
    # echo "Method 1"
    case "$1" in
    -h | --help)
        echo "$package - easy git use"
        echo " "
        echo "options:"
        echo "-h, --help    show brief help"
        echo "-c,           Only git add and commit w/ comment"
        echo "-p,           Only git push"
        echo
        echo "Usage:
            1. bash easygit.sh -h
                - Get help
            2. bash easygit.sh
                - Check git status
            3. bash easygit.sh 'comment'
                - Git add, commit (with comment) and push
            4. bash easygit.sh -c 'comment'
                - Only git add . and commit with 'comment'
            5. bash easygit.sh -p
                - Only git push"
        exit 0
        ;;
    -c)
        shift
        echo "*** Only git add & commit"
        echo

        # version_revision

        if [ $# -eq 1 ]; then
            echo ">>" "Commit message:" "$1"
            echo

            echo
            echo ">>" "Checking git status"
            echo
            git status

            echo
            echo ">>" "Git add"
            echo
            git add .

            echo
            echo ">>" "Git commit"
            echo
            git commit -m "$1"

        else

            echo "ERROR: Commit message required"
        fi
        exit 0
        ;;
    -p)

        shift

        if [ $# -eq 0 ]; then
            echo "*** Only git push"
            echo
            echo
            echo ">> Git push"
            echo
            git push
        else
            echo "ERROR: Unnecessary arguments!"
        fi
        exit 0
        ;;

    esac
fi

if [ $# -eq 0 ]; then
    echo
    echo ">>" "Checking git status"
    echo
    git status
    exit 0
fi

if [ $# -eq 1 ]; then
    
    # version_revision
    
    echo ">>" "Commit message:" "$1"
    echo
    echo
    echo ">>" "Git pull"
    echo
    git pull

    echo
    echo ">>" "Checking git status"
    echo
    git status

    echo
    echo ">>" "Git add"
    echo
    git add .

    echo
    echo ">>" "Git commit"
    echo
    git commit -m "$1"

    echo
    echo ">>" "Git push"
    echo
    git push

    echo
    echo ">>" "Checking git status"
    echo
    git status
fi
