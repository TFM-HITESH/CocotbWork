import cocotb
from cocotb.result import TestSuccess
from cocotb.triggers import Timer

@cocotb.test()
#decorator to mark the start of the test
async def mux_test(dut):

    dut._log.info("\n<========================== START OF TEST ==========================>")
    
    #====================================================================================
    # a=0, b=0, sel=0
    await Timer(1, 'ns')

    dut.a.value = 0
    dut.b.value = 0
    dut.sel.value = 0
    dut._log.info = ("Driving a = 0, b = 0, s = 0 to inputs of 2x1 MUX")

    await Timer(1, 'ns')

    #checking if the output is correct
    if dut.y.value != 0:
        print('\n<====-!-!- RESULT IS INCORRECT -!-!-====>')
        assert dut.y.value == 0
    else:
        print('. . . PASS . . .')
        raise TestSuccess(". . . Value of OUTPUT . . . = ", dut.y.value.binstr)

    #====================================================================================
    # a=0, b=0, sel=1
    await Timer(1, 'ns')

    dut.a.value = 0
    dut.b.value = 0
    dut.sel.value = 1
    dut._log.info = ("Driving a = 0, b = 0, s = 1 to inputs of 2x1 MUX")

    await Timer(1, 'ns')

    #checking if the output is correct
    if dut.y.value != 0:
        print('\n<====-!-!- RESULT IS INCORRECT -!-!-====>')
        assert dut.y.value == 0
    else:
        print('. . . PASS . . .')
        raise TestSuccess(". . . Value of OUTPUT . . . = ", dut.y.value.binstr)

    #====================================================================================
    # a=0, b=1, sel=0
    await Timer(1, 'ns')

    dut.a.value = 0
    dut.b.value = 1
    dut.sel.value = 0
    dut._log.info = ("Driving a = 0, b = 1, s = 0 to inputs of 2x1 MUX")

    await Timer(1, 'ns')

    #checking if the output is correct
    if dut.y.value != 0:
        print('\n<====-!-!- RESULT IS INCORRECT -!-!-====>')
        assert dut.y.value == 0
    else:
        print('. . . PASS . . .')
        raise TestSuccess(". . . Value of OUTPUT . . . = ", dut.y.value.binstr)
    
    #====================================================================================
    # a=0, b=1, sel=1
    await Timer(1, 'ns')

    dut.a.value = 0
    dut.b.value = 1
    dut.sel.value = 1
    dut._log.info = ("Driving a = 0, b = 1, s = 1 to inputs of 2x1 MUX")

    await Timer(1, 'ns')

    #checking if the output is correct
    if dut.y.value != 1:
        print('\n<====-!-!- RESULT IS INCORRECT -!-!-====>')
        assert dut.y.value == 1
    else:
        print('. . . PASS . . .')
        raise TestSuccess(". . . Value of OUTPUT . . . = ", dut.y.value.binstr)
    
    #====================================================================================
    # a=1, b=0, sel=0
    await Timer(1, 'ns')

    dut.a.value = 1
    dut.b.value = 0
    dut.sel.value = 0
    dut._log.info = ("Driving a = 1, b = 0, s = 0 to inputs of 2x1 MUX")

    await Timer(1, 'ns')

    #checking if the output is correct
    if dut.y.value != 1:
        print('\n<====-!-!- RESULT IS INCORRECT -!-!-====>')
        assert dut.y.value == 1
    else:
        print('. . . PASS . . .')
        raise TestSuccess(". . . Value of OUTPUT . . . = ", dut.y.value.binstr)
    
    #====================================================================================
    # a=1, b=0, sel=1
    await Timer(1, 'ns')

    dut.a.value = 1
    dut.b.value = 0
    dut.sel.value = 1
    dut._log.info = ("Driving a = 1, b = 0, s = 1 to inputs of 2x1 MUX")

    await Timer(1, 'ns')

    #checking if the output is correct
    if dut.y.value != 0:
        print('\n<====-!-!- RESULT IS INCORRECT -!-!-====>')
        assert dut.y.value == 0
    else:
        print('. . . PASS . . .')
        raise TestSuccess(". . . Value of OUTPUT . . . = ", dut.y.value.binstr)
    
    #====================================================================================
    # a=1, b=1, sel=0
    await Timer(1, 'ns')

    dut.a.value = 1
    dut.b.value = 1
    dut.sel.value = 0
    dut._log.info = ("Driving a = 1, b = 1, s = 0 to inputs of 2x1 MUX")

    await Timer(1, 'ns')

    #checking if the output is correct
    if dut.y.value != 1:
        print('\n<====-!-!- RESULT IS INCORRECT -!-!-====>')
        assert dut.y.value == 1
    else:
        print('. . . PASS . . .')
        raise TestSuccess(". . . Value of OUTPUT . . . = ", dut.y.value.binstr)
    
    #====================================================================================
    # a=1, b=1, sel=1
    await Timer(1, 'ns')

    dut.a.value = 1
    dut.b.value = 1
    dut.sel.value = 1
    dut._log.info = ("Driving a = 1, b = 1, s = 1 to inputs of 2x1 MUX")

    await Timer(1, 'ns')

    #checking if the output is correct
    if dut.y.value != 1:
        print('\n<====-!-!- RESULT IS INCORRECT -!-!-====>')
        assert dut.y.value == 1
    else:
        print('. . . PASS . . .')
        raise TestSuccess(". . . Value of OUTPUT . . . = ", dut.y.value.binstr)