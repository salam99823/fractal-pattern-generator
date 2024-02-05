pub struct Point {
    pub x_coordinate: f64,
    pub y_coordinate: f64,
}

impl Point {
    fn to_tuple(&self) -> (f64, f64) {
        (self.x_coordinate, self.y_coordinate)
    }
}

pub struct Turtle {
    start_point: Point,
    angle: f64,
    pub lines: Vec<((f64, f64), (f64, f64))>,
}

impl Turtle {
    pub fn new(lines_count: usize) -> Turtle {
        Turtle {
            start_point: Point {
                x_coordinate: 0.0,
                y_coordinate: 0.0,
            },
            angle: 0.0,
            lines: Vec::with_capacity(lines_count),
        }
    }
    fn end_point(&self, length: f64) -> Point {
        Point {
            x_coordinate: self.start_point.x_coordinate + length * self.angle.to_radians().cos(),
            y_coordinate: self.start_point.y_coordinate - length * self.angle.to_radians().sin(),
        }
    }
    pub fn get_line(&self, length: f64) -> ((f64, f64), (f64, f64)) {
        (
            self.start_point.to_tuple(),
            self.end_point(length).to_tuple(),
        )
    }
    pub fn forward(&mut self, quantity: f64) {
        self.lines.push(self.get_line(100. * quantity));
        self.move_forward(quantity);
    }
    pub fn backward(&mut self, quantity: f64) {
        self.lines.push(self.get_line(-100. * quantity));
        self.move_backward(quantity);
    }
    pub fn move_forward(&mut self, quantity: f64) {
        self.start_point = self.end_point(100. * quantity);
    }

    pub fn move_backward(&mut self, quantity: f64) {
        self.start_point = self.end_point(-100. * quantity);
    }

    pub fn right(&mut self, degrees: f64) {
        self.angle += degrees
    }
    pub fn left(&mut self, degrees: f64) {
        self.angle -= degrees
    }
}
