# Copyright (c) 2017
#
# All rights reserved.
#
# This file is distributed under the Clear BSD license.
# The full text can be found in LICENSE in the root directory.

import common
import openwrt_router
import sys
import pexpect

class Qemu(openwrt_router.OpenWrtRouter):
    '''
    Emulated QEMU board
    '''

    wan_iface = "erouter0"
    lan_iface = "brlan0"

    # allowed open ports (starting point)
    wan_open_ports = ['22', '8080', '8087', '8088', '8090']

    def __init__(self,
                 model,
                 conn_cmd,
                 power_ip,
                 power_outlet,
                 output=sys.stdout,
                 password='bigfoot1',
                 web_proxy=None,
                 tftp_server=None,
                 tftp_username=None,
                 tftp_password=None,
                 tftp_port=None,
                 connection_type=None,
                 power_username=None,
                 power_password=None,
                 rootfs=None,
                 **kwargs):

        cmd = "%s %s" % (conn_cmd, rootfs)

        # spawn a simple bash shell for now, will launch qemu later
        pexpect.spawn.__init__(self, command='/bin/bash',
                        args=["-c", cmd])
        self.logfile_read = output
        self.expect("SYSLINUX")

    def wait_for_boot(self):
        pass

    def setup_uboot_network(self):
        pass

    def flash_rootfs(self, ROOTFS):
        pass

    def wait_for_linux(self):
        self.expect("login:")

    def boot_linux(self, rootfs=None, bootargs=None):
        pass

    def reset(self):
        self.sendcontrol('a')
        self.send('c')
        self.sendline('system_reset')
        self.expect('SYSLINUX')
        self.sendcontrol('a')
        self.send('c')