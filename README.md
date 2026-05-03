# Async Batch Processor

## Description
Processes tasks from a JSON file in different execution modes.

## Run

python -m async_tool input.json --mode async

## Modes

sync     sequential  
async    fully concurrent  
limited  limited concurrency  

## Options

--limit N  
--continue-on-error  
--log-level DEBUG|INFO|WARNING|ERROR
