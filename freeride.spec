Summary:	FreeRIDE - IDE for Ruby
Summary(pl):	FreeRIDE - IDE dla jêzyka Ruby
Name:		freeride
Version:	0.6.0
Release:	1
License:	Ruby License
Group:		Development/Tools
Source0:	http://rubyforge.org/download.php/256/%{name}-%{version}.tgz
# Source0-md5:	1fc5dbd376437ce6da7df303b0907244
URL:		http://www.rubyide.org/
BuildRequires:	ruby
Requires:	ruby
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FreeRIDE is a cross-platform IDE for the Ruby Programming Language.

%description -l pl
FreeRIDE to wieloplatformowe zintegrowane ¶rodowisko programistyczne
(IDE) dla jêzyka Ruby.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_prefix}/lib,%{_bindir}

cp -a ../freeride-%{version} $RPM_BUILD_ROOT%{_prefix}/lib/freeride
rm -f $RPM_BUILD_ROOT%{_prefix}/lib/freeride/run.bat
cat <<EOF >$RPM_BUILD_ROOT%{_bindir}/freeride
#!/bin/sh
RUBYLIB=%{_prefix}/lib/freeride
export RUBYLIB
exec ruby %{_prefix}/lib/freeride/freeride.rb
EOF
chmod +x $RPM_BUILD_ROOT%{_bindir}/freeride

cd $RPM_BUILD_ROOT%{_prefix}/lib/freeride/redist
rbplat=`ruby -e'print RUBY_PLATFORM'`
[ -d $rbplat ] || ln -sf i686-linux $rbplat

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/freeride
%{_prefix}/lib/freeride
