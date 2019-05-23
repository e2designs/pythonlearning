Dog BNB

Application for reserving a cozy space for your dog while on vacation.



Notes:

Embed data or not to embed data?

1. Is the embedded data wanted 80% of the time?
     - Do we want the requirement information every time we look at a test record.
     - Probably don't want all the regression run information, maybe just the last run
     - Or last week
2. How often is the embedded data needed without the containing document?
     - How often would we query a requirement without the associated test?
     - Polarian would most likely be used.
3. Is the embedded data a bound set?
     - There are a finite number of requirements per test.
     - All regression run data would be too much.
4. Is that bound small?
    - Keep document in the kb range
5. How varied are your queries?
    - Document should match the most common query.
