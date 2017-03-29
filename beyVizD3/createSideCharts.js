function createSideCharts(data) {
	w = 300;
    h = 800;
	wordList = [];
	
	var barPadding = 1;
	var padding = 2;
	var paddingY = 25;
	var paddingX = 25;
	
	//console.log(data);
	
	data[0]["most_common_words"].splice(20);
	
	console.log(data);
	
	for (var i = 0; i < data[0]["most_common_words"].length; i++) {
				wordList.push(data[0]["most_common_words"][i]['key']);
			}
	
	var yScale = d3.scale.linear()
		.domain([data[0]["most_common_words"][0]['value'],0])
        .range([paddingY, (h/2)-(paddingY*4)]);
	var xScale = d3.scale.ordinal()
        .domain(wordList) 
		.rangeRoundBands([paddingX,w-paddingX]);
	var xScaleTime = d3.scale.linear()
        .domain([0,31]) 
		.range([paddingX,w-paddingX]);
					 
	var svg = d3.select("body")
		.append("svg")
		.data(data)
        .attr("width", w)
        .attr("height", h)
	;
		
	var xAxis = d3.svg.axis().scale(xScale).orient("bottom");
	var xAxisTime = d3.svg.axis().scale(xScaleTime).orient("bottom");
	var yAxis = d3.svg.axis().scale(yScale).orient("left").ticks(5);
	
	var bars = svg.selectAll("rect")
    .data(data[0]['most_common_words'])
    .enter()
    .append("rect");
	
	bars.attr("height","0")
		.attr("width", ((w-(paddingX*2)) / 21)- barPadding*2)
		.attr("x", function(d, i) {
			//return (i * ((w-(paddingX*2)) / 20))+paddingX;
			return (xScale(d['key']));
		}).attr("height", function(d) {
			return (((h/2)-(paddingY*4))-yScale(d['value']));
		}).attr("y", function(d) {
			return (yScale(d['value']));
		}).attr("fill", function(d) {
			return "rgba(200, 0, 128, 1)";
		});
	
	//initialize Axis'
	svg.append("g").attr("class", "axis")
		.attr("transform", "translate(0," + ((h/2)-(paddingY*4)) + ")")
		.call(xAxis)
		.selectAll("text")
			.attr("y", 0)
			.attr("x", 9)
			.attr("dy", ".35em")
			.attr("transform", "rotate(90)")
			.style("text-anchor", "start");

	svg.append("g").attr("class", "axis")
		.attr("transform", "translate(" + paddingX + ",0)")
		.call(yAxis);
		
	svg.append("g").attr("class", "axis")
		.attr("transform", "translate(0," + (h-paddingY) + ")")
		.call(xAxisTime);

	svg.append("g").attr("class", "axis")
		.attr("transform", "translate(" + paddingX + ","+((h/2)+(paddingY*3))+")")
		.call(yAxis);
}