<script lang="ts">
  export let name: string;
  export let description: string;
  export let duration: string;
  export let date: string;
  export let link: string;
</script>

<div class="border-2 border-gray-400 flex flex-col gap-y-2 p-4">
  <a href={link} class="text-md underline hover:decoration-gray-500 hover:text-gray-500"
    >Episode: {name}</a
  >
  <div class="flex flex-row gap-2">
    <div class="bg-gray-200 text-gray-400 text-sm rounded-lg px-2 py-1">{date}</div>
    <div class="bg-gray-200 text-gray-400 text-sm rounded-lg px-2 py-1">{duration}mins</div>
  </div>
  <p class="text-gray-600 text-sm">
    {description}
  </p>
</div>
