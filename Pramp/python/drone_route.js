/*

   Fuel Delta : 0 +10 +4 -2 -5 +2
   Actual Fuel: 5 15 9 3 0 7

   Strategy:
      * Set delta to 0
      * Set min_delta to 0
      * Iterate through points starting at point 1 to point n
      * Delta -= point[i][z] - point[i-1][z]
      * Update minimum delta as needed

   * Return maximum point
   
   start z = 10, max z = 15, so I need 5 liters of fuel
[{x:0, y:2, z:10}, {x:3, y:5, z:0}, {x:9, y:20, z:6}, {x:10, y:12, z:15}, {x:10, y:10, z:8}]

[{z: 8}, {z:2},{z:4}] ==> no fuel needed

[{z:10},{z:0},{z:20}] ==> 10 fuel required

[{z:1}] ==> 0 fuel required
      [] ==> 0 fuel

*/

function fuel_required(route){
   if(route === undefined || route.length == 0){
      return 0;
   }else{
      var initial_z = route[0].z;
      var max_z = initial_z;
      for(let i = 1; i<route.length; i++){
         if(route[i].z > max_z){
            max_z = route[i].z;
         }
      }
      return max_z - initial_z;
   }
}