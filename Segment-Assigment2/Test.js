function concat() {
    var y = document.getElementById("no1").value;
    var z = document.getElementById("no2").value;
    var x = y + z;

    console.log(x);
    console.log(x);
    console.log(x);
    concat3();

    analytics.identify('007', {

        name: 'James Bond',
      
        email: 'jamesbond@gmail.com'
      
      })

    document.getElementById("p").innerHTML = x;
}

function concat3() {
    var y = document.getElementById("no1").value;
    var z = document.getElementById("no2").value;
    var x = y + z;

    console.log(x);
    console.log(x);
    console.log(x);


    document.getElementById("p").innerHTML = x;

}

function buy() {

    analytics.track('shoes sold', {

        title: 'Stilleto',
      
        subtitle: 'red-German',
      
        designer: 'Cucci'
      
      });

}

