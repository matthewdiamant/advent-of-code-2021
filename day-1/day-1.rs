fn solve_part_1(input: &Vec<i64>) -> i64 {
    let mut count = 0;
    for idx in 1..input.len() {
        if input[idx] > input[idx - 1] {
            count += 1;
        }
    }
    return count;
}

fn solve_part_2(input: &Vec<i64>) -> i64 {
    let mut count = 0;
    for idx in 3..input.len() {
        if input[idx] > input[idx - 3] {
            count += 1;
        }
    }
    return count;
}

static INPUT: &str = include_str!("input.txt");
fn main() {
    let input: Vec<i64> = INPUT.lines().map(|x| x.parse().unwrap()).collect();
    println!("{}", solve_part_1(&input));
    println!("{}", solve_part_2(&input));
}
