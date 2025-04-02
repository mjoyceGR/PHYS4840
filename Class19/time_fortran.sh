#!/bin/bash

# Measure compilation time
echo "Compiling RK4.f90..."
start_compile=$(date +%s.%N)
gfortran RK4.f90 -o RK4.exe
end_compile=$(date +%s.%N)
compile_time=$(echo "$end_compile - $start_compile" | bc)

echo "Running RK4.exe..."
# Measure execution time
start_exec=$(date +%s.%N)
./RK4.exe
end_exec=$(date +%s.%N)
exec_time=$(echo "$end_exec - $start_exec" | bc)

echo "Compilation time: $compile_time seconds"
echo "Execution time: $exec_time seconds"
