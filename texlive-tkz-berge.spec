# revision 22891
# category Package
# catalog-ctan /macros/latex/contrib/tkz/tkz-berge
# catalog-date 2011-06-06 00:03:44 +0200
# catalog-license lppl
# catalog-version 1.00c
Name:		texlive-tkz-berge
Version:	1.00c
Release:	1
Summary:	Macros for drawing graphs of graph theory
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tkz/tkz-berge
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tkz-berge.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tkz-berge.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a collection of useful macros for drawing
classic graphs of graph theory, or to make other graphs.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tkz-berge/tkz-arith.sty
%{_texmfdistdir}/tex/latex/tkz-berge/tkz-berge.sty
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/README
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/NamedGraphs.pdf
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Andrasfai.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Balaban.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Bipartite.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Bull.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Cage.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Chvatal.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Cocktail_Party.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Coxeter.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Crown.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-CubicSymmetric.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Desargues.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Doyle.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Dyck.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Folkman.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Foster.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Franklin.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Gray.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Groetzsch.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Harries.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Heawood.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Hypercube.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Koenisberg.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Levi.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-McGee.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Moebius.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Nauru.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Pappus.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Petersen.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Platonic.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Robertson.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Tutte.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-Wong.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-couverture.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/NamedGraphs-main.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/doc/latex/namedg.ist
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-1-1-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-1-2-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-1-3-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-10-1-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-10-2-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-11-1-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-11-2-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-11-3-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-11-4-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-12-1-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-12-2-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-12-3-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-12-4-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-13-1-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-13-2-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-13-3-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-13-4-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-14-1-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-15-1-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-15-2-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-15-3-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-16-0-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-17-1-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-17-2-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-17-3-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-18-1-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-18-2-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-19-1-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-2-1-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-2-2-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-2-3-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-2-4-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-20-1-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-20-2-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-21-0-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-21-1-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-21-2-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-22-1-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-22-2-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-22-3-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-23-1-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-23-2-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-23-3-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-23-4-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-23-5-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-23-6-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-23-7-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-24-1-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-24-2-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-24-3-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-25-1-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-25-2-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-25-3-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-25-4-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-25-5-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-25-6-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-25-7-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-25-8-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-25-9-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-26-1-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-26-10-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-26-11-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-26-12-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-26-13-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-26-14-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-26-2-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-26-3-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-26-4-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-26-5-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-26-6-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-26-7-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-26-8-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-26-9-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-27-1-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-27-2-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-27-3-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-27-4-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-28-1-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-29-1-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-3-1-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-3-2-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-3-3-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-4-0-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-6-1-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-6-2-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-7-1-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-7-2-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-7-3-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-7-4-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-7-5-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-8-1-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-8-2-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-8-3-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-9-1-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/latex/tkzNamed-9-2-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/examples/tkzpreamblenamed.ltx
%doc %{_texmfdistdir}/doc/latex/tkz-berge/NamedGraphs/readme-namedgraph.txt
%doc %{_texmfdistdir}/doc/latex/tkz-berge/examples/Grid.pdf
%doc %{_texmfdistdir}/doc/latex/tkz-berge/examples/gr-Circulant.pdf
%doc %{_texmfdistdir}/doc/latex/tkz-berge/examples/gr-Complet-16.pdf
%doc %{_texmfdistdir}/doc/latex/tkz-berge/examples/gr-edgeingraphmodloop.pdf
%doc %{_texmfdistdir}/doc/latex/tkz-berge/examples/grCLadder.pdf
%doc %{_texmfdistdir}/doc/latex/tkz-berge/examples/grDoubleMod.pdf
%doc %{_texmfdistdir}/doc/latex/tkz-berge/examples/grExtraChords.pdf
%doc %{_texmfdistdir}/doc/latex/tkz-berge/examples/grLadder.pdf
%doc %{_texmfdistdir}/doc/latex/tkz-berge/examples/grSQCycle.pdf
%doc %{_texmfdistdir}/doc/latex/tkz-berge/examples/grStar.pdf
%doc %{_texmfdistdir}/doc/latex/tkz-berge/examples/grWheel.pdf
%doc %{_texmfdistdir}/doc/latex/tkz-berge/examples/hypercube.pdf
%doc %{_texmfdistdir}/doc/latex/tkz-berge/examples/hypercube_simple.pdf
%doc %{_texmfdistdir}/doc/latex/tkz-berge/examples/hypercubed.pdf
%doc %{_texmfdistdir}/doc/latex/tkz-berge/examples/latex/Grid.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/examples/latex/gr-Circulant.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/examples/latex/gr-Complet-16.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/examples/latex/gr-edgeingraphmodloop.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/examples/latex/grCLadder.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/examples/latex/grDoubleMod.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/examples/latex/grExtraChords.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/examples/latex/grLadder.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/examples/latex/grSQCycle.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/examples/latex/grStar.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/examples/latex/grWheel.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/examples/latex/hypercube_simple.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/examples/latex/hypercubed.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/latex/TKZdoc-berge-classic.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/latex/TKZdoc-berge-installation.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/latex/TKZdoc-berge-macros-e.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/latex/TKZdoc-berge-macros.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/latex/TKZdoc-berge-main.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/latex/TKZdoc-berge-style.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/latex/TKZdoc-gr-installation.tex
%doc %{_texmfdistdir}/doc/latex/tkz-berge/latex/berge.ist
%doc %{_texmfdistdir}/doc/latex/tkz-berge/readme-tkz-berge.txt
%doc %{_texmfdistdir}/doc/latex/tkz-berge/tkz-berge-screen.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
