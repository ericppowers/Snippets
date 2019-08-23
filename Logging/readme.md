# Logging
## Best Practices:
- Use .ini file for debug settings
- %(asctime)s format is: YY/MM/DD HH:MM:SS (UTC +/- HHMMSS)
  - Makes the file more legible when there's multiple days, months, or years of log info
- Use try/except clauses to log exceptions and keep the program running, if at all possible
- Log entire traceback to make debugging and troubleshooting much easier
- Use \_\_name\_\_ as logger name to display whether the module was called by another module
