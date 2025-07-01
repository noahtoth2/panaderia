<script>
  import Router from 'svelte-spa-router';
  import Login from './pages/Login.svelte';
  import Dashboard from './pages/Dashboard.svelte';
  import Register from './pages/Register.svelte'; // 👈 importa Register

  const routes = {
    "/": Login,
    "/dashboard": Dashboard,
    "/register": Register, // 👈 nueva ruta
  };
</script>

<main class="p-4">
  <Router {routes} />
</main>
