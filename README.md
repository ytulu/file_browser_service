# FileBrowserService
The application is a small REST API to display file information from a portion of the user’s file system.
The user will specify a root directory when launching the application. All directories from the root on
downward are then browsable using the REST API.


# Example 
For example, if there is a directory /home/my_user/otherstuff/foo/ containing files foo1 and foo2 as
well as a subdirectory bar/ which in turn contains a file bar1 and a directory baz/, the user will specify
/home/my_user/otherstuff/foo on input and the REST API will be something like:

## Endpoints Implemented
- [ ] GET / -> list contents of foo/ (e.g. foo1, foo2, bar/)
- [ ] GET /bar -> list contents of foo/bar/ (e.g bar1, baz/)
- [ ] GET /foo1 -> contents of file foo/foo1
- [ ] GET /bar/bar1 -> contents of file foo/bar/bar1

TODO:
- [ ] POST /foo3 -> add foo3 file to / directory
- [ ] POST /bar/baz2 add baz2 file to /bar directory
- [ ] POST /qux -> add qux directory to / directory

- [ ] PUT foo2 -> replace foo2 file with new foo2
- [ ] PUT baz -> replace baz directory with new baz

- [ ] DELETE / -> delete the content of / directory
- [ ] DELETE /bar -> delete the content of /bar directory
- [ ] DELETE bar1 -> delete file bar1 from /bar directory
```
## Basic Rules
- Your REST API should return responses in JSON in an appropriate fashion. Use good REST API
design practices.
- Report all files in directory responses, including hidden files. You should report file name, owner,
size, and permissions (read/write/execute - standard octal representation is acceptable). 
- You can assume that all files are text files of modest size (i.e., that can fit comfortably within a JSON blob).

## Requirements
Install [Docker](https://docs.docker.com/get-docker/)


## Usage
To run the server for first time after cloning the repo locally, please execute the following from the root directory:

```bash
chmod +x first_start.sh
./first_start.sh
```

Consecitive runs of the service can be done as followed:
```
chmod +x run.sh
./run.sh
```

Then visit the [api](http://localhost:5004/api) and take a look at the [swagger docs](http://localhost:5004/) 

## Running Testing locally
To run the tests locally within docker:
```
docker-compose exec -T api python -m pytest "src/tests"
```