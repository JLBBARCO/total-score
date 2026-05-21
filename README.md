# Answers

Repository of summation tests to discover your test score based on your answers and the answer key. The files to accept only extensions .csv and .tsv

## .csv File Names

- Answers: answer.csv
- Answer Key: answer_key.csv

### .csv File Structure

In the answer.csv, the first column is named _Question_, the second is _Answer_ and Third is _Class_.

Already in answer_key.csv, the structure is almost the same, with difference that there is a column before the _Question_ called _Score_ with contains a total score of the test. And in the following lines, add a `;` before the content.

These columns are separated by `;`.

This program supports a maximum of 512 answer choices. Furthermore, questions are disregarded.

## .tsv File Names

- Answers: answer.tsv
- Answer Keys: answer_key.tsv

### .tsv File Structure

Is the same structure of .csv

## Build and Release

When code is pushed to `main`, GitHub Actions builds the project on Windows, Linux, and macOS using `build.bat`, `build.sh`, and `build-mac.sh`.

After the three builds finish, the workflow recreates the `Latest` release and uploads these assets:

- `total-score-windows-x64.exe`
- `total-score-linux-x64`
- `total-score-macos-x64`
