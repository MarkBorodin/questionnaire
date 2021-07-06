#!/bin/bash

celery -A app worker -l info -c 2
