use pyo3::prelude::*;

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
        let point = Point {
            x_coordinate: self.start_point.x_coordinate +
                self.length * self.angle.to_radians().cos(),
            y_coordinate: self.start_point.y_coordinate -
                self.length * self.angle.to_radians().sin(),
        };
        point
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
}

fn _move(quantity: f64, line: &mut Line) -> Vec<f64> {
    line.length *= quantity;
    let result = line.to_vector();
    line.start_point = line.end_point();
    line.length = 100.0;
    return result;
}

#[pyfunction]
fn generate_lines(commands: Vec<(String, f64)>,
                  command_dict: Vec<String>,
                  angle_of_rotation: f64) -> PyResult<Vec<Vec<f64>>> {
    let mut result: Vec<Vec<f64>> = Vec::new();
    let mut line = Line {
        start_point: Point { x_coordinate: 0.0, y_coordinate: 0.0 },
        length: 100.0,
        angle: 0.0,
    };
    let _forward = command_dict.get(0).unwrap_or(&String::from("")).to_string();
    let _back = command_dict.get(1).unwrap_or(&String::from("")).to_string();
    let _move_forward = command_dict.get(2).unwrap_or(&String::from("")).to_string();
    let _move_back = command_dict.get(3).unwrap_or(&String::from("")).to_string();
    let _right = command_dict.get(4).unwrap_or(&String::from("")).to_string();
    let _left = command_dict.get(5).unwrap_or(&String::from("")).to_string();
    for (command, quantity) in commands {
        match command {
            _forward => {
                result.push(_move(quantity, &mut line)); // Draw Forward
            }
            _back => {
                result.push(_move(quantity * -1., &mut line)); // Draw Back
            }
            _move_forward => {
                _move(quantity, &mut line);
            }
            _move_back => {
                _move(quantity * -1., &mut line);
            }
            _right => {
                line.angle += angle_of_rotation * quantity; // Right
            }
            _left => {
                line.angle -= angle_of_rotation * quantity; // Left
            }
        }
    }
    return Ok(result);
}


/// A Python module implemented in Rust.
#[pymodule]
fn my_lib_rs(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(generate_lines, m)?)?;
    Ok(())
}
