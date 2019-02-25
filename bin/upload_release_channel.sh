#!/usr/bin/env bash

set -x

echo "publishing release channel metadata"
echo $1

cat <<EOF > release_channel.json
{
    "image": "fiaas/fiaas-deploy-daemon:$version",
    "build": "https://travis.schibsted.io/finn/fiaas-deploy-daemon/builds/5965774",
    "commit": "https://github.schibsted.io/finn/fiaas-deploy-daemon/compare/d84df2e5dce5...2ace0ea22afa",
    "spec": "https://fiaas.github.com/releases/artifacts/$version/fiaas.yml",
    "updated": "$(date)"
}
EOF

cat release_channel.json
