#!/bin/bash

sudo -u postgres dropdb testdb
sudo -u postgres dropuser user

sudo /etc/init.d/postgresql reload

