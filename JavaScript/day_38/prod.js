let cat=prompt("enter the category: ")


const url = `https://real-time-amazon-data.p.rapidapi.com/search?query=${cat}&page=1&country=IN&sort_by=RELEVANCE&product_condition=ALL&is_prime=false&deals_and_discounts=NONE`;
const options = {
	method: 'GET',
	headers: {
		'x-rapidapi-key': '0a099e886dmshbd575eed4f72363p133f32jsn6bbc95d5e265',
		'x-rapidapi-host': 'real-time-amazon-data.p.rapidapi.com'
	}
};

fetch(url,options).then(res=>res.json()).then(d=>console.log(d.data.products)).catch(err=>console.log(err))