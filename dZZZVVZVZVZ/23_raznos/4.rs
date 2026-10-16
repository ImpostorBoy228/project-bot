fn f(x: i64,y: i64) -> i64 {
    if x>y { return 0 }
    if x==y { return 1 }
    if x==15 { return 0 }
    f(x+1,y)+f(x+2,y)
}

fn main() {
    println!("{}",f(3,9)*f(9,20));
}
