//For handling the next and previous buttons.
//jQuery time
var current_fs, next_fs, previous_fs; //fieldsets
var left, opacity, scale; //fieldset properties which we will animate
var animating; //flag to prevent quick multi-click glitches
var isfaculty ;

$(".next").click(function(e){

    if(animating) return false;
    animating = true;
    
    current_fs = $(this).parent();
    next_fs = $(this).parent().next();
    
    //activate next step on progressbar using the index of next_fs
    $("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");
    
    //show the next fieldset
    next_fs.show(); 
    //hide the current fieldset with style
    current_fs.animate({opacity: 0}, {
      step: function(now, mx) {
        //as the opacity of current_fs reduces to 0 - stored in "now"
        //1. scale current_fs down to 80%
        scale = 1 - (1 - now) * 0.2;
        //2. bring next_fs from the right(50%)
        left = (now * 50)+"%";
        //3. increase opacity of next_fs to 1 as it moves in
        opacity = 1 - now;
        current_fs.css({
          'transform': 'scale('+scale+')',
          'position': 'absolute'
        });
        next_fs.css({'left': left, 'opacity': opacity});
      }, 
      duration: 800, 
      complete: function(){
        current_fs.hide();
        animating = false;
      }, 
      //this comes from the custom easing plugin
      easing: 'easeInOutBack'
    });
  });

$(".next1").click(function(e){
  console.log("pls");
  console.log(validate1());
  if(validate1()!=true){
    console.log("dfg");
    return false;
  }
  else{
    console.log("aaaaa");
    if(animating) return false;
    animating = true;
    
    current_fs = $(this).parent();
    next_fs = $(this).parent().next();
    
    //activate next step on progressbar using the index of next_fs
    $("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");
    
    //show the next fieldset
    next_fs.show(); 
    //hide the current fieldset with style
    current_fs.animate({opacity: 0}, {
      step: function(now, mx) {
        //as the opacity of current_fs reduces to 0 - stored in "now"
        //1. scale current_fs down to 80%
        scale = 1 - (1 - now) * 0.2;
        //2. bring next_fs from the right(50%)
        left = (now * 50)+"%";
        //3. increase opacity of next_fs to 1 as it moves in
        opacity = 1 - now;
        current_fs.css({
          'transform': 'scale('+scale+')',
          'position': 'absolute'
        });
        next_fs.css({'left': left, 'opacity': opacity});
      }, 
      duration: 800, 
      complete: function(){
        current_fs.hide();
        animating = false;
      }, 
      //this comes from the custom easing plugin
      easing: 'easeInOutBack'
    });
  }
  });


$(".next2").click(function(e){
  console.log("pls");
  console.log(validate2());
  if(validate2()!=true){
    console.log("dfg");
    return false;
  }
  else{
    console.log("aaaaa");
    if(animating) return false;
    animating = true;
    
    current_fs = $(this).parent();
    next_fs = $(this).parent().next();
    
    //activate next step on progressbar using the index of next_fs
    $("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");
    
    //show the next fieldset
    next_fs.show(); 
    //hide the current fieldset with style
    current_fs.animate({opacity: 0}, {
      step: function(now, mx) {
        //as the opacity of current_fs reduces to 0 - stored in "now"
        //1. scale current_fs down to 80%
        scale = 1 - (1 - now) * 0.2;
        //2. bring next_fs from the right(50%)
        left = (now * 50)+"%";
        //3. increase opacity of next_fs to 1 as it moves in
        opacity = 1 - now;
        current_fs.css({
          'transform': 'scale('+scale+')',
          'position': 'absolute'
        });
        next_fs.css({'left': left, 'opacity': opacity});
      }, 
      duration: 800, 
      complete: function(){
        current_fs.hide();
        animating = false;
      }, 
      //this comes from the custom easing plugin
      easing: 'easeInOutBack'
    });
  }
  });

