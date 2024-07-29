import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_up_down_counter(dut):
    """Test the 8-bit up-down counter."""

    # Create a 10ns period clock on port clk
    clock = Clock(dut.clk, 10, units="ns")  # 10ns period clock
    cocotb.start_soon(clock.start())  # Start the clock

    # Apply initial reset
    dut.rst.value = 1
    await RisingEdge(dut.clk)
    dut.rst.value = 0
    await RisingEdge(dut.clk)

    # Initialize count to zero
    assert dut.count.value == 0, f"Initial count is not zero! Got: {int(dut.count.value)}"

    # Test the counter in up mode
    dut.up_down.value = 1  # Set to count up
    for i in range(1, 11):
        await RisingEdge(dut.clk)
        assert dut.count.value == i, f"Count is not as expected! Expected: {i}, Got: {int(dut.count.value)}"

    # Apply reset in the middle of counting
    dut.rst.value = 1
    await RisingEdge(dut.clk)
    dut.rst.value = 0
    await RisingEdge(dut.clk)

    # Check if the counter is reset to zero
    assert dut.count.value == 0, f"Counter did not reset! Got: {int(dut.count.value)}"
    dut._log.info(f"After reset: count = {int(dut.count.value)}, expected = 0")

    # Test the counter in down mode
    dut.up_down.value = 0  # Set to count down
    for i in range(10, 0, -1):
        await RisingEdge(dut.clk)
        assert dut.count.value == i, f"Count is not as expected! Expected: {i}, Got: {int(dut.count.value)}"

    # Print the final counter value
    dut._log.info(f"Final count value: {int(dut.count.value)}")
