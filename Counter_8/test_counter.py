import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer

@cocotb.test()
async def test_up_counter(dut):
    """Test the 8-bit up counter."""

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

    # Wait for a few clock cycles and check the count value
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

    # Let the counter run for another 10 cycles
    for i in range(1, 11):
        await RisingEdge(dut.clk)
        assert dut.count.value == i, f"Count is not as expected after reset! Expected: {i}, Got: {int(dut.count.value)}"

    # Print the final counter value
    print(f"Final count value: {int(dut.count.value)}")
