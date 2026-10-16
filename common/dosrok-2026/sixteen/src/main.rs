fn f(n: f64) -> f64 {
    if n<10.0 {
    return 3.0;
    } else {
        return (n+4.0)*f(n-5.0);
    }
}

fn main() {
    let res = (f(257487.0)/683.0 + 67.0*f(257477.0))/f(257472.0);
    println!("{:?}",res);
}
