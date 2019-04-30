FROM freifeld/java:11

LABEL Maintainer="Royi Freifeld"

ENV RELEASE 2019-04-19_0642
ENV VERSION 19.0.0.4
ENV ARCHIVE_NAME openliberty-${VERSION}

ENV INSTALL_DIR /opt/openliberty
ENV OPENLIBERTY_HOME ${INSTALL_DIR}/${VERSION}
ENV DEFAULT_SERVER_DIR ${OPENLIBERTY_HOME}/usr/servers/defaultServer
ENV DEPLOYMENT_DIR ${DEFAULT_SERVER_DIR}/dropins

RUN mkdir -p /opt/openliberty/${VERSION} \
  && curl -O https://public.dhe.ibm.com/ibmdl/export/pub/software/openliberty/runtime/release/${RELEASE}/${ARCHIVE_NAME}.zip \
  && unzip ${ARCHIVE_NAME}.zip -d ${OPENLIBERTY_HOME} \
  && mv ${OPENLIBERTY_HOME}/wlp/* ${OPENLIBERTY_HOME} \
  && rm -rf ${OPENLIBERTY_HOME}/wlp \
  && rm ${ARCHIVE_NAME}.zip

ADD server.xml ${DEFAULT_SERVER_DIR}/

WORKDIR ${OPENLIBERTY_HOME}

EXPOSE 9080 9443
CMD [ "./bin/server" , "run", "defaultServer"]