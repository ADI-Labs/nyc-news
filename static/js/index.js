//Submits form on selection of neighborhood from dropdown menu
document.getElementsByName("location")[0].addEventListener("change", function() {
    document.getElementsByClassName("theform")[0].submit();
});

