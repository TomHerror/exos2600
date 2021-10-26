#!/bin/bash

VENV=$(realpath $1)
BIN=$2

shift 1
echo VENV $VENV
echo EXEC $1 AND $*
echo MUSTEXEC "source $VENV/bin/activate && $*"
source $VENV/bin/activate && $*
