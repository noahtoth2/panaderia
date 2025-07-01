<script>
  import { onMount } from "svelte";
  import { goto } from 'svelte-spa-router';

  let username = "";
  let password = "";
  let adminPassword = "";
  let role = "ventas"; // valor por defecto

  let error = "";
  let success = "";

  const register = async () => {
    error = "";
    success = "";

    if (!adminPassword || adminPassword !== "superclave123") {
      error = "Contraseña de administrador inválida.";
      return;
    }

    const response = await fetch("http://localhost:8000/auth/register", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ username, password, role })
    });

    if (response.ok) {
      success = "Usuario registrado correctamente.";
      setTimeout(() => goto("/"), 2000);
    } else {
      const data = await response.json();
      error = data.detail || "Error en el registro.";
    }
  };
</script>

<h1 class="text-2xl font-bold mb-4">Registrar Usuario</h1>

{#if error}
  <p class="text-red-500 mb-2">{error}</p>
{/if}
{#if success}
  <p class="text-green-500 mb-2">{success}</p>
{/if}

<div class="flex flex-col space-y-2">
  <input class="border p-2" placeholder="Nombre de usuario" bind:value={username} />
  <input class="border p-2" placeholder="Contraseña" type="password" bind:value={password} />
  <input class="border p-2" placeholder="Contraseña de administrador" type="password" bind:value={adminPassword} />

  <select class="border p-2" bind:value={role}>
    <option value="administrador">Administrador</option>
    <option value="bodega">Jefe de Bodega</option>
    <option value="produccion">Producción</option>
    <option value="ventas">Ventas</option>
  </select>

  <button class="bg-blue-500 text-white p-2 rounded" on:click={register}>Registrar</button>
</div>
