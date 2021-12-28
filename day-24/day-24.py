import math
import unittest

def do_math(operator, operand1, operand2):
    if operator == "add":
        return operand1 + operand2
    if operator == "mul":
        return operand1 * operand2
    if operator == "div":
        return math.floor(operand1 / operand2)
    if operator == "mod":
        return operand1 % operand2
    if operator ==  "eql":
        return 1 if operand1 == operand2 else 0

class ALU:

    registers = {
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0
    }

    model_number_pointer = 0

    def reset(self):
        self.registers["w"] = 0
        self.registers["x"] = 0
        self.registers["y"] = 0
        self.registers["z"] = 0
        self.model_number_pointer = 0

    def run_instruction(self, instruction, model_number):
        if not instruction:
            return
        instruction_parts = instruction.split(" ")
        instruction_name = instruction_parts[0]
        if instruction_name == "inp":
            input = model_number[self.model_number_pointer]
            register = instruction_parts[1]
            self.registers[register] = int(input)
            self.model_number_pointer += 1
        else:
            destination = instruction_parts[1]
            operand = instruction_parts[2]
            if operand in ["w", "x", "y", "z"]:
                value = self.registers[operand]
            else:
                value = int(operand)
            self.registers[destination] = do_math(instruction_name, self.registers[destination], value)


    def simplify(self, model_number):
        self.registers["z"] = ((int(model_number[0]) + 4) * 26 + int(model_number[1]) + 10) * 26 + int(model_number[2]) + 12
        self.registers["z"] = self.registers["z"] // 26 * 26 + int(model_number[3]) + 14

        self.registers["w"]

    def run_program(self, input, model_number):
        instructions = input.strip().split("\n")
        self.simplify(model_number)
        for instruction in instructions:
            self.run_instruction(instruction, model_number)

def solve(input):
    alu = ALU()
    d = {}
    # for model_number in range(99_999_999_999_999, -1, -1):
    for model_number in range(11_111_111_111_111, 99_999_999_999_999):
        if model_number % 10000 == 0:
            print(model_number, sorted(d.keys()))
        if "0" in str(model_number):
            continue
        alu.reset()
        alu.run_program(input, str(model_number))
        # print(model_number, alu.registers["z"])
        d[alu.registers["z"]] = d[alu.registers["z"]] + 1 if alu.registers["z"] in d else 1
        if alu.registers["z"] == 0:
            return model_number

    return alu.registers

with open("./input.txt") as f:
    input = f.read()

with open("./simple.txt") as f:
    simple = f.read()

class Test(unittest.TestCase):
    def test_solve_thing(self):
        alu = ALU()
        alu.reset()
        alu.run_program(simple, str(11_111_111_111_111))
        self.assertEqual(alu.registers, {'w': 1, 'x': 1, 'y': 9, 'z': 1682253257})
        alu.reset()
        alu.run_program(simple, str(22_222_222_222_222))
        self.assertEqual(alu.registers, {'w': 2, 'x': 1, 'y': 10, 'z': 2003525664})
        alu.reset()
        alu.run_program(simple, str(33_333_333_333_333))
        self.assertEqual(alu.registers, {'w': 3, 'x': 1, 'y': 11, 'z': 2324798071})
        alu.reset()
        alu.run_program(simple, str(44_444_444_444_444))
        self.assertEqual(alu.registers, {'w': 4, 'x': 1, 'y': 12, 'z': 2646070478})
        alu.reset()
        alu.run_program(simple, str(55_555_555_555_555))
        self.assertEqual(alu.registers, {'w': 5, 'x': 1, 'y': 13, 'z': 2967342885})
        alu.reset()
        alu.run_program(simple, str(66_666_666_666_666))
        self.assertEqual(alu.registers, {'w': 6, 'x': 1, 'y': 14, 'z': 3288615292})
        alu.reset()
        alu.run_program(simple, str(77_777_777_777_777))
        self.assertEqual(alu.registers, {'w': 7, 'x': 1, 'y': 15, 'z': 3609887699})
        alu.reset()
        alu.run_program(simple, str(88_888_888_888_888))
        self.assertEqual(alu.registers, {'w': 8, 'x': 1, 'y': 16, 'z': 3931160106})
        alu.reset()
        alu.run_program(simple, str(99_999_999_999_999))
        self.assertEqual(alu.registers, {'w': 9, 'x': 1, 'y': 17, 'z': 4252432513})

    def test_solve(self):
        # self.assertEqual(solve(input), None)
        pass

unittest.main()
