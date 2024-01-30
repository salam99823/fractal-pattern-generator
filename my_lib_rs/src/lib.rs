use pyo3::prelude::*;
use std::collections::HashMap;

struct Point {
    x_coordinate: f64,
    y_coordinate: f64,
}

struct Line {
    start_point: Point,
    length: f64,
    angle: f64,
}

impl Line {
    fn end_point(&self) -> Point {
        Point {
            x_coordinate: self.start_point.x_coordinate +
                self.length * self.angle.to_radians().cos(),
            y_coordinate: self.start_point.y_coordinate -
                self.length * self.angle.to_radians().sin(),
        }
    }
    fn to_vector(&self) -> Vec<f64> {
        let vector = vec![
            self.start_point.x_coordinate,
            self.start_point.y_coordinate,
            self.end_point().x_coordinate,
            self.end_point().y_coordinate,
        ];
        vector
    }
    fn _move(&mut self, quantity: f64) -> Vec<f64> {
        self.length *= quantity;
        let result = self.to_vector();
        self.start_point = self.end_point();
        self.length = 100.0;
        result
    }
}

#[pyfunction]
fn generate_lines(_actions: Vec<(String, f64)>,
                  command_dict: HashMap<String, String>,
                  angle_of_rotation: f64) -> PyResult<Vec<Vec<f64>>> {
    let size = _actions.iter().filter(
        |(command, _)| command_dict.get(command) == Some(&String::from("DrawForward")) || command_dict.get(command) == Some(&String::from("DrawBack"))
    ).count();
    println!("{}", size);
    let mut vector: Vec<Vec<f64>> = Vec::with_capacity(size);
    let mut line = Line {
        start_point: Point { x_coordinate: 0.0, y_coordinate: 0.0 },
        length: 100.0,
        angle: 0.0,
    };
    for (_action, quantity) in _actions {
        if let Some(act) = command_dict.get(&_action) {
            match act.as_str() {
                "DrawForward" => {
                    vector.push(line._move(quantity));
                }
                "DrawBack" => {
                    vector.push(line._move(quantity * -1.));
                }
                "MoveForward" => {
                    line._move(quantity);
                }
                "MoveBack" => {
                    line._move(quantity * -1.);
                }
                "TurnRight" => {
                    line.angle += angle_of_rotation * quantity;
                }
                "TurnLeft" => {
                    line.angle -= angle_of_rotation * quantity;
                }
                _ => {}
            }
        }
    }
    Ok(vector)
}


/// A Python module implemented in Rust.
#[pymodule]
fn cpuboundfunctions(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(generate_lines, m)?)?;
    Ok(())
}
