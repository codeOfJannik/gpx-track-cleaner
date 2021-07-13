# gpx-track-cleaner
Python script for cleaning gpx tracks. Trackpoints with no change of the lat/lon-position are remove form the gpx data. Script can be used to prevent Strava to calculate auto-pause when importing an activity from a gpx file.

# Purpose
When an activity is imported to Strava via gpx file, Strava automatically recalculates the moving time and pace. For the calculation the auto-pause option seems to be enabled, cause importing sometimes results in implausible moving time and pace.
Consecutive trackpoints where the position did not change are detected as pause. The gpx-cleaner script removes trackpoints with consecutive same positions from the gpx file,
so Strava won't detect any pauses. If activities are exported from Runtastic (Adidas Running), cleaned by the script and imported to Strava, the activity details
on Strava sometimes diverge from the activity details on Runtastic by a few seconds but are plausible in general.

## Runtastic Activity Data
![Runtastic Data](/readme-images/runtastic.jpg)
## Strava Activity Data with cleaned gpx file
![Strava Data](/readme-images/strava.jpg)


# Usage
## Prerequisits
- python needs to be installed
- download gpx-cleaner.py

## Execution
Run from command line:

```
python3 gpx-cleaner.py <path-to-directory-with-gpx-files>
```
Insert the path of the directory that contains the gpx files as argument.

## Result
The cleaned gpx files are stored in a subdirectory `/output` of the passed directory.
