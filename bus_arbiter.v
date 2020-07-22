`resetall
`timescale 1ns/10ps
module test719a(clk, rst_n, signal_a, signal_b, signal_c, grant);
// I/O definition
input      clk;
input      rst_n;
input      signal_a;
input      signal_b;
input      signal_c;
output   [1:0] grant;
// register definition
reg   [1:0] grant;
reg  [1:0] ls;
// parameter definition
parameter   s_null = 3'b000,
            s_a    = 3'b100,
            s_b    = 3'b010,
            s_c    = 3'b001,
            s_ab   = 3'b110,
            s_bc   = 3'b001,
            s_ac   = 3'b101,
            s_abc  = 3'b111;
//module part and FSM
always @(posedge clk or negedge rst_n)
if(!rst_n)// bus disable when negtive rst_n
begin
grant <= 2'b11;
//cs <= s_null;
ls <= s_null;
end
else
begin
case({signal_a, signal_b, signal_c})// bus enable with FSM
  s_null:
     begin
        grant <= 2'b00;
        ls <= s_a;
     end
  s_a:
     begin
        grant <= 2'b00;
        ls <= s_a;          //////?
     end
  s_b:
     begin
        grant <= 2'b01;
        ls <= s_b;
     end
  s_c:
     begin
        grant <= 2'b10;
        ls <= s_c;
     end
  s_ab:
     begin
        grant <= 2'b00;
        ls <= s_a;
     end
  s_bc:
     begin
        grant <= 2'b01;
        ls <= s_b;
     end
  s_ac:
     begin
        grant <= 2'b00;
        ls <= s_a;
     end
  s_abc:
    begin
        grant <= 2'b00;
        ls <= s_a;
     end
  default:
  begin grant <= 2'b00; ls <= s_a; end
            
endcase
end
endmodule
