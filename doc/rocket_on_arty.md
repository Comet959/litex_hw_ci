Intro
------

This essay describes how to use this repo to gengerate test for rocketchip with h-extension on arty-a7100T.

Quick Start
----------
First, clone this repo on your host.

Then,

```shell
python3 litex_hw_ci.py configs/test_linux_arty.py --config arty_rocket_1_core
```

**!Note:** You should insert the power and uart-usb line for you arty-100T before running the above command.

That you can see the launched riscv linux on your uart serial like `/dev/ttyUSB1`, use `sudo screen /dev/ttyUSB1 115200` to watch it on your host.