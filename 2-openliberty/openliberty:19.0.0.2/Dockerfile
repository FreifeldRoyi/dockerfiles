FROM freifeld/java:11

LABEL Maintainer="Royi Freifeld"

ENV RELEASE 2019-02-22_1311
ENV VERSION 19.0.0.2
ENV ARCHIVE_NAME openliberty-${VERSION}

ENV INSTALL_DIR /opt/openliberty
ENV OPENLIBERTY_HOME ${INSTALL_DIR}/${VERSION}
ENV DEPLOYMENT_DIR ${OPENLIBERTY_HOME}/standalone/deployments


RUN mkdir -p /opt/openliberty/${VERSION} \
    && curl -O https://public.dhe.ibm.com/ibmdl/export/pub/software/openliberty/runtime/release/${RELEASE}/${ARCHIVE_NAME}.zip \
    && unzip ${ARCHIVE_NAME}.zip -d ${INSTALL_DIR} \
    && rm ${ARCHIVE_NAME}.zip

EXPOSE 9080 9443