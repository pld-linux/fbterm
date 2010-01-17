Summary:	Terminal emulator for framebuffer
Summary(pl.UTF-8):	Emulator terminala dla framebuffera
Name:		fbterm
Version:	1.6
Release:	4
License:	GPL v2
Group:		Applications/Graphics
Source0:	http://fbterm.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	531ea0984836b58fd123e6a97a4228c6
Patch0:		%{name}-install.patch
Patch1:		%{name}-font-lang.patch
URL:		http://code.google.com/p/fbterm/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	gpm-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	ncurses
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FbTerm is a fast terminal emulator for linux with frame buffer device.
Features include:
- mostly as fast as terminal of linux kernel while accelerated
  scrolling is enabled on framebuffer device
- select font with fontconfig and draw text with freetype2, same as
  Qt/Gtk+ based GUI apps
- dynamicly create/destroy up to 10 windows initially running default
  shell
- record scrollback history for every window
- auto-detect text encoding with current locale, support double width
  scripts like Chinese, Japanese etc
- switch between configurable additional text encodings with hot keys
  on the fly
- copy/past selected text between windows with mouse when gpm server
  is running

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}
tic -o terminfo terminfo/fbterm

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/terminfo/f
install terminfo/f/fbterm $RPM_BUILD_ROOT%{_datadir}/terminfo/f

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/postshell
-/sbin/setcap 'cap_sys_tty_config+ep' %{_bindir}/fbterm

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/terminfo/f/fbterm
%{_mandir}/man1/*
