Name:		texlive-crimsonpro
Version:	64565
Release:	1
Summary:	CrimsonPro fonts with LaTeX support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/crimsonpro
License:	ofl lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/crimsonpro.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/crimsonpro.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The CrimsonPro fonts are designed by Jacques Le Bailly and
derived from the Crimson Text fonts designed by Sebastian
Kosch. The family includes eight weights and italics for each
weight.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/crimsonpro
%{_texmfdistdir}/fonts/vf/public/crimsonpro
%{_texmfdistdir}/fonts/type1/public/crimsonpro
%{_texmfdistdir}/fonts/truetype/public/crimsonpro
%{_texmfdistdir}/fonts/tfm/public/crimsonpro
%{_texmfdistdir}/fonts/map/dvips/crimsonpro
%{_texmfdistdir}/fonts/enc/dvips/crimsonpro
%doc %{_texmfdistdir}/doc/fonts/crimsonpro

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
