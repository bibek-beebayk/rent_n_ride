async function getUsers(){
    // let url= 'https://fakestoreapi.com/products/category/jeweleryss';
    let url= 'js/users.json';


    try{
        let res= await fetch(url);
        // console.log (fetch(url));
        // console.log(res.());
        let a =  await res.json();
        return a;

    }catch (error){
        console.log(error);
    };
}

// rendering json data

async function renderUsers(){
    let users = await getUsers();
    
    let html = '';
   users.forEach(user => {
        // let htmlSegment = `<div class = "user">
        //                     <id> ${user.id-4}</id>
        //                     <name>${user.title}</name>

        //                     </div>`;
        let htmlSegment = `<div class="ad-post col-md-3">
						
        <img src="${user.image}">
        <div class="detail">
        <name>${user.title.slice(0, 10)}</name>
        <br>
        <price>${user.price}</price> per day
        <br>
        <button>Book For Ride</button>
        
        </div>
        </div>`;
         html += htmlSegment;
    });
    let container = document.querySelector('.new-one');
    container.innerHTML = html;

}
renderUsers();