import cocotb
from cocotb.triggers import RisingEdge, Timer

# Clock generation coroutine
@cocotb.coroutine
def clock_gen(clk):
    while True:
        clk <= 0
        yield Timer(5, units='ns')
        clk <= 1
        yield Timer(5, units='ns')

@cocotb.coroutine
def reset_dut(rst, duration_ns):
    rst <= 1
    yield Timer(duration_ns, units='ns')
    rst <= 0
    rst._log.info("Reset complete")

@cocotb.coroutine
def set_up_down(dut, value):
    dut.up_down <= value
    yield RisingEdge(dut.clk)

@cocotb.coroutine
def check_count(dut, expected_value):
    yield RisingEdge(dut.clk)
    if dut.count == expected_value:
        dut._log.info(f"Count match: expected {expected_value}, got {int(dut.count)}")
    else:
        dut._log.info(f"Count mismatch: expected {expected_value}, got {int(dut.count)}")

@cocotb.test()
def counter_testbench(dut):
    """Testbench for the up-down counter"""

    # Start clock
    cocotb.fork(clock_gen(dut.clk))

    # Reset the DUT
    yield reset_dut(dut.rst, 20)

    # Test counting up
    yield set_up_down(dut, 1)
    yield check_count(dut, 1)  # Count up to 1
    yield set_up_down(dut, 1)
    yield check_count(dut, 2)  # Count up to 2
    yield set_up_down(dut, 1)
    yield check_count(dut, 3)  # Count up to 3

    # Test counting down
    yield set_up_down(dut, 0)
    yield check_count(dut, 2)  # Count down to 2
    yield set_up_down(dut, 0)
    yield check_count(dut, 1)  # Count down to 1
    yield set_up_down(dut, 0)
    yield check_count(dut, 0)  # Count down to 0

    # Test reset
    yield reset_dut(dut.rst, 20)
    yield check_count(dut, 0)  # Count should be 0 after reset
    yield set_up_down(dut, 1)
    yield check_count(dut, 1)  # After reset, count should start at 1
