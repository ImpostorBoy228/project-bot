fn f(n: i32) -> i32 {
    let nums: Vec<i32> = n
        .to_string()
        .chars()
        .filter_map(|c| c.to_digit(10))
        .map(|d| d as i32)
        .collect();
    let s: i32 = nums.iter().sum();
    let m = nums.iter().max().unwrap();
    let n = nums.iter().min().unwrap();
    let p1 = s - m;
    let p2 = s - n;
    format!("{p1}{p2}").parse().unwrap()
}

fn main() {
    for y in 0..129478 {
        if f(y) == 1318 {
            println!("{}", y);
        }
    }
}
