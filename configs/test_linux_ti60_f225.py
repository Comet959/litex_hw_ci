#!/usr/bin/env python3

#
# This file is part of LiteX-HW-CI.
#
# Copyright (c) 2024 Enjoy-Digital <enjoy-digital.fr>
# SPDX-License-Identifier: BSD-2-Clause

from litex_hw_ci import LiteXCIConfig, LiteXCITest, get_local_ip

# LiteX CI Config Definitions ----------------------------------------------------------------------

# Notes:
# Tested configs:
# - VexRiscv 32-bit / Wishbone Bus.

linux_build_args = "--clean --build --generate-dtb --prepare-tftp --copy-images"

litex_ci_configs = {
    # Efinix Ti60F225 running VexRiscv 32-bit with:
    # - Wishbone Bus.
    # - 1 Core.
    # - FPU.
    # - Coherent DMA.
    # - 1Gbps Ethernet / 1000BaseX with SFP module.
    "ti60_f225_vexriscv_32_bit_1_core_wishbone" : LiteXCIConfig(
        target           = "efinix_titanium_ti60_f225_dev_kit",
        gateware_command = f"--sys-clk-freq 100e6 --cpu-type=vexriscv_smp --cpu-variant=linux --with-hyperram --bus-bursting",
        software_command = "cd linux && python3 make.py {output_dir}/soc.json " + linux_build_args,
        setup_command    = "",
        exit_command     = "",
        tty              = "/dev/ttyUSB1",
    ),
}
