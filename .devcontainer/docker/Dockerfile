FROM mcr.microsoft.com/devcontainers/base:ubuntu22.04

RUN apt update \
    && apt install -y \
        vim \
        curl \
        gnupg \
        wget \
        software-properties-common \
    && rm -rf /var/lib/apt/lists/*

COPY --from=ghcr.io/astral-sh/uv:0.4 /uv /bin/uv
RUN uv python install 3.12
