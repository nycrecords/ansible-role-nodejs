import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_nodejs_installed(host):
    nodejs = host.package("rh-nodejs12")

    assert nodejs.is_installed


def test_npm_installed(host):
    npm = host.package("rh-nodejs12-npm")

    assert npm.is_installed


def test_node_global_packages_installed(host):
    global_packages = host.run("npm -g list --depth 0")

    assert "jslint@0.12.0" in global_packages.stdout
    assert "node-sass@4.13.0" in global_packages.stdout
    assert "yo@3.1.1" in global_packages.stdout
