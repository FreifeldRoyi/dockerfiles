FROM centos:7

LABEL Maintainer="Royi Freifeld"

ENV VERSION=11.0.2
RUN yum update -y \
  && mkdir /usr/lib/jvm/ \
  && yum -y install unzip \
  && curl -O https://download.java.net/java/GA/jdk11/9/GPL/openjdk-${VERSION}_linux-x64_bin.tar.gz \
  && tar xvf openjdk-${VERSION}_linux-x64_bin.tar.gz -C /usr/lib/jvm/ \
  && yum clean all \
  && rm openjdk-${VERSION}_linux-x64_bin.tar.gz \
  && rm -rf /var/cache/yum
ENV JAVA_HOME /usr/lib/jvm/jdk-${VERSION}
ENV PATH "$PATH":/${JAVA_HOME}/bin:.: