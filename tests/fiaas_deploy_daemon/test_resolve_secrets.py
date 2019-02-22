#!/usr/bin/env python
# -*- coding: utf-8

from __future__ import unicode_literals, absolute_import

import pytest

from fiaas_deploy_daemon.secrets import resolve_secrets

KEY = b"USAGE_REPORTING_KEY"


class TestSecrets(object):
    @pytest.fixture
    def secrets_dir(self, tmpdir_factory):
        yield tmpdir_factory.mktemp("secrets", numbered=True)

    def test_reads_files(self, secrets_dir):
        secrets_dir.join("usage-reporting-key").write(KEY)
        secrets = resolve_secrets(str(secrets_dir))
        assert secrets.usage_reporting_key == KEY

    def test_expects_filename_with_underscores_replaced_by_dashes(self, secrets_dir):
        secrets_dir.join("usage_reporting_key").write(KEY)
        secrets = resolve_secrets(str(secrets_dir))
        assert secrets.usage_reporting_key is None

    def test_ignores_missing_files(self, secrets_dir):
        secrets = resolve_secrets(str(secrets_dir))
        assert secrets.usage_reporting_key is None

    def test_ignores_extra_files(self, secrets_dir):
        secrets_dir.join("ignore-me").write("ignored")
        resolve_secrets(str(secrets_dir))

    def test_secrets_are_bytes(self, secrets_dir):
        secrets_dir.join("usage-reporting-key").write(KEY)
        secrets = resolve_secrets(str(secrets_dir))
        assert isinstance(secrets.usage_reporting_key, bytes)

    def test_secrets_are_stripped(self, secrets_dir):
        secrets_dir.join("usage-reporting-key").write(KEY + "\n")
        secrets = resolve_secrets(str(secrets_dir))
        assert secrets.usage_reporting_key == KEY
