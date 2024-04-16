import "./styles.css";
import App from "./App.svelte";

let target = document.getElementById("app");
if (target === null) {
  target = document.createElement("div");
  target.id = "app";
  document.body.appendChild(target);
}

const app = new App({
  target: target,
});

export default app;
