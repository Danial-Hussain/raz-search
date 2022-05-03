<script lang="ts">
  import { onMount } from 'svelte';

  interface Option {
    name: string;
    description: string;
  }

  export let search: boolean;
  export let updateData: (query: string, podcastName?: string) => void;
  export let options: Option[] = [];

  let filteredOptions: Option[];
  $: filteredOptions = [];

  let searchQuery: string;

  onMount(async () => {
    const url = 'https://raz-search-production.up.railway.app/all/';
    const response = await fetch(url);
    const dataString = await response.json();
    options = JSON.parse(dataString);
  });

  const filter = () => {
    filteredOptions = options.filter((option) =>
      option.name.toLowerCase().includes(searchQuery.toLowerCase())
    );
  };
</script>

<div
  class="p-2 fixed inset-0 bg-gray-600 bg-opacity-50 backdrop-blur-sm flex flex-col items-center pt-64"
>
  <div class="w-full flex flex-row justify-center items-center pb-2 gap-x-1">
    <input
      class="absolute w-full md:w-1/2 p-4 rounded-lg z-40 shadow-lg border-2 border-gray-600 bg-gray-300"
      placeholder="Search for a podcast, individual, or business idea..."
      bind:value={searchQuery}
      on:input={() => filter()}
    />
    <div class="w-full md:w-1/2 flex flex-row justify-end gap-x-1 p-2">
      <img
        src="./search.svg"
        alt="search"
        class="cursor-pointer relative z-50 h-10 w-10 p-2 bg-gray-200 rounded-full border-2 border-emerald-500 hover:bg-gray-300"
        on:click={() => updateData(searchQuery)}
      />
      <img
        src="./close.svg"
        alt="search"
        class="cursor-pointer relative z-50 h-10 w-10 p-2 bg-gray-200 rounded-full border-2 border-emerald-500 hover:bg-gray-300"
        on:click={() => (search = false)}
      />
    </div>
  </div>
  <div class="flex flex-col items-center justify-center gap-1 w-full">
    {#each filteredOptions.slice(0, 10) as option}
      <div
        class="cursor-pointer bg-gray-100 text-gray-500 w-full md:w-1/2 delay-50 hover:bg-gray-200 p-2"
        on:click={() => {
          updateData(option.description, option.name);
        }}
      >
        {option.name}
      </div>
    {/each}
  </div>
</div>
