module mux_2x1(
    input a, b, sel,
    output y
);

    assign y = sel ? a : b;

    //dump vcd
    initial begin
        $dumpfile("dump.vcd");
        $dumpvars(0, mux_2x1);
    end

endmodule


// TRUTH TABLE : 
//     +---+---+---+---+
//     | A | B | S | Y |
//     +---+---+---+---+
//     | 0 | 0 | 0 | 0 |
//     | 0 | 0 | 1 | 0 |
//     | 0 | 1 | 0 | 0 |
//     | 0 | 1 | 1 | 1 |
//     | 1 | 0 | 0 | 1 |
//     | 1 | 0 | 1 | 0 |
//     | 1 | 1 | 0 | 1 |
//     | 1 | 1 | 1 | 1 |
//     +---+---+---+---+