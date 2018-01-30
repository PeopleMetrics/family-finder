## Family Finder

This simple class takes in JSON family data from a separate source and has some simple functions to view information about the data.

The JSON is currently in a flat structure but the 3rd party data source is releasing a version 2 with nested parent data (see json_source.py)

1. Add a new feature to support some kind of user friendly message if the name passed to getAncestors() isn't found.

2. Update the class *and tests* to support the new data structure `data_v2` but keep it backwards compatible with the old structure.

When you're ready, send us a pull request