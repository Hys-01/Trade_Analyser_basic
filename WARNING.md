recloning from github removed the config.py on local machine, seems it was never pushed to web 

config files seeminly are ignored

in future: 

Use Environment Variables: For sensitive information, consider using environment variables instead of hardcoding them into a config.py. This way, the configuration can remain outside of the version control system entirely.
Documentation: Ensure that there's clear documentation on how to set up the project from scratch, including how to create any necessary configuration files.
Version Control for Important Files: If config.py contains non-sensitive defaults that are essential for the project to run, consider versioning it but use environment variables or a separate ignored file for sensitive values.


or BACKUP!! BACKUP SUCH FILES ELSEWHERE.