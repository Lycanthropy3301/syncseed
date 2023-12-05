# Syncseed Cycle Generation Test and Benchmarking Tools

## Overview

This toolkit is designed to evaluate the performance and cycle generation capabilities of the Syncseed authentication module. The cycle generation test assesses how many iterations it takes for the generator to produce a duplicate seed, indicating the formation of a cycle. The benchmarking tools measure the execution time of the authentication algorithm and seed exchange algorithm under different configurations.

## Cycle Generation Test

### Instructions:

1. **Installation:**
   - Ensure that you have Syncseed installed: `pip install syncseed`

2. **Usage:**
   - Run `cycle_generation_test.py` to perform the cycle generation test.
   - Adjust the test parameters in the script to meet your testing requirements.

3. **Results:**
   - The script will output the number of iterations before a duplicate seed is generated.

## Syncseed Benchmarking Tool

### Instructions:

1. **Installation:**
   - Ensure that you have Syncseed installed: `pip install syncseed`

2. **Usage:**
   - Run `syncseed_benchmark.py` to execute the benchmarking tool.
   - Modify the configuration parameters in the script to test different scenarios.

3. **Results:**
   - The tool will display the time taken for a specified number of iterations, helping you evaluate Syncseed's performance under various settings.

## Seed Exchange Benchmarking Tool

### Instructions:

1. **Installation:**
   - Ensure that you have Syncseed installed: `pip install syncseed`

2. **Usage:**
   - Run `seed_exchange_benchmark.py` to execute the benchmarking tool.
   - Modify the configuration parameters in the script to test different scenarios.

3. **Results:**
   - The tool will display the time taken for a specified number of iterations for each seed exchange method.

## Additional Notes

- **Test Responsibly:**
  - These tools are designed for testing and benchmarking purposes. Use them responsibly.

- **Contribute and Provide Feedback:**
  - Syncseed is a community-driven project. Feel free to contribute, report issues, or provide feedback to improve the toolkit.

- **Stay Updated:**
  - Check for updates and new features regularly. Syncseed is continuously evolving, and your engagement helps shape its future.
