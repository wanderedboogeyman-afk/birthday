document.addEventListener("DOMContentLoaded", function () {
    lottie.loadAnimation({
        container: document.getElementById('animation'),
        renderer: 'svg',
        loop: true,
        autoplay: true,
        path: 'https://assets10.lottiefiles.com/packages/lf20_9xkqg3pi.json' // You can replace this with any other Lottie animation URL
    });
});