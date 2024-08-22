Issue Summary💌
Duration⏰ of the Outage:
Start Time: 2024-08-20 8:00 AM GMT
End Time: 2024-08-20 11:30 AM GMT
Impact:
During the outage, 60% of users experienced slow response times or were unable to access the service entirely. The affected service was the main API responsible for user authentication and data retrieval. As a result, users could not log in, and those already logged in faced delays when attempting to load their dashboards.
Root Cause🔌:
The root cause was a memory leak in the API's session management module, which led to excessive memory consumption on the server. This eventually caused the server to become unresponsive.
Timeline⏲️
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

