fn can_break(n: u32) -> u32 {
    for o in (103..n).step_by(206) {
        for t in 1..((n as f64).log(3.0) as i32) {
            if o + 3_u32.pow(t as u32) == n {
                return t as u32;
            }
        }
    }
    1337 // 3**1337 это ужасно много
}
fn main() {
    for n in 100_000..1_000_000 {
        let t = can_break(n);
        if n.to_string().contains("1") || t == 1337 {
            continue;
        }
        println!("{n} {t}");
    }
}
