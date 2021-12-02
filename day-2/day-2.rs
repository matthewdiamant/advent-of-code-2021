fn parse_instruction(input: &str) -> (&str, i64) {
    let instruction = input.split(' ').collect::<Vec<&str>>();
    let direction = instruction[0];
    let value: i64 = instruction[1].parse().unwrap();
    return (direction, value);
}

fn solve_part_1(inputs: &Vec<String>) -> i64 {
    let mut horizontal = 0;
    let mut depth = 0;
    for input in inputs {
        let (direction, value) = parse_instruction(input);
        if direction == "up" {
            depth -= value;
        }
        if direction == "down" {
            depth += value;
        }
        if direction == "forward" {
            horizontal += value;
        }
    }
    return horizontal * depth;
}

fn solve_part_2(inputs: &Vec<String>) -> i64 {
    let mut horizontal = 0;
    let mut depth = 0;
    let mut aim = 0;
    for input in inputs {
        let (direction, value) = parse_instruction(input);
        if direction == "up" {
            aim -= value;
        }
        if direction == "down" {
            aim += value;
        }
        if direction == "forward" {
            horizontal += value;
            depth += aim * value;
        }
    }
    return horizontal * depth;
}

static INPUT: &str = include_str!("input.txt");
fn main() {
    let inputs: Vec<String> = INPUT.lines().map(|x| x.parse().unwrap()).collect();
    println!("{}", solve_part_1(&inputs));
    println!("{}", solve_part_2(&inputs));
}
