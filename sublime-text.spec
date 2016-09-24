# Sublime Text 3 RPM package.
# http://github.com/danielkza/sublime-text-rpm
# http://sublimetext.com

%define major_version 3
%define build_version 3125
%define _subldir /opt/sublime-text
%define debug_package %{nil}

Name:    sublime-text
Summary: Sublime Text is a sophisticated text editor for code, markup and prose.
Version: %{major_version}.%{build_version}
Release: 1%{?dist}
Group:   Applications/Editors
License: Proprietary
URL:     http://sublimetext.com

ExclusiveArch: i686 x86_64

%ifarch i686
Source0: https://download.sublimetext.com/sublime_text_%{major_version}_build_%{build_version}_x32.tar.bz2
%else
Source0: https://download.sublimetext.com/sublime_text_%{major_version}_build_%{build_version}_x64.tar.bz2
%endif
Source1: sublime_text.desktop
Source2: subl

BuildRequires: desktop-file-utils

%description
Sublime Text is a sophisticated text editor for code, markup and prose.
You'll love the slick user interface, extraordinary features and amazing performance.

%prep
%setup -q -n sublime_text_3

%build

%install

# Turn off the brp-python-bytecompile script
# Sublime Text's Python files are just API definitions and shouldn't actually
# be precompiled.
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

# Copy everything to the destination directory to start
install -m 755 -d %{buildroot}%{_subldir}
cp -a ./. %{buildroot}%{_subldir}/

# Create binaries: sublime_text is symlinked, subl is wrapped to keep the
# program name as sublime_text
install -m 755 -d %{buildroot}%{_bindir}
ln -s %{_subldir}/sublime_text %{buildroot}%{_bindir}/sublime_text
install -m 755 %{SOURCE2} %{buildroot}%{_bindir}/subl

# Create the desktop file correctly
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

# Copy icons to their correct place, then remove the 'Icon' directory from the
# main directory
install -m 755 -d %{buildroot}%{_datadir}/icons/hicolor/
for res in 16x16 32x32 48x48 128x128 256x256; do
    install -m 755 -d %{buildroot}%{_datadir}/icons/hicolor/${res}/apps
    mv %{buildroot}%{_subldir}/Icon/${res}/sublime-text.png \
       %{buildroot}%{_datadir}/icons/hicolor/${res}/apps
    rmdir %{buildroot}%{_subldir}/Icon/${res}
done
rmdir %{buildroot}%{_subldir}/Icon

%postun
# Update desktop files and icons. Only run for uninstall, since upgrade is
# covered by posttrans
if [ $1 -eq 0 ]; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
    update-desktop-database &> /dev/null || :
fi

%posttrans
# Covers install and upgrade
touch --no-create %{_datadir}/icons/hicolor &>/dev/null
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
update-desktop-database &> /dev/null || :

%files
%{_subldir}/
%{_bindir}/sublime_text
%{_bindir}/subl
%{_datadir}/applications/sublime_text.desktop
%{_datadir}/icons/hicolor/*/apps/sublime-text.png

%changelog
* Sat Sep 24 2016 Daniel Miranda <danielkza2@gmail.com> 3.3125-1
- New upstream build

* Sat Sep 24 2016 Daniel Miranda <danielkza2@gmail.com> 3.3124-1
- New upstream build

* Fri Sep 17 2016 Daniel Miranda <danielkza2@gmail.com> 3.3122-1
- New upstream build

* Sat Aug 06 2016 Daniel Miranda <danielkza2@gmail.com> 3.3120-1
- New upstream build

* Tue May 16 2016 Wes Render <wes.render@outlook.com> 3.3114-1
- Update Readme for search engine. Update Sublime Build to 3114

* Tue May 19 2015 Daniel Miranda <danielkza2@gmail.com> 3.3083-3
- Replace subl symlink with wrapper script to fix window class when run

* Tue May 19 2015 Daniel Miranda <danielkza2@gmail.com> 3.3083-2
- Fix invalid icon paths

* Tue May 19 2015 Daniel Miranda <danielkza2@gmail.com> 3.3083-1
- Initial release (build 3083)
