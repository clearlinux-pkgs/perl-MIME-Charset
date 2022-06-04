#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-MIME-Charset
Version  : 1.012.2
Release  : 19
URL      : https://cpan.metacpan.org/authors/id/N/NE/NEZUMI/MIME-Charset-1.012.2.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/N/NE/NEZUMI/MIME-Charset-1.012.2.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libm/libmime-charset-perl/libmime-charset-perl_1.012.2-1.debian.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0 GPL-2.0
Requires: perl-MIME-Charset-license = %{version}-%{release}
Requires: perl-MIME-Charset-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
MIME-Charset Package.
This package is free software; you can redistribute it and/or modify it
under the same terms as Perl itself.

%package dev
Summary: dev components for the perl-MIME-Charset package.
Group: Development
Provides: perl-MIME-Charset-devel = %{version}-%{release}
Requires: perl-MIME-Charset = %{version}-%{release}

%description dev
dev components for the perl-MIME-Charset package.


%package license
Summary: license components for the perl-MIME-Charset package.
Group: Default

%description license
license components for the perl-MIME-Charset package.


%package perl
Summary: perl components for the perl-MIME-Charset package.
Group: Default
Requires: perl-MIME-Charset = %{version}-%{release}

%description perl
perl components for the perl-MIME-Charset package.


%prep
%setup -q -n MIME-Charset-1.012.2
cd %{_builddir}
tar xf %{_sourcedir}/libmime-charset-perl_1.012.2-1.debian.tar.xz
cd %{_builddir}/MIME-Charset-1.012.2
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/MIME-Charset-1.012.2/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-MIME-Charset
cp %{_builddir}/MIME-Charset-1.012.2/COPYING %{buildroot}/usr/share/package-licenses/perl-MIME-Charset/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-MIME-Charset/054b169ea16fd2231ee891fe8d697b8158b5ac4f
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/MIME::Charset.3
/usr/share/man/man3/POD2::JA::MIME::Charset.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-MIME-Charset/054b169ea16fd2231ee891fe8d697b8158b5ac4f
/usr/share/package-licenses/perl-MIME-Charset/4cc77b90af91e615a64ae04893fdffa7939db84c

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
