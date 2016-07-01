#!/bin/bash

projdir="$HOME/bigdata/reddit"
curdir="$(pwd)"

cd "$projdir/output"

for arg in "$@"; do
    echo $arg
    echo "cd $projdir; pwd; echo $curdir/$arg; ./src/mkModel.py $curdir/$arg  0 10" | qsub -l mem=32gb
    echo "cd $projdir; pwd; echo $curdir/$arg; ./src/mkModel.py $curdir/$arg 10 20" | qsub -l mem=32gb
    echo "cd $projdir; pwd; echo $curdir/$arg; ./src/mkModel.py $curdir/$arg 20 30" | qsub -l mem=32gb
    echo "cd $projdir; pwd; echo $curdir/$arg; ./src/mkModel.py $curdir/$arg 30 40" | qsub -l mem=32gb
    echo "cd $projdir; pwd; echo $curdir/$arg; ./src/mkModel.py $curdir/$arg 40 50" | qsub -l mem=32gb
    echo "cd $projdir; pwd; echo $curdir/$arg; ./src/mkModel.py $curdir/$arg 50 60" | qsub -l mem=32gb
    echo "cd $projdir; pwd; echo $curdir/$arg; ./src/mkModel.py $curdir/$arg 60 70" | qsub -l mem=32gb
    echo "cd $projdir; pwd; echo $curdir/$arg; ./src/mkModel.py $curdir/$arg 70 80" | qsub -l mem=32gb
    echo "cd $projdir; pwd; echo $curdir/$arg; ./src/mkModel.py $curdir/$arg 80 90" | qsub -l mem=32gb
    echo "cd $projdir; pwd; echo $curdir/$arg; ./src/mkModel.py $curdir/$arg 90 100" | qsub -l mem=32gb
done

