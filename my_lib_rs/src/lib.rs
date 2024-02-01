use pyo3::exceptions::PyTypeError;
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
            x_coordinate: self.start_point.x_coordinate
                + self.length * self.angle.to_radians().cos(),
            y_coordinate: self.start_point.y_coordinate
                - self.length * self.angle.to_radians().sin(),
        }
    }
    fn to_tuple(&self) -> (f64, f64, f64, f64) {
        (
            self.start_point.x_coordinate,
            self.start_point.y_coordinate,
            self.end_point().x_coordinate,
            self.end_point().y_coordinate,
        )
    }
    fn _move(&mut self, quantity: f64) -> (f64, f64, f64, f64) {
        let save = self.length;
        self.length *= quantity;
        let result = self.to_tuple();
        self.start_point = self.end_point();
        self.length = save;
        result
    }
}

#[pyclass]
enum Actions {
    DrawForward,
    DrawBack,
    MoveForward,
    MoveBack,
    TurnLeft,
    TurnRight,
}

impl<'a> FromPyObject<'a> for Actions {
    fn extract(obj: &'a PyAny) -> PyResult<Self> {
        let action: Actions = match obj.to_string().as_str() {
            "Actions.DrawForward" => Actions::DrawForward,
            "Actions.DrawBack" => Actions::DrawBack,
            "Actions.MoveForward" => Actions::MoveForward,
            "Actions.MoveBack" => Actions::MoveBack,
            "Actions.TurnLeft" => Actions::TurnLeft,
            "Actions.TurnRight" => Actions::TurnRight,
            _ => return Err(PyTypeError::new_err(format!("Invalid action: {}", obj))),
        };
        Ok(action)
    }
}

fn is_draw_command(command: &String, command_dict: &HashMap<String, Actions>) -> bool {
    match command_dict.get(command) {
        None => false,
        Some(command) => match command {
            Actions::DrawForward => true,
            Actions::DrawBack => true,
            _ => false,
        },
    }
}

fn count_draw_commands(
    commands: &Vec<(String, isize)>,
    command_dict: &HashMap<String, Actions>,
) -> usize {
    let mut count = 0;
    for (_, quantity) in commands
        .iter()
        .filter(|(command, _)| is_draw_command(command, command_dict))
    {
        count += quantity.abs() as usize;
    }
    count
}

#[pyfunction]
fn multiply_recursively(
    mut string: String,
    rules: Vec<(String, String)>,
    number_of_iters: usize,
) -> PyResult<String> {
    for _ in 0..number_of_iters {
        for (key, value) in rules.iter() {
            string = string.replace(key, value);
        }
    }
    Ok(string)
}

#[pyfunction]
fn generate_lines(
    _actions: Vec<(String, isize)>,
    command_dict: HashMap<String, Actions>,
    angle_of_rotation: f64,
) -> PyResult<Vec<(f64, f64, f64, f64)>> {
    let mut vector: Vec<(f64, f64, f64, f64)> =
        Vec::with_capacity(count_draw_commands(&_actions, &command_dict));
    let mut line = Line {
        start_point: Point {
            x_coordinate: 0.0,
            y_coordinate: 0.0,
        },
        length: 100.0,
        angle: 0.0,
    };
    for (_action, quantity) in _actions {
        if let Some(act) = command_dict.get(&_action) {
            match act {
                Actions::DrawForward => {
                    vector.push(line._move(quantity as f64));
                }
                Actions::DrawBack => {
                    vector.push(line._move(quantity as f64 * -1.));
                }
                Actions::MoveForward => {
                    line._move(quantity as f64);
                }
                Actions::MoveBack => {
                    line._move(quantity as f64 * -1.);
                }
                Actions::TurnRight => {
                    line.angle += angle_of_rotation * quantity as f64;
                }
                Actions::TurnLeft => {
                    line.angle -= angle_of_rotation * quantity as f64;
                }
            }
        }
    }
    Ok(vector)
}

/// A Python module implemented in Rust.
#[pymodule]
fn cpuboundfunctions(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(generate_lines, m)?)?;
    m.add_function(wrap_pyfunction!(multiply_recursively, m)?)?;
    m.add_class::<Actions>()?;
    Ok(())
}
