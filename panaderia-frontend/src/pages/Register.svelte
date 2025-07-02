<script>
  let username = "";
  let password = "";
  let adminPassword = "";
  let role = "ventas"; // valor por defecto

  let error = "";
  let success = "";

  const register = async () => {
    error = "";
    success = "";

    const response = await fetch("http://localhost:8000/auth/register", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
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
      setTimeout(() => window.location.hash = "/", 2000); // redirige al login
    } else {
      error = data.detail || "Error en el registro.";
    }
  };

  const goToLogin = () => {
    window.location.hash = "/";
  }
</script>

<style>
  input, select, button {
    font-size: 1rem;
  }
</style>

<div class="w-full max-w-sm mx-auto mt-16">
  <h2 class="text-2xl font-bold mb-4 text-center">Registrar Usuario</h2>

  {#if error}
    <p class="text-red-500 text-sm mb-2">{error}</p>
  {/if}
  {#if success}
    <p class="text-green-500 text-sm mb-2">{success}</p>
  {/if}

  <input
    class="w-full border rounded px-3 py-2 mb-2"
    placeholder="Nombre de usuario"
    bind:value={username}
  />

  <input
    class="w-full border rounded px-3 py-2 mb-2"
    placeholder="Contraseña"
    type="password"
    bind:value={password}
  />

  <input
    class="w-full border rounded px-3 py-2 mb-2"
    placeholder="Clave de administrador"
    type="password"
    bind:value={adminPassword}
  />

  <select
    class="w-full border rounded px-3 py-2 mb-4"
    bind:value={role}
  >
    <option value="administrador">Administrador</option>
    <option value="jefe_bodega">Jefe de Bodega</option>
    <option value="produccion">Producción</option>
    <option value="ventas">Ventas</option>
  </select>

  <button
    class="w-full bg-blue-600 text-white px-3 py-2 rounded hover:bg-blue-700"
    on:click={register}
  >
    Registrar
  </button>

  <button
    class="w-full mt-2 text-blue-600 hover:underline text-sm"
    on:click={goToLogin}
  >
    ¿Ya tienes cuenta? Iniciar sesión
  </button>
</div>
