# raz-search

**raz-search** is a semantic search engine for finding related podcast episodes on the podcast show [How I Built This](https://www.npr.org/series/490248027/how-i-built-this) by Guy Raz. The podcast "weaves a narrative journey about innovators, entrepreneurs and idealists—and the movements they built". The episodes are jam-packed with wisdom and I often find myself curious about learning more on the discussed topics. **raz-search** allows you to do just that by enabling search across all episodes to find those related to your topic of interest. More details on how the algorithm works are below.

## Semantic Search

For this project, I'm using the `paraphrase-MiniLM-L6-v2` sentence transformer model to generate a vector embedding of each podcast episode description. This embedding is essentially a transformed version of the sentence represented in a high-dimensional space. With these embeddings, I can compare them to one another using `cosine similarity` to understand how similar they are. Those that have a higher score are more similar which ultimately determines the rankings you see on the web app. More details on sentence transformers can be found [here](https://www.sbert.net/).

## Technology Stack

With respect to the frontend, the web app is built using SvelteKit, and styling is predominantly done using TailwindCSS. Also, hosting is handled seamlessly through Vercel. For the backend, I'm persisting the Spotify podcast data into a Mongo database on Mongo Atlas and using a FastAPI server hosted on Railway for the semantic search transformer model.

## Future Applications

I believe there's significant room for improvement in the "discoverability" space for podcasts. At the moment, finding podcasts on related topics is extremely tedious and the best solution I've found so far is [ListenNotes](https://www.listennotes.com/). **raz-search** aims to be a proof-of-concept for the use of semantic search to help with this process, but it's far from perfect. One challenge with the approach I took is the fact that not all podcasts have standardized descriptions as HIBT. For example, [The Tim Ferris Show](https://tim.blog/podcast/) is an excellent podcast with some great guests, but the podcast descriptions are embedded with advertisements and don't follow a clear structure. Simply taking the podcasts' descriptions as they stand would cause the algorithm to pick up on similarities in the advertisers on the episode rather than the content being discussed.

One area where I think this application would be incredibly useful is in the technology podcast space. I've often found myself wanting to dive deep into a particular topic, but finding all podcasts on "graph neural networks" isn't the easiest thing to do.
