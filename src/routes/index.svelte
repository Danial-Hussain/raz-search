<script context="module">
  export const load = async () => {
    const url = 'http://localhost:8000/latest-episodes/';
    const response = await fetch(url);
    const dataString = await response.json();
    const data = JSON.parse(dataString);
    return {
      props: {
        data: data
      }
    };
  };
</script>

<script lang="ts">
  import About from '../components/About.svelte';
  import Search from '../components/Search.svelte';
  import Podcast from '../components/Podcast.svelte';

  let search: boolean;
  let searchQuery: string;
  let loading: boolean;

  $: search = false;
  $: searchQuery = '';
  $: loading = false;

  export let data: any;

  const updateData = async (query: string, podcastName: string = '') => {
    search = false;
    loading = true;
    searchQuery = podcastName === '' ? query : podcastName;
    const url = `http://localhost:8000/search/?query=${query}`;
    const response = await fetch(url);
    const dataString = await response.json();
    data = JSON.parse(dataString);
    loading = false;
  };
</script>

<div class="max-w-6xl mx-auto flex flex-col gap-8 p-2">
  <About />
  <button
    class="max-w-2xl mx-auto w-full border-2 border-gray-500 p-2 hover:bg-gray-200"
    on:click={() => (search = true)}>Search for a podcast, individual, or idea ...</button
  >
  <div class="max-w-4xl w-full mx-auto flex flex-col gap-6">
    <div class="flex flex-col gap-2">
      {#if searchQuery === ''}
        <h1 class="text-3xl">Latest Episodes</h1>
      {:else}
        <h1 class="text-3xl mr-2">
          Top Results for: <strong class="italic text-gray-500 text-xl font-normal"
            >"{searchQuery}"</strong
          >
        </h1>
      {/if}
      <div class="w-full h-1 bg-gray-500" />
    </div>
    {#if loading === false}
      {#each data as podcast}
        <Podcast
          name={podcast.name}
          description={podcast.description}
          duration={podcast.duration_mins}
          date={podcast.release_date}
          link={podcast.spotify_url}
        />
      {/each}
    {:else}
      <img src="./loading.svg" alt="loading" class="h-12 w-12 mx-auto" />
    {/if}
  </div>
</div>

{#if search}
  <Search bind:search {updateData} />
{/if}
