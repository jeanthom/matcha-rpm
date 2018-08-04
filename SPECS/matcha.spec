%define debug_package %{nil}
Name:           matcha
Version:        0.45.1
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
go get -u github.com/emersion/matcha/cmd/matcha
cd %{_builddir}/src/github.com/emersion/matcha
(cd public && npm install)
dep ensure

%install
mkdir -p %{buildroot}%{_bindir}
cp %{_builddir}/matcha %{buildroot}%{_bindir}
cp -r %{_builddir}/public/ %{_datadir}/matcha/

%files
%{_bindir}/matcha
%dir %{_datadir}/matcha

%changelog
