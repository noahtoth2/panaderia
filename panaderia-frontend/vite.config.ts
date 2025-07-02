import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'

export default defineConfig({
  plugins: [svelte()],
  server: {
    host: '0.0.0.0',  // <-- Esto permite que cualquier dispositivo en la red acceda
    port: 5173        // <-- Puedes cambiarlo si lo deseas, pero este es el puerto por defecto
  }
})
