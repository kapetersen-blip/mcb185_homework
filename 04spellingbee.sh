#!/bin/bash

# NYT Spelling Bee solver
# Middle letter: R
# Outer letters: O Z N I C A
# Words must be 4+ letters
# Dictionary: ../MCB185/data/dictionary.gz

gunzip -c ../MCB185/data/dictionary.gz \
| grep -i '^[OZNIRCA]*R[OZNIRCA]*$' \
| grep -E '^.{4,}$'

