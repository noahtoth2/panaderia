<script>
  import { onMount } from 'svelte';
  import { tsParticles } from 'tsparticles';

  onMount(async () => {
    await tsParticles.load("tsparticles", {
      fullScreen: { enable: true },
      background: { color: "#0f172a" },
      particles: {
        number: { value: 50 },
        color: { value: ["#f97316", "#3b82f6", "#ffffff"] },
        shape: { type: "circle" },
        opacity: { value: 0.8 },
        size: { value: 3 },
        move: { enable: true, speed: 1 }
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
    });
  });
</script>

<div id="tsparticles" class="absolute inset-0 z-0"></div>
