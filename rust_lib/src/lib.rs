use pyo3::prelude::*;

#[pyfunction]
fn hello() {
    let str = "Hello, world!".to_string();
    println!("{}", str);
}

#[pymodule]
fn poly_match_rs(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(hello, m)?)?;
    Ok(())
}
