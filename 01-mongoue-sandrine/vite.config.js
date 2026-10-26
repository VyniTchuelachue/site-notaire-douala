import { resolve } from "node:path";
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import tailwindcss from "@tailwindcss/vite";

// Deux pages réelles (FR à la racine, EN dans /en/) pour que chaque langue
// ait son propre HTML, ses balises meta et une URL indexable.
// base "./" : le site fonctionne à la racine du domaine comme dans un sous-dossier.
export default defineConfig({
  base: "./",
  plugins: [react(), tailwindcss()],
  build: {
    rollupOptions: {
      input: {
        fr: resolve(import.meta.dirname, "index.html"),
        en: resolve(import.meta.dirname, "en/index.html"),
      },
    },
  },
});
