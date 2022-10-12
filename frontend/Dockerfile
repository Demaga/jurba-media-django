FROM node:alpine AS deps
# Check https://github.com/nodejs/docker-node/tree/b4117f9333da4138b03a546ec926ef50a31506c3#nodealpine to understand why libc6-compat might be needed.
ENV CHOKIDAR_USEPOLLING=true

RUN apk add --no-cache libc6-compat
WORKDIR /frontend
COPY package.json package-lock.json ./
RUN npm install --frozen-lockfile


# Rebuild the source code only when needed
FROM node:alpine AS builder
WORKDIR /frontend
COPY . .
COPY --from=deps /frontend/node_modules ./node_modules
ARG NODE_ENV=devolpement
RUN echo ${NODE_ENV}
RUN NODE_ENV=${NODE_ENV} yarn build

FROM node:alpine AS runner
WORKDIR /frontend

COPY . /frontend/

EXPOSE 3000

