#!/usr/bin/env python
# -*- coding: utf-8

from distutils.version import StrictVersion

from .common import has_utility, LinuxDriver


# In version 0.20, the none-driver is supposed to work, but in general it segfaults
# and does weird things as root, so it doesn't look like it's ready yet.
class NoneDriver(LinuxDriver):
    name = "none"
    arguments = ("--vm-driver", "none")

    def supported(self, minikube_version):
        if minikube_version < StrictVersion("0.20"):
            return has_utility("systemctl") and has_utility("docker")
        return has_utility("docker")
