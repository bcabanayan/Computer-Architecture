"""CPU functionality."""

import sys



class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.registers = [0] * 8
        self.pc = 0
        self.running = True
        self.ops = {
            HLT: self.op_ldi,
            LDI: self.op_hlt,
            PRN: self.op_prn
        }

    def ram_read(self, MAR):
        return self.ram[MAR]

    def ram_write(self, MAR, MDR):
        self.ram[MAR] = MDR  

    def load(self, filename):
        """Load a program into memory."""
        
        address = 0

        # try:
        with open(filename) as file:
            for line in file:
                comment_split = line.split('#')
                instruction = comment_split[0]
                if instruction == '':
                    continue
                first_bit = instruction[0]
                if first_bit == '1' or first_bit == '0':
                    self.ram[address] = int(instruction[:8], 2)
                    address += 1

        # except IOError: #File Not Found Error
        #     print('I cannot find that file, check the name')
        #     sys.exit(2)

        # For now, we've just hardcoded a program:

        # program = [
        #     # From print8.ls8
        #     0b10000010, # LDI R0,8
        #     0b00000000,
        #     0b00001000,
        #     0b01000111, # PRN R0
        #     0b00000000,
        #     0b00000001, # HLT
        # ]

        # for instruction in program:
        #     self.ram[address] = instruction
        #     address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""

        # self.load()

        while self.running:
            IR = self.ram_read(self.pc)

            OP_A = self.ram_read(self.pc + 1)
            OP_B = self.ram_read(self.pc + 2)

            OP_SIZE = IR >> 6

            if IR == LDI:
                MAR = OP_A
                MDR = OP_B
                self.registers[MAR] = MDR
            elif IR == PRN:
                MAR = OP_A
                MDR = self.registers[MAR]
                print(MDR)
            elif IR == HLT:
                self.running = False
            
            self.pc += OP_SIZE + 1
            
# example print code

# file = open('./examples/print8.ls8')

# for line in file:
#     print(line)

# file.close()

# example print code, which closes file for us

# with open('./examples/print8.ls8') as file:
#     for line in file:
#         print(line)

# example printing with command line argument


# print(sys.argv)

# if len(sys.argv) != 2:
#     print('use like so: file-01.py filename')
#     print(sys.stderr)
#     sys.exit(1)

# IO Error == File Not Found Error

# try:
#     with open(sys.argv[1]) as file:
#         for line in file:
#             # print(line)
#             comment_split = line.split('#')
#             possible_number = comment_split[0]
#             if possible_number == '':
#                 continue
#             first_bit = possible_number[0]
#             if first_bit == '1' or first_bit == '0':
#                 x = int(possible_number[0:8], base = 2)
#                 print('{:b}, {:d}'.format(x, x))

# except IOError: #File Not Found Error
#     print('I cannot find that file, check the name')
#     sys.exit(2)