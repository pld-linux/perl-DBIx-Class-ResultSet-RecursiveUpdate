#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	DBIx
%define	pnam	Class-ResultSet-RecursiveUpdate
Summary:	DBIx::Class::ResultSet::RecursiveUpdate - like update_or_create - but recursive
#Summary(pl.UTF-8):	
Name:		perl-DBIx-Class-ResultSet-RecursiveUpdate
Version:	0.002
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/DBIx/%{pdir}-%{pnam}-v%{version}.tar.gz
# Source0-md5:	f24a772e098223693737f9a3b5922343
URL:		http://search.cpan.org/dist/DBIx-Class-ResultSet-RecursiveUpdate/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(DBIx::Class::IntrospectableM2M)
BuildRequires:	perl-DateTime
BuildRequires:	perl-DBIx-Class >= 0.08011
BuildRequires:	perl-SQL-Translator >= 0.08
BuildRequires:	perl-SQL-Translator-DBIx-Class
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
You can feed the ->create method with a recursive datastructure
and have the related records created.  Unfortunately you cannot do
a similar thing with update_or_create - this module tries to fill
that void.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-v%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/DBIx/Class/ResultSet/*.pm
%{_mandir}/man3/*