$(".next3").click(function(){
  console.log("pls");
  console.log(validate3());
  if(validate3()!=true){
    console.log("dfg");
    return false;
  }
  else{
    console.log(animating);
    if(animating && isfaculty!=0) return false;
    animating = true;
    console.log("qwerty");
    current_fs = $(this).parent();
    if(isfaculty!=0)
      next_fs = $(this).parent().next();
    else
      next_fs = $(this).parent().next().next().next().next();
    console.log(isfaculty+" asdf");
    
    //activate next step on progressbar using the index of next_fs
    $("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");
    
    //show the next fieldset
    next_fs.show(); 
    //hide the current fieldset with style
    current_fs.animate({opacity: 0}, {
      step: function(now, mx) {
        //as the opacity of current_fs reduces to 0 - stored in "now"
        //1. scale current_fs down to 80%
        scale = 1 - (1 - now) * 0.2;
        //2. bring next_fs from the right(50%)
        left = (now * 50)+"%";
        //3. increase opacity of next_fs to 1 as it moves in
        opacity = 1 - now;
        current_fs.css({
          'transform': 'scale('+scale+')',
          'position': 'absolute'
        });
        next_fs.css({'left': left, 'opacity': opacity});
      }, 
      duration: 800, 
      complete: function(){
        current_fs.hide();
        animating = false;
      }, 
      //this comes from the custom easing plugin
      easing: 'easeInOutBack'
    });
  }
});

$(".next4").click(function(e){
  console.log("pls");
  console.log(validate4());
  if(validate4()!=true){
    console.log("dfg");
    return false;
  }
  else{
    console.log("aaaaa");
    if(animating) return false;
    animating = true;
    
    current_fs = $(this).parent();
    next_fs = $(this).parent().next();
    
    //activate next step on progressbar using the index of next_fs
    $("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");
    
    //show the next fieldset
    next_fs.show(); 
    //hide the current fieldset with style
    current_fs.animate({opacity: 0}, {
      step: function(now, mx) {
        //as the opacity of current_fs reduces to 0 - stored in "now"
        //1. scale current_fs down to 80%
        scale = 1 - (1 - now) * 0.2;
        //2. bring next_fs from the right(50%)
        left = (now * 50)+"%";
        //3. increase opacity of next_fs to 1 as it moves in
        opacity = 1 - now;
        current_fs.css({
          'transform': 'scale('+scale+')',
          'position': 'absolute'
        });
        next_fs.css({'left': left, 'opacity': opacity});
      }, 
      duration: 800, 
      complete: function(){
        current_fs.hide();
        animating = false;
      }, 
      //this comes from the custom easing plugin
      easing: 'easeInOutBack'
    });
  }
  });

$(".next4editProfile").click(function(e){
  console.log("pls");
  console.log(validate4editProfile());
  if(validate4editProfile()!=true){
    console.log("dfg");
    return false;
  }
  else{
    console.log("aaaaa");
    if(animating) return false;
    animating = true;
    
    current_fs = $(this).parent();
    next_fs = $(this).parent().next();
    
    //activate next step on progressbar using the index of next_fs
    $("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");
    
    //show the next fieldset
    next_fs.show(); 
    //hide the current fieldset with style
    current_fs.animate({opacity: 0}, {
      step: function(now, mx) {
        //as the opacity of current_fs reduces to 0 - stored in "now"
        //1. scale current_fs down to 80%
        scale = 1 - (1 - now) * 0.2;
        //2. bring next_fs from the right(50%)
        left = (now * 50)+"%";
        //3. increase opacity of next_fs to 1 as it moves in
        opacity = 1 - now;
        current_fs.css({
          'transform': 'scale('+scale+')',
          'position': 'absolute'
        });
        next_fs.css({'left': left, 'opacity': opacity});
      }, 
      duration: 800, 
      complete: function(){
        current_fs.hide();
        animating = false;
      }, 
      //this comes from the custom easing plugin
      easing: 'easeInOutBack'
    });
  }
  });

$(".next5").click(function(e){
  console.log("pls");
  console.log(validate5());
  if(validate5()!=true){
    console.log("dfg");
    return false;
  }
  else{
    console.log("aaaaa");
    if(animating) return false;
    animating = true;
    
    current_fs = $(this).parent();
    next_fs = $(this).parent().next();
    
    //activate next step on progressbar using the index of next_fs
    $("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");
    
    //show the next fieldset
    next_fs.show(); 
    //hide the current fieldset with style
    current_fs.animate({opacity: 0}, {
      step: function(now, mx) {
        //as the opacity of current_fs reduces to 0 - stored in "now"
        //1. scale current_fs down to 80%
        scale = 1 - (1 - now) * 0.2;
        //2. bring next_fs from the right(50%)
        left = (now * 50)+"%";
        //3. increase opacity of next_fs to 1 as it moves in
        opacity = 1 - now;
        current_fs.css({
          'transform': 'scale('+scale+')',
          'position': 'absolute'
        });
        next_fs.css({'left': left, 'opacity': opacity});
      }, 
      duration: 800, 
      complete: function(){
        current_fs.hide();
        animating = false;
      }, 
      //this comes from the custom easing plugin
      easing: 'easeInOutBack'
    });
  }
  });

