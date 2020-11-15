@echo off

set problemname=%1
set testdir=test\%problemname%
set baseurl=%problemname:~0,-2%
set baseurlreplaced=%baseurl:_=-%

rem # log in
oj login -u username -p password "https://atcoder.jp/"
oj login --check "https://atcoder.jp/"

rem # make test directory
if not exist %testdir% (
  oj dl -d test/%problemname%/ https://atcoder.jp/contests/%baseurlreplaced%/tasks/%problemname%
)

oj test -c "python src/%problemname%.py" -d test/%problemname%/