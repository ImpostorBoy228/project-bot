use turtle::Turtle;

fn main() {
    let mut turtle = Turtle::new();
    for _ in 0..10 {
        let pos = turtle.position();
        turtle.go_to([pos.x+60.0,pos.y+156.0]);
        turtle.go_to([pos.x+140.0,pos.y-153.0]);
        turtle.go_to([71.0,80.0]);
        turtle.go_to([pos.x-111.0,pos.y+77.0]);
    }
    std::thread::park();
}
