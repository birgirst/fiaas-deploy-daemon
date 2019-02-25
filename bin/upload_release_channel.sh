#!/usr/bin/env bash

set -x

echo "publishing release channel metadata"
echo $1

cat <<EOF > release_channel.json
{
    "image": "fiaas/fiaas-deploy-daemon:$version",
    "build": "https://fiaas.semaphoreci.com/jobs/$SEMAPHORE_JOB_ID"
    "commit": "https://github.com/fiaas/fiaas-deploy-daemon/commit/$SEMAPHORE_GIT_SHA"
    "spec": "https://fiaas.github.com/releases/artifacts/$version/fiaas.yml",
    "updated": "$(date)"
}
EOF

cat release_channel.json
