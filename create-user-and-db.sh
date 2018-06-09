#!/bin/bash

sudo -u postgres createuser -D -A -P user
sudo -u postgres createdb -O user testdb

sudo /etc/init.d/postgresql reload

