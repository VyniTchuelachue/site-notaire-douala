import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import App from "./App.jsx";
import fr from "./content/fr.js";
import en from "./content/en.js";
import "./index.css";

// La langue vient de la page HTML : index.html (fr) ou en/index.html (en).
const content = document.documentElement.lang === "en" ? en : fr;

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <App c={content} />
  </StrictMode>,
);
