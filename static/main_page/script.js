function validate(){

 
    let form = document.getElementsByTagName("form")[0];
    let message = document.getElementsByClassName("message");

    let username = form[0].value;
    let password = form[1].value;
    
    if (username.trim() == ""){
        message[0].innerHTML = " Please Enter Username.";
        

    }else{
        message[0].innerHTML = "";
        return false;
    }

    if (password.trim()== ""){
        message[1].innerHTML = "Please Enter Password.";
        

    }else{
        message[1].innerHTML = "";
        return false;

    }
    return true;
}
