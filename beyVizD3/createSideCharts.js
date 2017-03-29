function createSideCharts(dataW, dataC) {
	w = 300;
    h = 600;
	
	wordList = [];
	
	var barPadding = 1;
	var padding = 2;
	var paddingY = 25;
	var paddingX = 35;
	
	//console.log(data);
	
	dataW.splice(20);
	dataC.splice(20);
	dataW.splice(0,1);
	dataC.splice(0,1);
	
	for(i=0;i<dataW.length;i++)
    {
        wordList.push([dataW[i],dataC[i]]);
    }
	

	
	//console.log(data);
	
	var yScale = d3.scale.linear()
		.domain([dataC[0],0])
        .range([paddingY, (h/2)-(paddingY*4)]);
	var xScale = d3.scale.ordinal()
        .domain(dataW) 
		.rangeRoundBands([paddingX,w-paddingX]);
	//var xScaleTime = d3.scale.linear().domain([0,31]).range([paddingX,w-paddingX]);
					 

		
	var xAxis = d3.svg.axis().scale(xScale).orient("bottom");
	var yAxis = d3.svg.axis().scale(yScale).orient("left").ticks(5);
	//var xAxisTime = d3.svg.axis().scale(xScaleTime).orient("bottom");
	
	var bars = svg.selectAll("rect")
    .data(wordList)
    .enter()
    .append("rect");
	
	bars.attr("height","0")
		.attr("width", ((w-(paddingX*2)) / (wordList.length+1))- barPadding*2)
		.attr("x", function(d, i) {
			//return (i * ((w-(paddingX*2)) / 20))+paddingX;
			return (xScale(d[0])+(barPadding*2));
		}).attr("height", function(d) {
			return (((h/2)-(paddingY*4))-yScale(d[1]));
		}).attr("y", function(d) {
			return (yScale(d[1]));
		}).attr("fill","rgba(35, 80, 143, 1)");
	
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
		
	//svg.append("g").attr("class", "axis").attr("transform", "translate(0," + (h-paddingY) + ")").call(xAxisTime);
	//svg.append("g").attr("class", "axis").attr("transform", "translate(" + paddingX + ","+((h/2)+(paddingY*3))+")").call(yAxis);
}