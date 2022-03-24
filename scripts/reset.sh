#!/usr/bin/env bash

set -x
set -e

pushd ~/MHDDoS

git reset --hard
git pull --rebase
pip install -r requirements.txt

popd
