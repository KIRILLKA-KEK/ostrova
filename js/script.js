// import Swiper from 'https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.mjs'

let swiper = new Swiper('.weather__swiper', {
	// Optional parameters
	direction: 'horizontal',
	// loop: true,

	// If we need pagination
	pagination: {
		el: '.swiper-pagination',
	},
});