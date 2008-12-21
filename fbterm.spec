Summary:	Terminal emulator for framebuffer
Summary(pl.UTF-8):	Emulator terminala dla framebuffera
Name:		fbterm
Version:	1.3
Release:	0.2
License:	GPL v2
Group:		Applications/Graphics
Source0:	http://fbterm.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	12f52f60390576866ce9f7696779050d
URL:		http://code.google.com/p/fbterm/
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	libstdc++-devel
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

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/postshell
-/sbin/setcap 'cap_sys_tty_config+ep' /usr/bin/fbterm

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README 
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
