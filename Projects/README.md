SERVER HEALTH CHECKER

OVERVIEW
A beginner Python project that checks a disk-usage percentage and reports 
whether it is healthy or too high.

FEATURES
•Accepts user input.
•Warns when disk usage exceeds 80%.
•Accepts valid percentages from 0 to 100.
•Handles invalid text input without crashing.
•Rejects percentages outside the valid range.

TECHNOLOGIES
•Python 3
•Terminal
•Basic conditional logic and exception handling

TEST RESULTS
INPUT		EXPECTED RESULT		RESULT
90		Warning			Passed
hello		Invalid input error	Passed
123		Out-of-range error	Passed
50		Healthy 		Passed
-9		Out-of-range error	Passed

WHAT I LEARNED
I learned how to use variables, user input, numeric conversion, if/else 
statements, validation, and try/except error handling.

FUTURE IMPROVEMENTS
•Read disk usage from a real computer or server.
•Add timestamps to reports.
•Log warnings to a file.
•Explore monitoring a cloud server in AWS.
