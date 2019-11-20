P = undef;

module ball() {

    translate([0, 0, 10]) {
       color("red")
       sphere(r=10);
    }
}

module floor() {
  cube([200, 200, 0.1], center=true);
}

if(P==0 || P==1) ball();
if(P==0 || P==2) floor();