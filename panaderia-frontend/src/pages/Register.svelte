<script>
  import { User, Lock, ShieldCheck, KeyRound } from 'lucide-svelte';

  let username = "";
  let password = "";
  let adminPassword = "";
  let role = "ventas";

  let error = "";
  let success = "";
  let fieldErrors = {
    username: "",
    password: "",
    master_key: "",
    role: ""
  };

  const clearErrors = () => {
    error = "";
    success = "";
    fieldErrors = { username: "", password: "", master_key: "", role: "" };
  };

  const register = async () => {
    clearErrors();

    try {
      const response = await fetch("http://192.168.11.3:8000/auth/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          username,
          password,
          role,
          master_key: adminPassword
        })
      });

      const data = await response.json();

      if (response.ok) {
        success = "✅ Usuario registrado correctamente.";
        setTimeout(() => window.location.hash = "/", 2000);
      } else {
        if (response.status === 422 && Array.isArray(data.detail)) {
          data.detail.forEach(e => {
            const field = e.loc.at(-1);
            fieldErrors[field] = e.msg;
          });
        } else {
          error = data.detail || "Error en el registro.";
        }
      }
    } catch (err) {
      error = "Error al conectar con el servidor.";
    }
  };

  const goToLogin = () => {
    window.location.hash = "/";
  };
</script>

<div class="min-h-screen flex items-center justify-center bg-gradient-to-br from-orange-100 via-white to-blue-100 px-4">
  <div class="bg-white shadow-2xl rounded-3xl p-8 w-full max-w-md">
    <h2 class="text-3xl font-bold text-center text-gray-800 mb-6">Registrar Usuario</h2>

    {#if error}
      <div class="text-red-600 text-sm text-center mb-4 animate-pulse">{error}</div>
    {/if}
    {#if success}
      <div class="text-green-600 text-sm text-center mb-4 animate-bounce">{success}</div>
    {/if}

    <!-- Usuario -->
    <div class="mb-2 relative">
      <input
        type="text"
        placeholder="Nombre de usuario"
        bind:value={username}
        class="w-full pl-10 pr-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-400 focus:outline-none text-sm"
      />
      <User class="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400 w-5 h-5" />
    </div>
    {#if fieldErrors.username}
      <div class="text-red-500 text-xs mb-2">{fieldErrors.username}</div>
    {/if}

    <!-- Contraseña -->
    <div class="mb-2 relative">
      <input
        type="password"
        placeholder="Contraseña"
        bind:value={password}
        class="w-full pl-10 pr-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-400 focus:outline-none text-sm"
      />
      <Lock class="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400 w-5 h-5" />
    </div>
    {#if fieldErrors.password}
      <div class="text-red-500 text-xs mb-2">{fieldErrors.password}</div>
    {/if}

    <!-- Clave administrador -->
    <div class="mb-2 relative">
      <input
        type="password"
        placeholder="Clave de administrador"
        bind:value={adminPassword}
        class="w-full pl-10 pr-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-400 focus:outline-none text-sm"
      />
      <KeyRound class="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400 w-5 h-5" />
    </div>
    {#if fieldErrors.master_key}
      <div class="text-red-500 text-xs mb-2">{fieldErrors.master_key}</div>
    {/if}

    <!-- Selector de rol -->
    <div class="mb-4 relative">
      <select
        bind:value={role}
        class="w-full pl-10 pr-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-400 focus:outline-none text-sm"
      >
        <option value="administrador">Administrador</option>
        <option value="jefe_bodega">Jefe de Bodega</option>
        <option value="produccion">Producción</option>
        <option value="ventas">Ventas</option>
      </select>
      <ShieldCheck class="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400 w-5 h-5" />
    </div>
    {#if fieldErrors.role}
      <div class="text-red-500 text-xs mb-4">{fieldErrors.role}</div>
    {/if}

    <!-- Botón de registro -->
    <button
      on:click={register}
      class="w-full bg-gradient-to-r from-blue-500 to-orange-400 text-white font-semibold py-3 rounded-lg transition-transform hover:scale-105 active:scale-95 shadow-lg"
    >
      Registrar
    </button>

    <!-- Volver al login -->
    <p class="mt-4 text-sm text-gray-700 text-center">
      ¿Ya tienes cuenta?
      <button on:click={goToLogin} class="text-blue-600 hover:underline font-semibold">Iniciar sesión</button>
    </p>
  </div>
</div>
