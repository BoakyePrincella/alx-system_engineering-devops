Issue Summary
Duration of the Outage:
Start Time: 2024-08-20 8:00 AM GMT
End Time: 2024-08-20 11:30 AM GMT

Impact:
During the outage, 60% of users experienced slow response times or were unable to access the service entirely. The affected service was the main API responsible for user authentication and data retrieval. As a result, users could not log in, and those already logged in faced delays when attempting to load their dashboards.
Root Cause:
The root cause was a memory leak in the API's session management module, which led to excessive memory consumption on the server. This eventually caused the server to become unresponsive.

Timeline
08:00 AM GMT:
Issue detected by automated monitoring system, which reported elevated response times and a spike in memory usage on the primary API server.
08:15 AM GMT:
Engineers on-call were alerted via monitoring system notifications. Initial investigation began by checking server load and performance metrics.
08:30 AM GMT:
Assumptions were made that a recent code deployment might have caused the issue. The deployment was rolled back, but the problem persisted.
09:00 AM GMT:
Further investigation led the team to suspect a database bottleneck, prompting a review of query performance. No significant issues were found in the database.
09:30 AM GMT:
The issue was escalated to the senior engineering team for a deeper analysis.
10:00 AM GMT:
Senior engineers identified that the memory usage on the API server continued to rise, pointing towards a possible memory leak.
10:30 AM GMT:
The session management module was identified as the source of the leak. A temporary fix was implemented by restarting the affected service to free up memory.
11:30 AM GMT:
The API service was fully restored, and all users were able to access the service without delays. The incident was declared resolved.

Root Cause and Resolution
Root Cause:
The memory leak was caused by a bug in the session management module, specifically in the way session data was stored and retrieved. Sessions were not being properly garbage collected after user logouts, leading to an accumulation of unused session data in memory. Over time, this consumed all available memory on the server, causing it to become unresponsive.
Resolution:
To resolve the issue, the team first restarted the API service to temporarily clear the memory. A deeper analysis of the session management code revealed that sessions were not being correctly terminated. The team applied a patch to ensure that session data is properly cleaned up after use, preventing memory accumulation. The patched version of the module was tested and deployed successfully.

Corrective and Preventative Measures
Improvements/Fixes:
Code Review: Conduct a comprehensive review of the session management module to ensure no further memory leaks exist.
Enhanced Monitoring: Implement more granular memory usage monitoring on all critical services to detect potential leaks early.
Automated Garbage Collection: Update the system to include automated garbage collection for session data at regular intervals.
Tasks:
Patch session management module to ensure proper cleanup of session data.
Implement additional memory usage alerts for critical services.
Conduct a full code audit on session handling across the API to prevent similar issues.
Schedule regular performance testing to identify potential bottlenecks or memory issues.

