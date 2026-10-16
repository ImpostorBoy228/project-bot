fn moves(s: i32) -> Vec<i32> {
    vec![s-3,s-7,s/4 as i32]
}

fn g(s: i32,c: i32) -> bool {
    if s <= 15 {
        return c%2==0
    }
    let m = vec![g(s-3,c+1),g(s-7,c+1),g(s/4 as i32, c+1)];
    if c%2==0 {
        return m.iter().all(|&a| a)
    } else {
        return m.iter().any(|&a| a)
    }
    
}

fn main() {
    let mut c=0;
    for i in 0..500 {
        if g(i, 1) {
            c+=1
        }
    }
    println!("{}",c);
}
