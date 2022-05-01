<script lang="ts">
  import About from '../components/About.svelte';
  import Search from '../components/Search.svelte';
  import Podcast from '../components/Podcast.svelte';
  let search: boolean;
  $: search = false;
</script>

<div class="max-w-6xl mx-auto flex flex-col gap-8 p-2">
  <About />
  <button
    class="max-w-2xl mx-auto w-full border-2 border-gray-500 p-2 hover:bg-gray-200"
    on:click={() => (search = true)}>Search for a podcast, individual, or idea ...</button
  >
  <div class="max-w-4xl w-full mx-auto flex flex-col gap-6">
    <div class="flex flex-col gap-2">
      <h1 class="text-3xl">Latest Episodes</h1>
      <div class="w-full h-1 bg-gray-500" />
    </div>
  </div>
</div>

{#if search}
  <Search bind:search />
{/if}
