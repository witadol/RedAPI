#!/usr/bin/env bash
CURRENT_DIR=`dirname $0`
${CURRENT_DIR}/confinit.py
${CURRENT_DIR}/ArtSoftPrinter &
${CURRENT_DIR}/../nw &
