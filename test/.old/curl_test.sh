#!/usr/bin/env bash

CREDENTIALS=$@

./curl_graph_upload.sh $CREDENTIALS
./curl_score_upload.sh $CREDENTIALS
./curl_test_run.sh $CREDENTIALS
