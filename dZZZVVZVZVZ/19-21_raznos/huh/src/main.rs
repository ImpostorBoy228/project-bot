fn moves(s: u32, d: u32, res: &mut Vec<u32>) {
    if d==0 {
        res.push(s);
        return;
    }
    moves(s-3, d-1, res);
    moves(s-5,d-1, res);
    moves(s/4,d-1, res);
}

fn gmoves(s: u32, d: u32) -> Vec<u32> {
    let mut res = Vec::with_capacity(81);
    moves(s,d,&mut res);
    res
}

fn main() {
    
}
