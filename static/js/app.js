//Submits form on selection of neighborhood from dropdown menu
document.getElementsByName("location")[0].addEventListener("change", function() {
    document.getElementById("theform").submit();
});


firebase.auth().onAuthStateChanged(function(user) {
    if(user) {
        document.getElementsByClassName("sign-in-button")[0].style.display = "none";
        document.getElementsByClassName("sign-out-button")[0].style.display = "block";
        var user = firebase.auth().currentUser;
        document.getElementsByClassName("account-info")[0].textContent = "You are signed in as " + user.email;
    } else {
        document.getElementsByClassName("sign-out-button")[0].style.display = "none";
        document.getElementsByClassName("sign-in-button")[0].style.display = "block";
    }
});

document.getElementsByClassName("logout")[0].addEventListener("click", function() {
    firebase.auth().signOut();
});

