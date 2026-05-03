1. Await inside a loop waits for each task to complete before starting the next one, so execution is sequential.

2. asyncio.gather runs multiple tasks concurrently, improving performance for I/O-bound operations.

3. If one task fails without --continue-on-error, gather raises an exception and stops execution.

4. Semaphore limits the number of concurrent tasks to avoid overload.

5. Async should not be used for CPU-bound tasks or when operations are already fast and simple.
