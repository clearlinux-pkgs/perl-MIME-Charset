#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-MIME-Charset
Version  : 1.012.2
Release  : 8
URL      : https://cpan.metacpan.org/authors/id/N/NE/NEZUMI/MIME-Charset-1.012.2.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/N/NE/NEZUMI/MIME-Charset-1.012.2.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libm/libmime-charset-perl/libmime-charset-perl_1.012.2-1.debian.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0 GPL-2.0
Requires: perl-MIME-Charset-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
MIME-Charset Package.
This package is free software; you can redistribute it and/or modify it
under the same terms as Perl itself.

%package dev
Summary: dev components for the perl-MIME-Charset package.
Group: Development
Provides: perl-MIME-Charset-devel = %{version}-%{release}

%description dev
dev components for the perl-MIME-Charset package.


%package license
Summary: license components for the perl-MIME-Charset package.
Group: Default

%description license
license components for the perl-MIME-Charset package.


%prep
%setup -q -n MIME-Charset-1.012.2
cd ..
%setup -q -T -D -n MIME-Charset-1.012.2 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/MIME-Charset-1.012.2/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-MIME-Charset
cp COPYING %{buildroot}/usr/share/package-licenses/perl-MIME-Charset/COPYING
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-MIME-Charset/deblicense_copyright
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
/usr/lib/perl5/vendor_perl/5.28.2/MIME/Charset.pm
/usr/lib/perl5/vendor_perl/5.28.2/MIME/Charset/Defaults.pm.sample
/usr/lib/perl5/vendor_perl/5.28.2/MIME/Charset/UTF.pm
/usr/lib/perl5/vendor_perl/5.28.2/MIME/Charset/_Compat.pm
/usr/lib/perl5/vendor_perl/5.28.2/POD2/JA/MIME/Charset.pod

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/MIME::Charset.3
/usr/share/man/man3/POD2::JA::MIME::Charset.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-MIME-Charset/COPYING
/usr/share/package-licenses/perl-MIME-Charset/deblicense_copyright
