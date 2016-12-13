Name: jobinfo
Version: 13dec2016
Release: 1
Summary: Collect job information from SLURM in nicely readable format.

Group: System Environment/Base
License: MIT
URL: https://github.com/rug-cit-ris/slurm-jobinfo
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
jobinfo - collates job information from the 'sstat', 'sacct' and 'squeue' SLURM commands to give a uniform interface for both current and historical jobs.

%prep
%setup -q

%build
#make

%install
mkdir -p $RPM_BUILD_ROOT/usr/bin
install jobinfo $RPM_BUILD_ROOT/usr/bin/jobinfo

%files
%defattr(-,root,root)
#%doc README
/usr/bin/jobinfo

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Tue Dec 13 2016 Bob Dröge <b.e.droge@rug.nl> - 13dec2016
- Python 3 compatibility
- Job efficiency percentage at CPU time

* Mon Mar 22 2016 Bob Dröge <b.e.droge@rug.nl> - 8dec2015
- Initial build