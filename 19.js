
nb=0;
for(var an=1901;an<=2000;an++){
    for(var mois=1;mois<=12;mois++){
    var d= new Date(an,mois,1);
    if (d.getDay()==0){
        nb++;
        
    }
    }
}
console.log(nb)