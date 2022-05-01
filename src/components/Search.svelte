<script lang="ts">
  export let search: boolean;
</script>

<div
  class="fixed inset-0 bg-gray-600 bg-opacity-50 backdrop-blur-sm flex flex-col justify-center items-center"
  on:click={() => (search = false)}
>
  <input
    class="w-full md:w-1/2 p-4 rounded-lg z-50 shadow-lg border-2 border-gray-600 bg-gray-300"
    placeholder="Search for a podcast, individual, or business idea..."
  />
</div>
