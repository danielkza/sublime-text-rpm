# Deprecation Notice

Official Sublime Text [repositories](https://www.sublimetext.com/docs/3/linux_repositories.html#dnf)
are now available and should be used instead of this repository.

---

# RPM packaging files for Sublime Text
## Suitable for RPM based Linux such as Fedora, RedHat & CentOS

Main files are installed in /opt/sublime-text. Icons are moved to their correct
place at /usr/share/icons, and a desktop file is included in /usr/share/applications.

Unlike some other packages available online, this does not download the program
at installation time. Since Sublime Text's license does not permit redistribution,
I cannot provided pre-compiled versions. You must create them yourself.
The process is easy, fortunately.

For example, for Fedora, you need the rpmdevtools and rpm-build packages. Then,
after cd-ing to this project's folder, run `./build.sh`, or equivalently:

```
spectool -g sublime-text.spec`
rpmbuild --define "_sourcedir $PWD" -bb sublime-text.spec
```

If everything went correctly, you should see the path of the resulting RPM
printed in rpmbuild's output. e.g.:

`Wrote: /home/danielkza/rpmbuild/RPMS/x86_64/sublime-text-3.3083-3.fc21.x86_64.rpm`

Just install it and you're good to go.

If a new version has been released and the spec has yet not been updated, it's
easy to fix it yourself. All that is needed is to change the `build_version`
variable at the top of the file to the correct build and reset the release
number to 1. Aftwerwards, please send a pull request with the update if
possible.
