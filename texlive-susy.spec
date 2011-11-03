# revision 19440
# category Package
# catalog-ctan /macros/latex/contrib/susy
# catalog-date 2008-08-23 22:26:13 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-susy
Version:	20080823
Release:	1
Summary:	Macros for SuperSymmetry-related work
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/susy
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/susy.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/susy.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package provides abbreviations of longer expressions.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/susy/susy.sty
%doc %{_texmfdistdir}/doc/latex/susy/README
%doc %{_texmfdistdir}/doc/latex/susy/README.TEXLIVE

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
