# revision 19440
# category Package
# catalog-ctan /macros/latex/contrib/susy
# catalog-date 2008-08-23 22:26:13 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-susy
Version:	20080823
Release:	8
Summary:	Macros for SuperSymmetry-related work
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/susy
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/susy.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/susy.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20080823-2
+ Revision: 756356
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20080823-1
+ Revision: 719614
- texlive-susy
- texlive-susy
- texlive-susy
- texlive-susy

