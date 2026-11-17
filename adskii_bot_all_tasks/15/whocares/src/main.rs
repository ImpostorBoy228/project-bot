use rayon::iter::{IntoParallelIterator, ParallelIterator};

fn forall(a: u64) -> bool {
    for x in 0..212_405 {
        for y in 0..124_150 {
            if (3*x+y)>=a {
                return false;
            }
        }
    }
    return true;
}

fn main() {
    let a: Vec<u64> = (0..1_000_000).into_par_iter().filter(|&x| forall(x)).collect();
    for t in a{
        println!("{}", t);
    }
    
}
