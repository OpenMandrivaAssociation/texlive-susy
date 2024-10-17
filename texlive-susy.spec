Name:		texlive-susy
Version:	19440
Release:	2
Summary:	Macros for SuperSymmetry-related work
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/susy
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/susy.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/susy.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides abbreviations of longer expressions.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/susy/susy.sty
%doc %{_texmfdistdir}/doc/latex/susy/README
%doc %{_texmfdistdir}/doc/latex/susy/README.TEXLIVE

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
