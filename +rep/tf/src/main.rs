use std::{fs, path::Path};

fn main() {
    let seq = fs::read_to_string(Path::new("24_3.lol")).unwrap();
    let mut last = 'C';
    let mut c = 0;
    let mut ma = 0;
    for s in seq.chars() {
        if (last == 'A' && s == 'B') || (last == 'B' && s == 'A') {
            c += 1;
            ma = c.max(ma);
        } else {
            c = 0;
        }
        last = s;
    }
    println!("{ma}");
}
