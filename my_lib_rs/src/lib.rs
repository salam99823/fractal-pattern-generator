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
    fn _move(&mut self, quantity: usize) -> Vec<f64> {
        self.length *= quantity;
        let result = self.to_vector();
        self.start_point = self.end_point();
        self.length = 100.0;
        result
    }
}

fn is_draw_command(command: &String, command_dict: &HashMap<String, String>) -> bool {
    match command_dict.get(command) {
        None => false,
        Some(command) => {
            command.starts_with("Draw")
        }
    }
}

fn count_draw_commands(commands: &Vec<(String, usize)>,
                       command_dict: &HashMap<String, String>,
) -> usize {
    let mut count = 0;
    for (_, quantity) in commands.iter().filter(
        |(command, _)|
            is_draw_command(command, command_dict)
    ) {
        count += quantity
    }
    count
}

fn count_draw_commands_(commands: &Vec<String>, command_dict: &HashMap<String, String>) -> usize {
    commands.iter().filter(
        |command|
            is_draw_command(command, command_dict)
    ).count()
}

#[pyfunction]
fn recurse_generate_lines(string: Vec<String>,
                          rules: Vec<(Vec<String>, Vec<String>)>,
                          number_of_iters: u32,
                          command_dict: HashMap<String, String>,
                          angle_of_rotation: f64,
) -> PyResult<Vec<Vec<f64>>> {
    let mut size = 0;
    for (key, value) in rules.iter() {
        size += (count_draw_commands_(value, &command_dict) /
            count_draw_commands_(key, &command_dict)).pow(number_of_iters) *
            count_draw_commands_(&string, &command_dict);
    }
    let mut vector: Vec<Vec<f64>> = Vec::with_capacity(size);
    fn generate_lines(vector: &mut Vec<Vec<f64>>,
                      string: Vec<String>,
                      rules: Vec<(Vec<String>, Vec<String>)>,
                      number_of_iters: u32,
                      command_dict: HashMap<String, String>,
                      angle_of_rotation: f64) -> Vec<Vec<f6>> {
        for act in string.iter() {
            if is_draw_command(act, &command_dict) {
                let mut line = Line {
                    start_point: Point {
                        x_coordinate: 0.0,
                        y_coordinate: 0.0,
                    },
                    length: 100.0,
                    angle: angle_of_rotation,
                };
                for (key, value) in rules.iter() {
                    if is_draw_command(act, &command_dict) {
                        for _ in 0..(count_draw_commands_(value, &command_dict) /
                            count_draw_commands_(key, &command_dict)).pow(number_of_iters) *
                            count_draw_commands_(&string, &command_dict) {
                            vector.push(line._move(1));
                        }
                    }
                }
            }
        }
    }
    Ok(vector)
}

#[pyfunction]
fn recurse_multiplier(string: String,
                      rules: Vec<(String, String)>,
                      number_of_iters: usize,
) -> PyResult<String> {
    let mut string = String::from(string);
    for _ in 0..number_of_iters {
        for (key, value) in rules.iter() {
            string = string.replace(key, value);
        };
    };
    Ok(string)
}

#[pyfunction]
fn generate_lines(_actions: Vec<(String, usize)>,
                  command_dict: HashMap<String, String>,
                  angle_of_rotation: f64) -> PyResult<Vec<Vec<f64>>> {
    let mut vector: Vec<Vec<f64>> = Vec::with_capacity(count_draw_commands(&_actions, &command_dict));
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
    m.add_function(wrap_pyfunction!(recurse_multiplier, m)?)?;
    Ok(())
}
