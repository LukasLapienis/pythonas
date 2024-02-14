cities = {
	"New York City":{
		"country": "United States",
		"population": 20.14,
		"area": 1223.59
	},
	"Tokyo":{
		"country": "Japan",
		"population": 37.47,
		"area": 2194.07,
	},
		"Los Angeles":{
 
		"country": "United States",
		"population": 13.2,
		"area": 1299.01,
	},
	"Madrid":{
		"country": "Spain",
		"population": 6.79,
		"area": 604.31,
	},
	 "Osaka":{
 
		"country": "Japan",
		"population": 19.3,
		"area": 5107.0,
	},
	"London":{
 
		"country": "United Kingdom",
		"population": 14.26,
		"area": 8382.0,
	}
}

miestai = dict(sorted(cities.items(), key=lambda city:city[1]['population'], reverse=True))

print(miestai)