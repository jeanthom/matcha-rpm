%define debug_package %{nil}
Name:           matcha
Version:        0.10
Release:        1%{?dist}
Summary:        A simple read-only web interface for Git repositories.

Group:          Applications/System
License:        MIT
URL:            https://github.com/emersion/matcha

BuildRequires:  git golang npm

%description
A simple read-only web interface for Git repositories.

%prep

%build
export GOPATH="%{_builddir}"
go get -ldflags "-X github.com/emersion/matcha.publicDir=/usr/share/webapps/matcha" github.com/emersion/matcha/cmd/matcha
cd %{_builddir}/src/github.com/emersion/matcha
(cd public && npm install)

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/webapps/matcha/
cp %{_builddir}/bin/matcha %{buildroot}%{_bindir}
cp -r %{_builddir}/src/github.com/emersion/matcha/public/* %{buildroot}%{_datadir}/webapps/matcha/

%files
%{_bindir}/matcha
%{_datadir}/webapps/matcha

%changelog
