module updown_counter (
    input wire clk,
    input wire rst,
    input wire up_down,  // 1 for up, 0 for down
    output reg [7:0] count
);

always @(posedge clk or posedge rst) begin
    if (rst) begin
        count <= 8'b0;
    end else if (up_down) begin
        count <= count + 1;
    end else begin
        count <= count - 1;
    end
end

endmodule
