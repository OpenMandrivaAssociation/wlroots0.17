%define major 11
%define libname %mklibname wlroots0.16 %{major}
%define devname %mklibname -d wlroots0.16
#define snapshot 20211107

Name:		wlroots0.16
Version:	0.16.2
Release:	1
Summary:	Compat package wlroots016.A modular Wayland compositor library
License:	MIT
URL:		https://gitlab.freedesktop.org/wlroots/wlroots/
Source0:	https://gitlab.freedesktop.org/wlroots/wlroots/-/archive/%{version}/wlroots-%{version}.tar.bz2

BuildRequires:	pkgconfig(libcap)
BuildRequires:	pkgconfig(libinput)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(xwayland)
BuildRequires:	pkgconfig(libseat)
BuildRequires:	meson
BuildRequires:	hwdata
BuildRequires:	pkgconfig(pixman-1)
BuildRequires:	pkgconfig(freerdp2)
BuildRequires:	pkgconfig(systemd)
BuildRequires:	pkgconfig(gbm)
BuildRequires:	pkgconfig(egl)
BuildRequires:	pkgconfig(glesv2)
BuildRequires:	pkgconfig(libudev)
BuildRequires:	pkgconfig(systemd)
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(xcb-errors)
BuildRequires:	pkgconfig(libglvnd)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(wayland-egl)
BuildRequires:	pkgconfig(wayland-protocols)
BuildRequires:	pkgconfig(wayland-scanner)
BuildRequires:	pkgconfig(wayland-server)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:	pkgconfig(libavutil)
BuildRequires:	pkgconfig(xcb)
BuildRequires:	pkgconfig(x11-xcb)
BuildRequires:	pkgconfig(xcb-icccm)
BuildRequires:	pkgconfig(uuid)
BuildRequires:	pkgconfig(xcb-renderutil)
BuildRequires:  glslang

%description
%{summary}.

%package -n %{libname}
Summary:	Library files for %{name}

%description -n %{libname}
A modular Wayland compositor library.

%package -n %{devname}
Summary:	Development files for %{name}
Requires:	%{libname} = %{EVRD}
Requires:	pkgconfig(libinput)
Requires:	pkgconfig(xcb)
Requires:	pkgconfig(xkbcommon)
Requires:	pkgconfig(pixman-1)
Requires:	pkgconfig(wayland-protocols)
Requires:	pkgconfig(xcb-icccm)

%description -n %{devname}
Development files for %{name}.

%prep
%autosetup -p1 %{?snapshot:-n %{name}-master}

%build
%meson  \
        -Dxcb-errors=disabled \
        -Dexamples=false
%meson_build

%install
%meson_install

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}*

%files -n %{devname}
%{_includedir}/wlr
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
