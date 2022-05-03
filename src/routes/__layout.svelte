<script>
  import '../app.css';
  import Navbar from '../components/Navbar.svelte';
  import Footer from '../components/Footer.svelte';

  const title = 'raz-search';
  const description = 'Semantic search over the podcast "How I Built This" by Guy Raz';
</script>

<svelte:head>
  <title>{title}</title>
  <meta name="description" content={description} />
  <meta name="viewport" content="width=device-width, initial-scale=1" />

  <meta property="og:title" content={title} />
  <meta property="og:description" content={description} />
  <meta property="og:image" content="https://raz-search.vercel.app/logo.png" />

  <meta name="twitter:image" content="https://raz-search.vercel.app/logo.png" />
  <meta name="twitter:card" content="summary_large_image" />
</svelte:head>

<Navbar />
<slot />
<Footer />
