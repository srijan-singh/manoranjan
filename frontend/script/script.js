//api url
const api_url =
    'https://manoranjan.deta.dev/movie/*';

// Defining async function
async function getapi(url) {
	
	// Storing response
	const response = await fetch(url);
	
	// Storing data in form of JSON
	var data = await response.json();
	if (response) {
		hideloader();
	}
	show(data);
}
// Calling that async function
getapi(api_url);

// Function to hide the loader
function hideloader() {
	document.getElementById('loading').style.display = 'none';
}
// Function to define innerHTML for HTML table
function show(data) {
	let tab = ``;

        console.log(data);
	
	// Loop to access all rows
	for (let r of data) {
		tab += 
        `    
        <a href="${r.server_url}">    
        <div class="container">
        <div class ="content">
        Movie ${r.name}
		<br>
        Tag ${r.tag}
        <br>
        Year ${r.year} 
        </div>  
        </div>
        </a>
        
        `;
	}
	// Setting innerHTML as tab variable
	document.getElementById("body").innerHTML = tab;
    
}
