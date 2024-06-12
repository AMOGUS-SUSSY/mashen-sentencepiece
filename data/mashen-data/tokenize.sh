#!/bin/bash

cmake ..
make -j $(nproc)
sudo make install
sudo ldconfig -v
spm_train --input=test.txt --model_prefix=prefix --vocab_size=8000 --character_coverage=1.0 --model_type=bpe --treat_whitespace_as_suffix=False


