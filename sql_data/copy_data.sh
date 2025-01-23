#!/bin/bash

data_dump='order_items'
psql --username=postgres ecommerce < $data_dump.sql

