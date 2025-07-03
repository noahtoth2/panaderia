<script>
  import { push } from 'svelte-spa-router';
  import { User, Lock } from 'lucide-svelte';

  let username = '';
  let password = '';
  let error = '';

  async function login() {
    try {
      const res = await fetch('http://192.168.11.3:8000/auth/login', {
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

<div class="min-h-screen flex items-center justify-center bg-gradient-to-br from-orange-100 via-white to-blue-100 px-4">
  <div class="bg-white shadow-2xl rounded-3xl p-8 w-full max-w-md">
    <h2 class="text-3xl font-bold text-center text-gray-800 mb-6">Iniciar Sesión</h2>

    {#if error}
      <div class="text-red-600 text-sm text-center mb-4 animate-pulse">{error}</div>
    {/if}

    <div class="mb-4 relative">
      <input
        type="text"
        placeholder="Usuario"
        bind:value={username}
        class="w-full pl-10 pr-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-400 focus:outline-none text-sm"
      />
      <User class="absolute top-1/2 left-3 -translate-y-1/2 text-gray-400 w-5 h-5" />
    </div>

    <div class="mb-6 relative">
      <input
        type="password"
        placeholder="Contraseña"
        bind:value={password}
        class="w-full pl-10 pr-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-400 focus:outline-none text-sm"
      />
      <Lock class="absolute top-1/2 left-3 -translate-y-1/2 text-gray-400 w-5 h-5" />
    </div>

    <button
      on:click={login}
      class="w-full bg-gradient-to-r from-blue-500 to-orange-400 text-white font-semibold py-3 rounded-lg transition-transform hover:scale-105 active:scale-95 shadow-lg"
    >
      Iniciar sesión
    </button>

    <p class="mt-4 text-sm text-gray-700 text-center">
      ¿No tienes cuenta?
      <a href="#/register" class="text-blue-600 hover:underline font-semibold">Regístrate</a>
    </p>
  </div>
</div>