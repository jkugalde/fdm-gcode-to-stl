linewidth = 0.4; //extruder diameter
layerheight = 0.3;

//cap_round true adds a faceted disc in the ends of the lines

nfacets = 3; //facets of the disc

module line(point1, point2,lh=0.3,width = 1,cap_round=false) {
    angle = 90 - atan((point2[1] - point1[1]) / (point2[0] - point1[0]));
    offset_x = 0.5 * width * cos(angle);
    offset_y = 0.5 * width * sin(angle);

    offset1 = [-offset_x, offset_y];
    offset2 = [offset_x, -offset_y];
    if(cap_round) {
    translate(point1) 
            translate([0,0,lh])
            linear_extrude(layerheight){
        circle(d = width, $fn = nfacets);}
        
            translate(point2) 
            translate([0,0,lh])
                   linear_extrude(0.3){
    circle(d = width, $fn = nfacets);
                   }
               }
               
    translate([0,0,lh])
    linear_extrude(layerheight){

    polygon(points=[
        point1 + offset1, point2 + offset1,  
        point2 + offset2, point1 + offset2
    ]);
    }
}

//PASTE THE TXT HERE
