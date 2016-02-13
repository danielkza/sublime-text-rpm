#!/bin/sh

spectool -g sublime-text.spec
rpmbuild --define "_sourcedir $PWD" -bb sublime-text.spec
