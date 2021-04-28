var days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];

// var body = document.querySelector('body');
// var body = document.body

var ul = document.createElement('ul');  // ul = <ul> </ul>
var li = "";

for( var index = 0; index < days.length; index++){
    li = li + `<li>${days[index]}</li>`;
}

/* 
    li =>   <li>Monday</li>
            <li>Tuesday</li>
            <li>Wednesday</li>
            <li>Thursday</li>
            <li>Friday</li>
            <li>Saturday</li>
            <li>Sunday</li> 
*/

ul.innerHTML = li;
/* ul = <ul>
            <li>Monday</li>
            <li>Tuesday</li>
            <li>Wednesday</li>
            <li>Thursday</li>
            <li>Friday</li>
            <li>Saturday</li>
            <li>Sunday</li>  
        </ul>
*/

document.body.append(ul);