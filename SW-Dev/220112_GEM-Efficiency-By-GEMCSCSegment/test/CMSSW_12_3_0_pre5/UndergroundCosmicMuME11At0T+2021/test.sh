TEST=${1:-""}

if [ -z ${TEST} ]; then
    TEST="hi"
fi

echo ${TEST}
