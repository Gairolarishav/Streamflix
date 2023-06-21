$(document).ready(function(){
    $(window).scroll(function(){
        var scroll = $ (window).scrollTop();
        if(scroll>100){
            $(".streamflix-navbar").css("background","#0C0C0C");
        }
        else{
            $(".streamflix-navbar").css("background","transparent");
        }
    })
})