$(".next6").click(function(e){
  console.log("pls");
  console.log(validate6());
  if(validate6()!=true){
    console.log("dfg");
    return false;
  }
  else{
    console.log("aaaaa");
    if(animating) return false;
    animating = true;
    
    current_fs = $(this).parent();
    next_fs = $(this).parent().next();
    
    //activate next step on progressbar using the index of next_fs
    $("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");
    
    //show the next fieldset
    next_fs.show(); 
    //hide the current fieldset with style
    current_fs.animate({opacity: 0}, {
      step: function(now, mx) {
        //as the opacity of current_fs reduces to 0 - stored in "now"
        //1. scale current_fs down to 80%
        scale = 1 - (1 - now) * 0.2;
        //2. bring next_fs from the right(50%)
        left = (now * 50)+"%";
        //3. increase opacity of next_fs to 1 as it moves in
        opacity = 1 - now;
        current_fs.css({
          'transform': 'scale('+scale+')',
          'position': 'absolute'
        });
        next_fs.css({'left': left, 'opacity': opacity});
      }, 
      duration: 800, 
      complete: function(){
        current_fs.hide();
        animating = false;
      }, 
      //this comes from the custom easing plugin
      easing: 'easeInOutBack'
    });
  }
  });

$(".previous3").click(function(){
  if(animating && isfaculty!=0) return false;
  animating = true;
  
  current_fs = $(this).parent();
  if(isfaculty!=0)
    previous_fs = $(this).parent().prev();
  else
    previous_fs = $(this).parent().prev().prev().prev().prev();

  //de-activate current step on progressbar
  $("#progressbar li").eq($("fieldset").index(current_fs)).removeClass("active");
  
  //show the previous fieldset
  previous_fs.show(); 
  //hide the current fieldset with style
  current_fs.animate({opacity: 0}, {
    step: function(now, mx) {
      //as the opacity of current_fs reduces to 0 - stored in "now"
      //1. scale previous_fs from 80% to 100%
      scale = 0.8 + (1 - now) * 0.2;
      //2. take current_fs to the right(50%) - from 0%
      left = ((1-now) * 50)+"%";
      //3. increase opacity of previous_fs to 1 as it moves in
      opacity = 1 - now;
      current_fs.css({'left': left});
      previous_fs.css({'transform': 'scale('+scale+')', 'opacity': opacity});
    }, 
    duration: 800, 
    complete: function(){
      current_fs.hide();
      animating = false;
    }, 
    //this comes from the custom easing plugin
    easing: 'easeInOutBack'
  });
});

$(".previous").click(function(){
  if(animating && isfaculty!=0) return false;
  animating = true;
  
  current_fs = $(this).parent();
  
  previous_fs = $(this).parent().prev();
  
  //de-activate current step on progressbar
  $("#progressbar li").eq($("fieldset").index(current_fs)).removeClass("active");
  
  //show the previous fieldset
  previous_fs.show(); 
  //hide the current fieldset with style
  current_fs.animate({opacity: 0}, {
    step: function(now, mx) {
      //as the opacity of current_fs reduces to 0 - stored in "now"
      //1. scale previous_fs from 80% to 100%
      scale = 0.8 + (1 - now) * 0.2;
      //2. take current_fs to the right(50%) - from 0%
      left = ((1-now) * 50)+"%";
      //3. increase opacity of previous_fs to 1 as it moves in
      opacity = 1 - now;
      current_fs.css({'left': left});
      previous_fs.css({'transform': 'scale('+scale+')', 'opacity': opacity});
    }, 
    duration: 800, 
    complete: function(){
      current_fs.hide();
      animating = false;
    }, 
    //this comes from the custom easing plugin
    easing: 'easeInOutBack'
  });
});

$(".submit").click(function(){
  return false;
})

function showTabs(ifaculty){
  console.log("hi"+(ifaculty));
  if(ifaculty=="0"){
        document.getElementById('tab4').style.display = "none";
        document.getElementById('tab5').style.display = "none";
        document.getElementById('tab6').style.display = "none";
        document.getElementById('InstituteDetails').style.display = "none";
        document.getElementById('InstituteHeadDetails').style.display = "none";
        document.getElementById('OtherDetails').style.display = "none";
    }
    else{
        document.getElementById('tab4').style.display = "block";
        document.getElementById('tab5').style.display = "block";
        document.getElementById('tab6').style.display = "block";
        document.getElementById('InstituteDetails').style.display = "block";
        document.getElementById('InstituteHeadDetails').style.display = "block";
        document.getElementById('OtherDetails').style.display = "block";
    }
}

//Created / Generates the captcha function    
function DrawCaptcha(){
 /* document.getElementById("next1").disabled = true;
  document.getElementById("next2").disabled = true;
  document.getElementById("next3").disabled = true;
  document.getElementById("next4").disabled = true;
  document.getElementById("next5").disabled = true;
  document.getElementById("next6").disabled = true;*/

  var a = Math.ceil(Math.random() * 9)+ '';
  var b = Math.ceil(Math.random() * 9)+ '';       
  var c = Math.ceil(Math.random() * 9)+ '';  
  var d = Math.ceil(Math.random() * 9)+ '';   
  var code = a + ' ' + b + ' ' + ' ' + c + ' ' + d;
  document.getElementById("txtCaptcha").value = code
}

// Validate the Entered input aganist the generated security code function   
function ValidCaptcha(){
    var str1 = removeSpaces(document.getElementById('txtCaptcha').value);
    var str2 = removeSpaces(document.getElementById('txtInput').value);
    if (str1 == str2) return true;
    DrawCaptcha();        
    return false;
    
}

// Remove the spaces from the entered and generated code
function removeSpaces(string){
  return string.split(' ').join('');
}
    

function showDiv(elem){
  console.log(elem.value+" is faculty");
  if(elem.value == 1){
      document.getElementById('InstituteDetails').style.display = "block";
      document.getElementById('InstituteHeadDetails').style.display = "block";
      document.getElementById('OtherDetails').style.display = "block";
      document.getElementById('secondlabel').style.display = "block";
      document.getElementById('tab4').style.display="block";
        document.getElementById('tab5').style.display="block";
        document.getElementById('tab6').style.display="block";
       $("#progressbar li").css('width','14.28%');
  }
  else{
      document.getElementById('InstituteDetails').style.display = "none";
      document.getElementById('InstituteHeadDetails').style.display = "none";
      document.getElementById('OtherDetails').style.display = "none";
      document.getElementById('secondlabel').style.display = "none";
      document.getElementById('tab4').style.display="none";
        document.getElementById('tab5').style.display="none";
        document.getElementById('tab6').style.display="none";
        $("#progressbar li").css('width','25%');

  }
}

/*//Check if password and ConfirmPassword match.
function checkPass(){
    //Store the password field objects into variables ...
    var pass1 = document.getElementById('password');
    var pass2 = document.getElementById('passwordAgain');
    //Store the Confimation Message Object ...
    var message = document.getElementById('confirmMessage');
    //Set the colors we will be using ...
    var goodColor = "#66cc66";
    var badColor = "#ff6666";
    //Compare the values in the password field 
    //and the confirmation field
    if(pass1.value == pass2.value){
        //The passwords match. 
        //Set the color to the good color and inform
        //the user that they have entered the correct password 
        //pass2.style.backgroundColor = goodColor;
        message.style.color = goodColor;
        message.innerHTML = "Passwords Match!"
    }else{
        //The passwords do not match.
        //Set the color to the bad color and
        //notify the user.
        //pass2.style.backgroundColor = badColor;
        message.style.color = badColor;
        message.innerHTML = "Passwords Do Not Match!"
    }
}*/

function changecity(a){
    if(a==0)
        var s = '#personState'
    else if(a==1)
        var s = '#instituteState'
    $.ajax({
           type: "GET",
           url:"/registration/changecity",                                              // url should define in url.py
           data:{stateid: $(s).val()},          // data : passing parmater $('#elementid').val to get value
           contentType: "application/json; charset=utf-8",                    
           datatype: 'json',
           success: function(result)                                           // if success then return result
                 {
                    //console.log(result);
                    var list =  result;
                    var listItems = "<option value='' disabled selected>--Select the City--</option>";
                    for(var c=0; c<list.length; c++)
                       listItems += "<option value='" + list[c][0]+ "'>" + list[c][1]+ "</option>";
                    if(a==0)
                        $("#personCity").html(listItems);
                    else if(a==1){
                        $("#instituteCity").html(listItems);
                        $("#instituteName").html("<option value='' disabled selected>--Select the Institute--</option>");
                        $("#instituteAddress").html('');
                        $("#institutePincode").val('');
                        document.getElementById('labelinstituteAddress').style.display = "inline";
                        document.getElementById('labelinstitutePincode').style.display = "inline";
                    }
                   }

            });
}

function changeinstitute(){
    $.ajax({
           type: "GET",
           url:"/registration/changeinstitute",                                              // url should define in url.py
           data:{cityid: $("#instituteCity").val()},          // data : passing parmater $('#elementid').val to get value
           contentType: "application/json; charset=utf-8",                    
           datatype: 'json',
           success: function(result)                                           // if success then return result
                 {
                    //console.log(result);
                    var list =  result;
                    var listItems = "<option value='' disabled selected>--Select the Institute--</option>";
                    for(var c=0; c<list.length; c++)
                       listItems += "<option value='" + list[c][0]+ "'>" + list[c][1]+ "</option>";
                    listItems += "<option value='other'>Other</option>"
                    $("#instituteName").html(listItems);
                    $("#instituteAddress").html('');
                    $("#institutePincode").val('');
                    document.getElementById('labelinstituteAddress').style.display = "inline";
                    document.getElementById('labelinstitutePincode').style.display = "inline";
                   }

            });
}

function institutedetails(value){
    if(value == 'other') {
        document.getElementById('newinstitutename').style.display = "inline";
        document.getElementById('labelnewinstitutename').style.display = "inline";
        $("#instituteAddress").html('');
        $("#institutePincode").val('');
        document.getElementById('labelinstituteAddress').style.display = "inline";
        document.getElementById('labelinstitutePincode').style.display = "inline";
        return;
    }

    document.getElementById('newinstitutename').style.display = "none";
    document.getElementById('labelnewinstitutename').style.display = "none";

    $.ajax({
     type: "GET",
     url:"/registration/institutedetails",                                              // url should define in url.py
     data:{instituteid: value},          // data : passing parmater $('#elementid').val to get value
     contentType: "application/json; charset=utf-8",                    
     datatype: 'json',
     success: function(result)                                           // if success then return result
           {
              var list = result;
              $("#instituteAddress").val(list[0]);
              $("#institutePincode").val(list[1]);
              $("#instituteHeadTitle").val(list[2]);
              $("#instituteHeadName").val(list[3]);
              $("#instituteHeadDesignation").val(list[4]);
              $("#instituteHeadEmail").val(list[5]);
              $("#instituteHeadmobileNumber").val(list[6]);
              $("#instituteHeadAddress").val(list[7]);
              $('#checkbox1').checked = true;
              console.log(list);
              //document.getElementById('labelinstituteAddress').style.display = "none";
              //document.getElementById('labelinstitutePincode').style.display = "none";
             }

      });
}

function checkemail(){ 
 
  $.ajax({
   type: "GET",
   url:"/registration/checkemail",                                              // url should define in url.py
   data:{email: $('#email').val()},          // data : passing parmater $('#elementid').val to get value
   contentType: "application/json; charset=utf-8",                    
   datatype: 'json',
   success: function(result)                                           // if success then return result
         {
            if(result){
                document.getElementById('checkemail').style.display = "block";
            }
            else
            {
                document.getElementById('checkemail').style.display = "none";
            }
          }
    });
}

function changeHeadAddress(){
  var $text1 = $('#instituteAddress');
      $text2 = $('#instituteHeadAddress');
  $('#checkbox1').change(function(){
    var c = this.checked;
    if(c){
      $text2.val($text1.val());
      //document.getElementById('instituteHeadAddress').val() = document.getElementById('instituteAddress');
      $('#checkbox1').checked = true;
    }
});

}

//This is for the upload file button.
var fileInputTextDiv = document.getElementById('file_input_text_div');
var fileInput = document.getElementById('file_input_file');
var fileInputText = document.getElementById('file_input_text');
fileInput.addEventListener('change', changeInputText);
fileInput.addEventListener('change', changeState);

function changeInputText() {
  var str = fileInput.value;
  var i;
  if (str.lastIndexOf('\\')) {
    i = str.lastIndexOf('\\') + 1;
  } else if (str.lastIndexOf('/')) {
    i = str.lastIndexOf('/') + 1;
  }
  fileInputText.value = str.slice(i, str.length);
}

function changeState() {
  if (fileInputText.value.length != 0) {
    if (!fileInputTextDiv.classList.contains("is-focused")) {
      fileInputTextDiv.classList.add('is-focused');
    }
  } else {
    if (fileInputTextDiv.classList.contains("is-focused")) {
      fileInputTextDiv.classList.remove('is-focused');
    }
  }
}


function borderRedError(id) {
  document.getElementById(id).style.border = '1px solid red';
}

function AddressVerify(id,val){
  console.log(id);
  console.log(document.getElementById(id).value);
  remark = document.getElementById(id).value;
  if(!remarkValidator(remark) || remark==""){
    borderRedError(id);
    document.getElementById(id+'Error').style.display="block";
    val++;
  }
  else{
    document.getElementById(id).style.border = '';
    document.getElementById(id+'Error').style.display="none";
  }
  return val;
}

function checkPhoto(id,val){
  photo = document.getElementById(id);
  photoname = document.getElementById('file_input_text')
  file = photo.files[0]; console.log(file);
  if(validateLetter(photoname) && checkFileSize(file.size,262144) ){
    console.log("It ok!!");
    document.getElementById('photoError').style.display = "none";
  }
  else{
    console.log("Try another");
    document.getElementById('photoError').style.display = "block";
    val++;
  }
  console.log(val);
  return val;


}

function validateLetter(letter)
{
    var result = false;
    var filext = (getExt(letter)).toLowerCase();
    result = ((letter != null) && (letter != "") && (filext == "jpeg" || filext == "jpg"));
    return result;
}

function getExt(filename) {
    var dot_pos = filename.lastIndexOf(".");
    if (dot_pos == -1)
        return "";
    return filename.substr(dot_pos + 1).toLowerCase();
}

function checkExcel(id,val){
  excel = document.getElementById(id);
  excelname = document.getElementById('file_input_text');
  file = excel.files[0]; //console.log(file);
  if(file.name.includes("xls")&& checkFileSize(file.size,262144) ){
    //console.log("It ok!!");
    document.getElementById('excelError').style.display = "none";
  }
  else{
    //console.log("Try another");
    document.getElementById('excelError').style.display = "block";
    val++;
  }
  console.log(val);
  return val;
}


function checkFileSize(size, requiredSize) {
    var result = false;
    if (size != 0 && size <= requiredSize) {
        result = true;
    }
    return result;
}

function validate1(){
  var value = 0 ;
  var email = document.getElementById("email").value.trim();
  var password = document.getElementById("password").value.trim();
  var cpassword = document.getElementById("passwordAgain").value.trim();

  if (!emailValidator('email')) {
        borderRedError("email");
        document.getElementById("emailError").style.display = "inline";
        value++;
    }
    else{
      document.getElementById("emailError").style.display = "none";
      document.getElementById("email").style.border = '';
    }

    if (!passCheck('password')) {
        borderRedError("password");
        document.getElementById("passwordError").style.display = "inline";
        value++;
    }
    else{
      document.getElementById("password").style.border = '';
      document.getElementById("passwordError").style.display = "none";
    }
    if ((cpassword) == "" || !((password) == (cpassword))) {
        borderRedError("passwordAgain");
        document.getElementById("cpasswordError").style.display = "inline";
        value++;
    }
    else{
      document.getElementById("passwordAgain").style.border = '';
      document.getElementById("cpasswordError").style.display = "none";
    }

    /*if (!((password) == (cpassword))) {
        borderRedError("passwordAgain");
        document.getElementById("cpasswordError").style.display = "inline";
        value++;
    }
    else{
      document.getElementById("passwordAgain").style.border = '';
      document.getElementById("cpasswordError").style.display = "none";
    }*/

    if (value > 0) {
        //scrollWin();
        return false;
    }
    return true;
}

function emailValidator(id) {
    var result = false;
    var email = document.getElementById(id).value.trim();
    console.log(email);
    var emailExp = /^[\w\-\.\+]+\@[a-zA-Z0-9\.\-]+\.[a-zA-z0-9]{2,4}$/;
    if (email.match(emailExp) && email!="") {
      document.getElementById(id+"Error").style.display = "none";
      document.getElementById(id).style.border = '';
        result = true;
    }
    else{
      borderRedError(id);
      document.getElementById(id+"Error").style.display = "inline";
    }
    return result;
}

function passCheck(id){
    var password = document.getElementById(id).value.trim();
    var result = false;
    var passExp = /^(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$/;
    if (password.match(passExp) && password!="") {
        result = true;
        document.getElementById("password").style.border = '';
        document.getElementById("passwordError").style.display = "none";
    }
    else{
      borderRedError("password");
      document.getElementById("passwordError").style.display = "inline";
    }
    return result;   
}

function passConf(){
  var password = document.getElementById("password").value.trim();
  var cpassword = document.getElementById("passwordAgain").value.trim();
  if ((cpassword) == "") {
        borderRedError("passwordAgain");
        document.getElementById("cpasswordError").style.display = "inline";
    }
    else{
      document.getElementById("passwordAgain").style.border = '';
      document.getElementById("cpasswordError").style.display = "none";
    }

    if (!((password) == (cpassword))) {
        borderRedError("passwordAgain");
        document.getElementById("cpasswordError").style.display = "inline";
    }
    else{
      document.getElementById("passwordAgain").style.border = '';
      document.getElementById("cpasswordError").style.display = "none";
    }
}

function nameCheck(id){
  var result = false;
  var name = alltrim(document.getElementById(id).value);
    var nameExp = /^[a-zA-Z][a-zA-Z\. ]+$/;
    if (name.match(nameExp) && name!="") {
      result = true;
      document.getElementById(id+"Error").style.display = "none";
      document.getElementById(id).style.border = '';
    }
    else{
      borderRedError(id);
        document.getElementById(id+"Error").style.display = "inline";
    }
    console.log(result);
    return result;  
}

function validate2(){
  var value = 0;

    value += verifySelect("title",value);
    
    if (!nameCheck('name')) {
        borderRedError("name");
        document.getElementById("nameError").style.display = "inline";
        value++;
    }
    else{
      document.getElementById("nameError").style.display = "none";
      document.getElementById("name").style.border = '';
    }
    if (!nameCheck('lastName')) {
        borderRedError("lastName");
        document.getElementById('lastNameError').style.display = "inline";
        value++;
    }
    else{
      document.getElementById("lastNameError").style.display = "none";
      document.getElementById("lastName").style.border = '';
    }
    
    value += verifySelect("qualification",value);
    value += verifySelect("discipline",value);
    value += verifySelect("gender",value);
    console.log(value);
    if (value > 0) {
        //scrollWin();
        return false;
    }
    return true;
}


function verifySelect(id,err){
  var val = document.getElementById(id).value;
  if (val== "") {
        borderRedError(id);
        document.getElementById(id+'Error').style.display = "inline";
        err++;
    }
    else{
      document.getElementById(id+"Error").style.display = "none";
      document.getElementById(id).style.border = '';
    }
    return err;
}

function alltrim(str){
    return str.replace(/^\s+|\s+$/g, '');
}


function validate3(){
  var value = 0;

    value += verifySelect("personState",value);
    value += AddressVerify('address',value);
    if(!nameCheck('personCity')){
      borderRedError("personCity");
      document.getElementById("personCityError").style.display = "inline";
      value++;
    }
    else{
      document.getElementById('personCity').style.border = "";
      document.getElementById("personCityError").style.display = "none";
    }
    value += checkmobileNumber('mobileNumber',value);
    value += checkemergencymobileNumber('emergencyMobileNumber',value);
    value += checkPincode('pincode',value);
    value += verifySelect("faculty",value);
    isfaculty = document.getElementById('faculty').value;
    if(isfaculty=="0"){
        document.getElementById('tab4').style.display="none";
        document.getElementById('tab5').style.display="none";
        document.getElementById('tab6').style.display="none";
        document.getElementById('InstituteDetails').style.display = "none";
        document.getElementById('InstituteHeadDetails').style.display = "none";
        document.getElementById('OtherDetails').style.display = "none";
        document.getElementById('secondlabel').style.display = "none";        
    }
    else{
        document.getElementById('tab4').style.display="block";
        document.getElementById('tab5').style.display="block";
        document.getElementById('tab6').style.display="block";
        document.getElementById('InstituteDetails').style.display = "block";
        document.getElementById('InstituteHeadDetails').style.display = "block";
        document.getElementById('OtherDetails').style.display = "block";
        document.getElementById('secondlabel').style.display = "block";      
    }
    console.log(value);
    if (value > 0) {
        //scrollWin();
        return false;
    }
    return true;
}

function validate4(){
  var value=0;
  value += checkPhoto('file_input_file',value);
  value += verifySelect('designation',value);
  value += verifySelect('experience',value);
  console.log(value);
    if (value > 0) {
        //scrollWin();
        //document.getElementById("next4").disabled = true;
        return false;
    }
    //document.getElementById("next4").disabled = false;
    return true;
}

function validate4editProfile(){
  var value=0;
  value += verifySelect('designation',value);
  value += verifySelect('experience',value);
  console.log(value);
    if (value > 0) {
        //scrollWin();
        //document.getElementById("next4").disabled = true;
        return false;
    }
    //document.getElementById("next4").disabled = false;
    return true;
}

function validate5(){
  var value = 0;

  value += verifySelect('instituteState',value);
  value += verifySelect('instituteCity',value);
  value += verifySelect('instituteName',value);

  if(instituteName=="other"){
    if(!nameCheck('newinstitutename')){
      value++;
      borderRedError('newinstitutename');
      document.getElementById('newinstitutenameError').style.display = "inline";
    }
    else{
      document.getElementById('newinstitutenameError').style.display = "none";
      document.getElementById('newinstitutename').style.border = "";
    }
  }
  value += AddressVerify('instituteAddress',value);
  value += checkPincode('institutePincode',value);
  console.log(value);
    if (value > 0) {
        //scrollWin();
        //document.getElementById("next5").disabled = true;
        return false;
    }
    //document.getElementById("next5").disabled = false;
    return true;

}

function validate6(){
  var value = 0;
  value += verifySelect("instituteHeadTitle",value);

  if (!nameCheck('instituteHeadName')) {
      borderRedError("instituteHeadName");
      document.getElementById("instituteHeadNameError").style.display = "inline";
      value++;
  }
  else{
    document.getElementById("instituteHeadNameError").style.display = "none";
    document.getElementById("instituteHeadName").style.border = '';
  }

  value += verifySelect("instituteHeadDesignation",value);

  if (!emailValidator('instituteHeadEmail')) {
      borderRedError("instituteHeadEmail");
      document.getElementById("instituteHeadEmailError").style.display = "inline";
      value++;
  }
  else{
    document.getElementById("instituteHeadEmailError").style.display = "none";
    document.getElementById("instituteHeadEmail").style.border = '';
  }

  value += checkemergencymobileNumber('instituteHeadmobileNumber',value);
  value += AddressVerify('instituteHeadAddress',value);
  
    if (value > 0) {
        //scrollWin();
        //document.getElementById("next6").disabled = true;
        return false;
    }
    //document.getElementById("next6").disabled = false;
    return true;   

}

function checkmobileNumber(id,val){
    var mobileNumber = document.getElementById(id).value;
    var Exp = /^[0][7-9][0-9]*$|^[7-9][0-9]*$/;
    if (!mobileNumber.match(Exp)) {
        borderRedError(id);
        document.getElementById(id+'Error').style.display = "inline";
        val++;
    }
    else{
      document.getElementById(id+"Error").style.display = "none";
      document.getElementById(id).style.border = '';
    }
    return val;

}

function checkemergencymobileNumber(id,val){
  //var result = false;
  var emergencyMobileNumber = document.getElementById(id).value;
  var mobileNumber = document.getElementById('mobileNumber').value;
    var Exp = /^[0][7-9][0-9]*$|^[7-9][0-9]*$|^\+?[0][0-9]{8,12}$/;
    console.log(mobileNumber==emergencyMobileNumber);
    if (!emergencyMobileNumber.match(Exp) || mobileNumber==emergencyMobileNumber) {
        borderRedError(id);
        document.getElementById(id+'Error').style.display = "inline";
        val++;
    }
    else{
      document.getElementById(id+"Error").style.display = "none";
      document.getElementById(id).style.border = '';
    }
    return val;
}

function checkPincode(id,val){
  //var result = false;
  var pincode = document.getElementById(id).value;
    var Exp = /^(0|[1-9][0-9]*)$/;
    if (!pincode.match(Exp) || pincode=="") {
        borderRedError(id);
        document.getElementById(id+'Error').style.display = "inline";
        val++;
    }
    else{
      document.getElementById(id+"Error").style.display = "none";
      document.getElementById(id).style.border = '';
    }
    return val;

}

function remarkValidator(remark) {
    var result = false;
    var remarkstr = /^[A-Za-z0-9 .\r\n\\/()&:',_;-]*$/;
    if (remark.match(remarkstr)) {
        result = true;
    }
    console.log(result);
    return result;
}



