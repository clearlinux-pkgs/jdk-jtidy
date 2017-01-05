Name     : jdk-jtidy
Version  : 1
Release  : 1
URL      : http://repo.maven.apache.org/maven2/net/sf/jtidy/jtidy/r938/jtidy-r938.jar
Source0  : http://repo.maven.apache.org/maven2/net/sf/jtidy/jtidy/r938/jtidy-r938.jar
Source1  : http://repo.maven.apache.org/maven2/net/sf/jtidy/jtidy/r938/jtidy-r938.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Zlib
Requires: jdk-jtidy-data
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%package data
Summary: data components for the jdk-jtidy package.
Group: Data

%description data
data components for the jdk-jtidy package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/java/jtidy.jar
mv %{SOURCE1} %{buildroot}/usr/share/maven-poms/jtidy.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/jtidy.xml \
%{buildroot}/usr/share/maven-poms/jtidy.pom \
%{buildroot}/usr/share/java/jtidy.jar \

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/jtidy.jar
/usr/share/maven-metadata/jtidy.xml
/usr/share/maven-poms/jtidy.pom
