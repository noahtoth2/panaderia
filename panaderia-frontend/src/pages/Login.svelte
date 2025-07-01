<script>
  import { onMount } from 'svelte';
  import { push } from 'svelte-spa-router';

  let username = '';
  let password = '';
  let error = '';

  async function login() {
    try {
      const res = await fetch('http://localhost:8000/auth/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
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

<div class="w-full max-w-sm mx-auto mt-16">
  <h2 class="text-2xl font-bold mb-4 text-center">Iniciar Sesión</h2>

  {#if error}
    <p class="text-red-500 text-sm mb-2">{error}</p>
  {/if}

  <input
    type="text"
    bind:value={username}
    placeholder="Usuario"
    class="w-full border rounded px-3 py-2 mb-2"
  />

  <input
    type="password"
    bind:value={password}
    placeholder="Contraseña"
    class="w-full border rounded px-3 py-2 mb-2"
  />

  <button
    on:click={login}
    class="w-full bg-blue-600 text-white px-3 py-2 rounded hover:bg-blue-700"
  >
    Iniciar sesión
  </button>

  <!-- Enlace al registro -->
  <p class="mt-4 text-center text-sm">
    ¿No tienes cuenta?
    <a href="#/register" class="text-blue-600 hover:underline">Regístrate</a>
  </p>
</div>

<style>
  input, button {
    font-size: 1rem;
  }
</style>
