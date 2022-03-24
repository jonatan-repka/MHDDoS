#!/usr/bin/env bash

set -x
set -e

pushd ~/MHDDoS

git reset --hard
git pull --rebase
./scripts/pxy_loop.py

popd
