#! /usr/bin/env bash

sudo ln -s /usr/lib/python3/dist-packages/apt* /usr/local/lib/python3.11/site-packages/
sudo ln -s /usr/local/lib/python3.11/site-packages/apt_pkg.cpython*.so /usr/local/lib/python3.11/site-packages/apt_pkg.so
sudo ln -s /usr/local/lib/python3.11/site-packages/apt_inst.cpython*.so /usr/local/lib/python3.11/site-packages/apt_inst.so
pipenv install -d
