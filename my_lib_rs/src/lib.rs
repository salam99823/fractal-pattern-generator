mod turtle;

use pyo3::prelude::*;
use std::collections::HashMap;
use turtle::Turtle;

fn is_draw_command(command: &String, command_dict: &HashMap<String, String>) -> bool {
    match command_dict.get(command) {
        None => false,
        Some(command) => command.starts_with("Draw"),
    }
}

#[pyfunction]
fn generate_lines(
    turtle_actions: Vec<(String, f64)>,
    command_dict: HashMap<String, String>,
    angle_of_rotation: f64,
) -> PyResult<(Vec<((f64, f64), (f64, f64))>, Vec<usize>)> {
    let mut turtle = Turtle::new(
        turtle_actions
            .iter()
            .filter(|(command, _)| is_draw_command(command, &command_dict))
            .count(),
    );
    let mut color_index: usize = 0;
    let mut color_indexes = Vec::with_capacity(turtle.lines.capacity());
    for (turtle_action, quantity) in turtle_actions {
        if let Some(act) = command_dict.get(&turtle_action) {
            match act.as_str() {
                "DrawForward" => {
                    turtle.forward(quantity);
                    color_indexes.push(color_index);
                }
                "DrawBack" => {
                    turtle.backward(quantity);
                    color_indexes.push(color_index);
                }
                "MoveForward" => {
                    turtle.move_forward(quantity);
                }
                "MoveBack" => {
                    turtle.move_backward(quantity);
                }
                "TurnRight" => {
                    turtle.right(angle_of_rotation * quantity);
                }
                "TurnLeft" => {
                    turtle.left(angle_of_rotation * quantity);
                }
                "ChangePenColor" => {
                    color_index += quantity.round() as usize;
                }
                _ => {}
            }
        }
    }
    Ok((turtle.lines, color_indexes))
}

/// A Python module implemented in Rust.
#[pymodule]
fn cpuboundfunctions(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(generate_lines, m)?)?;
    Ok(())
}
