FROM rehabstudio/nodejs-ffmpeg
MAINTAINER Ricky Dunlop <ricky@rehabstudio.com>

# Cairo
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
        libcairo2-dev \
        libjpeg8-dev \
        libpango1.0-dev \
        libgif-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

CMD ["node"]
