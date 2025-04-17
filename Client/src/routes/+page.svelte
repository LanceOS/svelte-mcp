<script>
	let data = null;
	let loading = false;
	let error = null;

	const API_URL = 'http://127.0.0.1:6274/tools/get_distribution_data';

	async function fetchData() {
		const response = await fetch(API_URL, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({ user_input: 'Can I get my current distribution data please' })
		});

		console.log(response);
	}
</script>

<div class="mx-auto max-w-2xl p-5 font-sans">
	<h1 class="mb-6 text-2xl font-bold text-gray-800">API Data Fetcher</h1>

	<button
		on:click={fetchData}
		disabled={loading}
		class="rounded bg-green-600 px-4 py-2 text-white transition-colors
             hover:bg-green-700 disabled:cursor-not-allowed disabled:bg-gray-400"
	>
		{loading ? 'Loading...' : 'Fetch Data'}
	</button>

	{#if error}
		<div class="mt-4 rounded border border-red-300 bg-red-50 p-3 text-red-700">
			Error: {error}
		</div>
	{/if}

	{#if data}
		<div class="mt-6 overflow-x-auto rounded border border-gray-200 bg-gray-50 p-4">
			<h2 class="mb-2 text-lg font-semibold text-gray-700">API Response:</h2>
			<pre
				class="overflow-x-auto whitespace-pre-wrap break-words rounded border border-gray-200
                   bg-white p-3 text-sm">
          {JSON.stringify(data, null, 2)}
        </pre>
		</div>
	{/if}
</div>
