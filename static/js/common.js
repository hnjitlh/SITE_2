$(function () {
    console.log("Document Loaded!");

    const controller = new ScrollMagic.Controller();


    //all SlideIns
    const slideIns = $('.slideIn');
    for (let i = 0; i < slideIns.length; i++) {
        new ScrollMagic.Scene({
            triggerElement: slideIns[i],
            triggerHook: 0.9
        })
            .setClassToggle(slideIns[i], 'visible')
            .addIndicators()
            .addTo(controller);
    }

});

$('a[href*="#"]:not([href="#"])').click(function () {
    if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
        var target = $(this.hash);
        target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
        if (target.length) {
            $('html, body').animate({
                scrollTop: target.offset().top
            }, 500);
            return false;
        }
    }
});