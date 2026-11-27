#!/usr/bin/env bash
set -euo pipefail

# Run from the directory containing Shell1.zip.
rm -rf Shell1
unzip -q Shell1.zip

# Problem 1: navigate and report the current directory without echo.
cd Shell1
printf 'Working in %s\n' "$PWD"

# Problem 2: include hidden entries, use long format, and sort by size.
ls -alS

# Problem 3: remove, create, and rename directories.
rm -r Audio
mkdir Documents Photos Python
mv Random Files

# Problem 4: organize top-level files by extension.
mv ./*.jpg Photos/
mv ./*.txt Documents/
mv ./*.py Python/

# Problem 5: find, move, permit, and execute the photo organizer.
organizer=$(find Files -name organize_photos.sh -type f -print -quit)
printf 'Found photo organizer: %s\n' "$organizer"
mv "$organizer" Scripts/
chmod u+x Scripts/organize_photos.sh
bash Scripts/organize_photos.sh

cd ..
tar -czf UnixShell1.tar.gz Shell1
printf 'Created %s/UnixShell1.tar.gz\n' "$PWD"
