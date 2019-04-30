FROM centos:7

LABEL Maintainer="Royi Freifeld"

ENV VERSION_MAJOR=12
ENV VERSION_MINOR=0.1
ENV VERSION_FULL=${VERSION_MAJOR}.${VERSION_MINOR}

RUN yum update -y \
  && mkdir /usr/lib/jvm/ \
  && yum -y install unzip \
  && curl -O https://download.oracle.com/java/GA/jdk${VERSION_FULL}/69cfe15208a647278a19ef0990eea691/${VERSION_MAJOR}/GPL/openjdk-${VERSION_FULL}_linux-x64_bin.tar.gz \
  && tar xvf openjdk-${VERSION_FULL}_linux-x64_bin.tar.gz -C /usr/lib/jvm/ \
  && yum clean all \
  && rm openjdk-${VERSION_FULL}_linux-x64_bin.tar.gz \
  && rm -rf /var/cache/yum
ENV JAVA_HOME /usr/lib/jvm/jdk-${VERSION_FULL}
ENV PATH "$PATH":/${JAVA_HOME}/bin:.: