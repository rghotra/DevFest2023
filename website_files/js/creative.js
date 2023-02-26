
const loadingCircle = document.getElementById('loading-circle');
loadingCircle.style.display = 'none';
  
  
  // change the color of the loading circle
// loadingCircle.style.borderTopColor = '#ff0000'; // set to red


// Define the Flask route to handle the image processing

// const URL = "http://localhost:5000/process";

// windows.alert(5);
// Function to process the uploaded image

// function processImage() {

//   // Retrieve the selected image file from the input element

//   const fileInput = document.getElementById("fileInput");

//   const file = fileInput.files[0];

 

//   // Create a FormData object to store the file data

//   const formData = new FormData();

//   formData.append("file", file);

 

//   // Send a POST request to the Flask route with the FormData object

//   fetch(URL, {

//     method: "POST",

//     body: formData

//   })

//   .then(response => response.json())

//   .then(data => {

//     // Handle the response from the Flask route

//     console.log(data);

//   })

//   .catch(error => console.error(error));

// }

 

// Add an event listener to the input element to trigger the image processing

// const fileInput = document.getElementById("fileInput");

// fileInput.addEventListener("change", processImage);



function readURL(input) {
  if (input.files && input.files[0]) {

    const reset = document.getElementById('response');
    
    reset.innerText = ("");

    var reader = new FileReader();

    reader.onload = function(e) {
      $('.image-upload-wrap').hide();

      $('.file-upload-image').attr('src', e.target.result);
      $('.file-upload-content').show();

      $('.image-title').html(input.files[0].name);


     
      console.log(JSON.stringify({
        data: reader.result
      }))
      fetchData()




    

      

function fetchData(){
        loadingCircle.style.display = 'block';
        fetch("https://devfest2023-je62xqayyq-ue.a.run.app/process-file", {
          
          
          method: 'POST',
          mode: "cors",
          body: JSON.stringify({
            data: reader.result,
            // datatype: 'jsonp'
          })
        }).then(data => data.json()).then(json => {
      
            console.log(json)
            

            // const loadingCircle = document.getElementById('loading-circle');


            loadingCircle.style.display = 'none';




      
              const responseElement = document.getElementById('response');
              responseElement.innerText = (json.output);
            })
            .catch(error => {
              loadingCircle.style.display = 'none';

              const responseElement = document.getElementById('response');
              responseElement.innerText = 'Error: ' + error.message;
            });
    }
    
    };











      reader.readAsDataURL(input.files[0]);

      //console.log(reader.result);

      //heroku fetch


      // fetch('heroku.dsd/process-image', {
      //   method: 'POST',
      //   body: reader.result
      // }).then(response => {
      //   console.log()
      // })

      // response = '{"name":"John"}'

      
      //console.log(result)
      // fetch("https://devfest2023-d9dd0.web.app/process-file", {
        
      //   method: 'POST',
      //   body: JSON.stringify({
      //     data: result
      //   })
      // }).then(data => {
    
          
    
      //     let jsObject = JSON.parse(data);
          
    
      //       const responseElement = document.getElementById('response');
      //       responseElement.innerText = (jsObject.result);
      //     })
      //     .catch(error => {
      //       const responseElement = document.getElementById('response');
      //       responseElement.innerText = 'Error: ' + error.message;
      //     });

        }

      

      
      

      // console.log(reader.result);

      // reader.readAsDataURL(input.files[0]);


  
  // else {
  //   removeUpload();
  // }
}




function removeUpload() {
  $('.file-upload-input').replaceWith($('.file-upload-input').clone());
  $('.file-upload-content').hide();
  $('.image-upload-wrap').show();
}
$('.image-upload-wrap').bind('dragover', function () {
    $('.image-upload-wrap').addClass('image-dropping');
  });
  $('.image-upload-wrap').bind('dragleave', function () {
    $('.image-upload-wrap').removeClass('image-dropping');
});



/*!
    * Start Bootstrap - Creative v6.0.4 (https://startbootstrap.com/theme/creative)
    * Copyright 2013-2020 Start Bootstrap
    * Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-creative/blob/master/LICENSE)
    */
    (function($) {
  "use strict"; // Start of use strict

  // Smooth scrolling using jQuery easing
  $('a.js-scroll-trigger[href*="#"]:not([href="#"])').click(function() {
    if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
      if (target.length) {
        $('html, body').animate({
          scrollTop: (target.offset().top - 72)
        }, 1000, "easeInOutExpo");
        return false;
      }
    }
  });

  // Closes responsive menu when a scroll trigger link is clicked
  $('.js-scroll-trigger').click(function() {
    $('.navbar-collapse').collapse('hide');
  });

  // Activate scrollspy to add active class to navbar items on scroll
  $('body').scrollspy({
    target: '#mainNav',
    offset: 75
  });

  // Collapse Navbar
  var navbarCollapse = function() {
    if ($("#mainNav").offset().top > 100) {
      $("#mainNav").addClass("navbar-scrolled");
    } else {
      $("#mainNav").removeClass("navbar-scrolled");
    }
  };
  // Collapse now if page is not at top
  navbarCollapse();
  // Collapse the navbar when page is scrolled
  $(window).scroll(navbarCollapse);

  // Magnific popup calls
  $('#portfolio').magnificPopup({
    delegate: 'a',
    type: 'image',
    tLoading: 'Loading image #%curr%...',
    mainClass: 'mfp-img-mobile',
    gallery: {
      enabled: true,
      navigateByImgClick: true,
      preload: [0, 1]
    },
    image: {
      tError: '<a href="%url%">The image #%curr%</a> could not be loaded.'
    }
  });

})(jQuery); // End of use strict
