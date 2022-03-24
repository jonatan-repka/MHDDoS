#!/usr/bin/env bash

set -x
set -e

pushd ~

rm -rf expressvpn*
wget https://www.expressvpn.works/clients/linux/expressvpn_3.19.0.13-1_amd64.deb
sudo dpkg -i expressvpn_3.19.0.13-1_amd64.deb
expressvpn activate

popd
