<script>
  import { onMount } from 'svelte';
  import { push } from 'svelte-spa-router';
  import Particles from 'tsparticles-svelte';

  let username = '';
  let password = '';
  let error = '';

  async function login() {
    try {
      const res = await fetch('http://localhost:8000/auth/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password }),
      });

      const data = await res.json();
      if (res.ok) {
        localStorage.setItem('token', data.access_token);
        push('/dashboard');
      } else {
        error = data.detail || 'Credenciales incorrectas';
      }
    } catch (err) {
      error = 'Error de conexión con el servidor';
    }
  }
</script>

<!-- Fondo de partículas -->
<Particles id="tsparticles" options={{
  fullScreen: { enable: true },
  background: { color: "#0f172a" },
  particles: {
    number: { value: 50 },
    color: { value: ["#f97316", "#3b82f6", "#ffffff"] },
    shape: { type: "circle" },
    opacity: { value: 0.8 },
    size: { value: 3 },
    move: { enable: true, speed: 1 },
  },
  interactivity: {
    events: {
      onHover: { enable: true, mode: "repulse" },
      onClick: { enable: true, mode: "push" }
    },
    modes: {
      repulse: { distance: 100 },
      push: { quantity: 4 }
    }
  },
  detectRetina: true
}} />

<!-- Caja de login -->
<div class="relative z-10 flex justify-center items-center min-h-screen">
  <div class="bg-white bg-opacity-90 p-8 rounded-2xl shadow-xl w-full max-w-sm text-center">
    <h2 class="text-3xl font-bold mb-6 text-gray-800">Iniciar Sesión</h2>

    {#if error}
      <p class="text-red-600 text-sm mb-4">{error}</p>
    {/if}

    <input
      type="text"
      bind:value={username}
      placeholder="Usuario"
      class="w-full mb-3 px-4 py-2 border rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-blue-400"
    />

    <input
      type="password"
      bind:value={password}
      placeholder="Contraseña"
      class="w-full mb-4 px-4 py-2 border rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-blue-400"
    />

    <button
      on:click={login}
      class="w-full bg-gradient-to-r from-blue-500 to-orange-400 text-white py-2 rounded-lg font-semibold transform transition hover:scale-105 active:scale-95 shadow-md hover:shadow-lg"
    >
      Iniciar sesión
    </button>

    <p class="mt-4 text-sm text-gray-700">
      ¿No tienes cuenta?
      <a href="#/register" class="text-blue-600 hover:underline">Regístrate</a>
    </p>
  </div>
</div>

<style>
  :global(body) {
    margin: 0;
    font-family: 'Segoe UI', sans-serif;
    overflow: hidden;
  }
</style>
