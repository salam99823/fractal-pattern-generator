import "./styles.css";
import App from "./App.svelte";

let target = document.getElementById("app");
if (target === null) {
  throw new Error("Cannot find application target. Please Check your HTML.");
}

const app = new App({
  target: target,
});

export default app;
