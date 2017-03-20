//info:
//
//##pop2scale## for scaling nodes by popularity(based on followers and friends)
//####
//
//
//
//

var pop2scale = new function(i){
	popularity = i.user.followers_count+i.user.friends_count;
	return Math.sqrt(popularity);
}
