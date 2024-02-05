mod turtle;

use pyo3::exceptions::PyValueError;
use pyo3::prelude::{pyfunction, pymodule, wrap_pyfunction, PyModule, PyResult, Python};
use pyo3::types::PyIterator;
use std::collections::HashMap;
use turtle::Turtle;

#[pyfunction]
fn generate_lines(
    turtle_actions: &PyIterator,
    command_dict: HashMap<String, String>,
    angle_of_rotation: f64,
    lines_count: usize,
) -> PyResult<(Vec<((f64, f64), (f64, f64))>, Vec<usize>)> {
    let mut turtle = Turtle::new(lines_count);
    let mut color_index: usize = 0;
    let mut color_indexes = Vec::with_capacity(turtle.lines.capacity());
    for item in turtle_actions {
        let (turtle_action, quantity) = item?.extract::<(String, f64)>()?;
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
                some => return Err(PyValueError::new_err(format!("Invalid Command: {some}"))),
            }
        }
    }
    Ok((turtle.lines, color_indexes))
}

/// A Python module implemented in Rust.
#[pymodule]
fn cpuboundfunctions(_py: Python, module: &PyModule) -> PyResult<()> {
    module.add_function(wrap_pyfunction!(generate_lines, module)?)?;
    Ok(())
}
