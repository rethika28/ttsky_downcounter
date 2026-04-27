import cocotb
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_downcounter(dut):

    # Init
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.ena.value = 1
    dut.clk.value = 0
    dut.rst_n.value = 0

    # Clock
    async def clock():
        while True:
            dut.clk.value = 0
            await Timer(5, units="ns")
            dut.clk.value = 1
            await Timer(5, units="ns")

    cocotb.start_soon(clock())

    # Reset release
    await Timer(20, units="ns")
    dut.rst_n.value = 1

    # Enable counter
    dut.ui_in.value = 1

    # Stabilize
    for _ in range(3):
        await RisingEdge(dut.clk)

    await RisingEdge(dut.clk)
    await Timer(1, units="ns")

    prev = dut.uo_out.value.integer & 0xF
    print(f"Initial = {prev}")

    # Check decrement
    for i in range(10):
        await RisingEdge(dut.clk)
        await Timer(1, units="ns")

        curr = dut.uo_out.value.integer & 0xF
        expected = (prev - 1) % 16

        print(f"Cycle {i}: prev={prev}, curr={curr}, expected={expected}")

        assert curr == expected, f"Mismatch at cycle {i}"

        prev = curr

    # Disable check
    dut.ui_in.value = 0
    hold = dut.uo_out.value.integer & 0xF

    for _ in range(3):
        await RisingEdge(dut.clk)
        curr = dut.uo_out.value.integer & 0xF
        assert curr == hold

    print("PASS ✅")
