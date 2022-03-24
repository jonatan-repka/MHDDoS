#!/usr/bin/env bash

set -x
set -e

git remote set-url origin git@repka-github:MHProDev/MHDDoS.git
git pull origin main --rebase --autostash
git remote set-url origin git@repka-github:jonatan-repka/MHDDoS.git
