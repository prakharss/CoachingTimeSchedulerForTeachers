
//for deleting custom added fields
function delete_cust_key(cust_id){
    $("#cust_key_val_div"+cust_id).hide();
    $("#cust_is_active"+cust_id).prop("checked",false);
}
function reset_fields(){
        var fdp_type=$("#fdp_type").val();

        //$('#fdp_form')[0].reset();
        

        // //text fields
        // enterTextField('fdp_name','');
        // enterTextField('instr','');
        // enterTextField('fee_amount','');
        // enterTextField('reg_start_date','');
        // enterTextField('reg_end_date','');
        // enterTextField('ws_start_date','');
        // enterTextField('ws_end_date','');
        // enterTextField('ann_name','');
        // enterTextField('mood_course_name','');
        // enterTextField('iitbx_course_name','');
        // // custom fields
        // $("#cust_div").html("");
        // // input file fields
        // document.getElementById("certUpload").value = "";
        // document.getElementById("permLetUpload").value = "";
        // document.getElementById("brochureUpload").value = "";
        // document.getElementById("eligUpload").value = "";
        // document.getElementById("regSuccUpload").value = "";
        // document.getElementById("proSchedUpload").value = "";
        // //checkbox


// document.querySelector('.mdl-textfield  input').value = '';
// document.querySelector('.mdl-textfield').MaterialTextfield.change();

var chx = document.getElementsByTagName('input');
  for (var i=0; i<chx.length; i++) {
    
    if(chx[i].type=='file'){
             chx[i].value="";
            chx[i].type='file';
    }

    if (chx[i].type == 'radio') {
        chx[i].parentNode.MaterialRadio.uncheck();
    } 
    if(chx[i].type=='checkbox'){
        if(chx[i].parentNode.MaterialCheckbox!=null)
                chx[i].parentNode.MaterialCheckbox.uncheck();
    }
    if(chx[i].type=='text'){
        if(chx[i].parentNode.MaterialTextfield!=null)
            chx[i].parentNode.MaterialTextfield.change('');
    }
  }
  document.getElementById("fdp_type").parentNode.MaterialTextfield.change(fdp_type);
  document.getElementById("date_display").parentNode.MaterialCheckbox.check();
  document.getElementById("aval_soon").parentNode.MaterialRadio.check();
  $("#fee_amount_div").hide();
  $("#mood_course_div").hide();
  $("#iitbx_course_div").hide();

        // document.getElementById('instWise').parentNode.MaterialCheckbox.check();
        // document.getElementById('rcWise').parentNode.MaterialCheckbox.check();
        // document.getElementById('LMS_moodle').parentNode.MaterialCheckbox.check();
        // document.getElementById('LMS_iitbx').parentNode.MaterialCheckbox.check();
        // document.getElementById('instWise').parentNode.MaterialCheckbox.check();
        // document.getElementById('instWise').parentNode.MaterialCheckbox.check();
        // document.getElementById('instWise').parentNode.MaterialCheckbox.check();
        // document.getElementById('instWise').parentNode.MaterialCheckbox.check();



}

$(document).ready(function(){
    var outer_wrapper     ="#cust_div"; //Fields wrapper
     


    //switching between create and manage mode
     $("#switch_button").click(function(){
        
        if(document.getElementById("manage").checked==true){
            //reset_fields();
            document.getElementById("manage").checked=false;
            var temp_main_heading=$("#main_heading").html();
            temp_main_heading=$(temp_main_heading).text();
            $("#main_heading").html("<h1>"+$('#switch_button').html()+"</h1>");
            $("#switch_button").html(temp_main_heading);
            //console.log(temp_main_heading);
            $.ajax({
            type: "GET",
            url: "getNextWorkshopId",
            success: function(data) {
                enterTextField("fdp_id",data[0]);
                
            }
            });
            enterTextField("resp_coord_id","0");
            $(".manage_fdp").hide();
            $(outer_wrapper).html("");
     //        $('#fdp_name').removeAttr('required');
     //        $('#instr').removeAttr('required');
     //        $('#fee_amount').removeAttr('required');
     //        $('#reg_start_date').removeAttr('required');
     //        $('#reg_end_date').removeAttr('required');
     //        $('#ws_start_date').removeAttr('required');
        // $('#ws_end_date').removeAttr('required');
     //        $('#ann_name').removeAttr('required');
        // $('#mood_course_name').removeAttr('required');
     //        $('#iitbx_course_name').removeAttr('required');
            



        }
         else{
            reset_fields();
            document.getElementById("manage").checked=true;
            var temp_main_heading=$("#main_heading").html();
            temp_main_heading=$(temp_main_heading).text();
            $("#main_heading").html("<h1>"+$('#switch_button').html()+"</h1>");
            $("#switch_button").html(temp_main_heading);
             $(".manage_fdp").show();
             enterTextField("fdp_id","");
             
             $("#pilots").val("-1");
             
        }
     });

    
    
    var max_fields      = 100; //maximum input boxes allowed
    
    
    
    //adding custom key value fields
    $(add_button).click(function(e){ //on add input button click
        e.preventDefault();
        var x = 0; //initlal text box count
        x++;
        while(document.getElementById("cust_key"+x)){
            x++;
        }
        

        if(x < max_fields){ //max input box allowed
            
            $(outer_wrapper).append('<div class="mdl-grid" id="cust_key_val_div'+x+'">\
            <div class="mdl-cell mdl-cell--3-col mdl-cell--top">\
            <div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label" id="cust_key_div'+x+'">\
            <input class="mdl-textfield__input" type="text" id="cust_key'+x+'" name="cust_key'+x+'"  >\
           <label  class="mdl-textfield__label" for="cust_key'+x+'">Field name</label>\
             </div>\
            </div>\
            <div class="mdl-cell mdl-cell--3-col">\
            <div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label" id="cust_val_div'+x+'">\
            <textarea class="mdl-textfield__input" type="text" rows= "6" id="cust_val'+x+'" name="cust_val'+x+'" ></textarea>\
           <label  class="mdl-textfield__label" for="cust_val'+x+'">Field content</label>  </div>\
            </div>\
            <div class="mdl-cell mdl-cell--4-col mdl-cell--middle">\
            <button type="button" onclick="delete_cust_key('+x+')" class="mdl-button mdl-js-button mdl-button--raised mdl-button--colored"> Delete </button>\
                <input type="checkbox" id="cust_is_active'+x+'" name="cust_is_active'+x+'" class="mdl-checkbox__input" style="display:none" checked>\
             </div>\
             </div>');
            componentHandler.upgradeDom();
            //componentHandler.upgradeAllRegistered(); 

            
            //$(wrapper).append('<a href="#" class="remove_field">Remove</a></div>'); //add input box
            x++; //text box increment
        }
    });
    

    
    $("#face_to_face_intr").change(function(){
        $("#pay_rc_div").toggle();
        $("#accom_div").toggle();

    });




    $(".has_datepicker").datepicker({

        dateFormat: 'dd-mm-yy', 
      onSelect: function(dateText) {
        $(this).parent().addClass("is-dirty");
        $(this).parent().removeClass("is-invalid");
      }
    });


    $("#LMS_moodle").change(function(){
        $("#mood_course_div").toggle();
    });
    $("#LMS_iitbx").change(function(){
        $("#iitbx_course_div").toggle();
    });
    $("#pay_iitb").change(function(){
        
        if(document.getElementById("pay_iitb").checked){
            $("#fee_amount_div").show();
        }
        else{
            $("#fee_amount_div").hide();

        }
    });

    MaterialTextfield.prototype.CssClasses_ = {
        LABEL: 'mdl-textfield__label',
        INPUT: 'mdl-textfield__input',
        IS_DIRTY: 'is-dirty',
        IS_FOCUSED: 'is-focused',
        IS_DISABLED: 'is-disabled',
        IS_INVALID: 'is-invalid',
        IS_UPGRADED: 'is-upgraded',
        HAS_PLACEHOLDER: 'has-placeholder'
      };
    function enterTextField(dom_id,value){
        document.getElementById(dom_id).value=value;
        $("#"+dom_id).parent().addClass("is-dirty");
        
        
        document.getElementById(dom_id).classList.remove('is-invalid');
    }
    function reverseDateFormat(date_string){
        date_comp=date_string.split('-');
        result_date=date_comp[2]+"-"+date_comp[1]+"-"+date_comp[0];
        return result_date;
    }


    // CSRF code
    function getCookie(name) {
        var cookieValue = null;
        var i = 0;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (i; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        crossDomain: false, // obviates need for sameOrigin test
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    //filling workshop data based on change in selection of the manage workshops dropdown
    $("#pilots").change(function(){
        var selected_ws_id=document.getElementById("pilots").value;
        if(selected_ws_id=="-1"){
            alert("Please select a pilot FDP to manage");
            reset_fields();
        }



        else{   
            $.ajax({
                type: "GET",
                url: "getWorkshopData",
                data: {"ws_id":selected_ws_id},
                dataType:'json',
                success: function(data) {

                    
                    
                    var ws=data.selected_ws[0].fields;
                    
                    // document.getElementById("fdp_name").value=ws.workshopname;
                    // $("#fdp_name").parent().addClass("is-dirty");
                    enterTextField("fdp_id",data.selected_ws[0].pk);
                    enterTextField("fdp_name",ws.workshopname);
                    enterTextField("resp_coord_id",ws.respective_coordinatorid);


                    if(ws.workshop_by_invite==1)
                        document.getElementById('ws_by_invite').parentNode.MaterialCheckbox.check();
                    else
                        document.getElementById('ws_by_invite').parentNode.MaterialCheckbox.uncheck();
                   if(ws.facetofaceintrif_available==1){
                                      document.getElementById('face_to_face_intr').parentNode.MaterialCheckbox.check();
                                      $("#pay_rc_div").show();
                                      $("#accom_div").show();
                    }
                    else{
                        document.getElementById('face_to_face_intr').parentNode.MaterialCheckbox.uncheck();
                        $("#pay_rc_div").hide();
                        $("#accom_div").hide();
                    }

                   if(ws.online_course_activityif_available==1)
                        document.getElementById('online_course').parentNode.MaterialCheckbox.check();
                    else
                        document.getElementById('online_course').parentNode.MaterialCheckbox.uncheck();
                   
                    if(ws.rc_payment_if_required==1){
                        document.getElementById('pay_rc').parentNode.MaterialCheckbox.check();

                    }
                    else{
                        document.getElementById('pay_rc').parentNode.MaterialCheckbox.uncheck();

                    }

                    if(ws.iitb_payment_if_required==1){
                        document.getElementById('pay_iitb').parentNode.MaterialCheckbox.check();
                        $("#fee_amount_div").show();

                    }
                    else{
                        document.getElementById('pay_iitb').parentNode.MaterialCheckbox.uncheck();
                        $("#fee_amount_div").hide();

                    }
                   

                    enterTextField("fee_amount",ws.feeamount);
                    enterTextField("instr",ws.instructions);







                    enterTextField("reg_start_date",reverseDateFormat(ws.startdateofappli));
                    enterTextField("reg_end_date",reverseDateFormat(ws.lastdateforappli));
                    enterTextField("ws_start_date",reverseDateFormat(ws.startdate));
                    enterTextField("ws_end_date",reverseDateFormat(ws.enddate));
                    

                    if(ws.dateif_tobedisplayed==1)
                        document.getElementById('date_display').parentNode.MaterialCheckbox.check();
                    else
                        document.getElementById('date_display').parentNode.MaterialCheckbox.uncheck();

                    if(ws.coursewarestatus=="Available Soon"){
                        document.getElementById('view_down').parentNode.MaterialRadio.uncheck();
                        document.getElementById("aval_soon").parentNode.MaterialRadio.check();
                    }
                

                    else if(ws.coursewarestatus=="View/Download"){
                        
                        document.getElementById('view_down').parentNode.MaterialRadio.check();
                        document.getElementById("aval_soon").parentNode.MaterialRadio.uncheck();

                    }
                    
                    if(ws.certificatepath!=null)
                        ;
                        //$("#certUploadFlag").html("<p>Already done</p>");
                    else
                        $("#certUploadFlag").html("");


                    if(ws.certificate_institute_wise==1){
                                      document.getElementById('instWise').parentNode.MaterialCheckbox.check();
                    }
                    else
                        document.getElementById('instWise').parentNode.MaterialCheckbox.uncheck();
                    
                   

                     if(ws.certificate_rc_wise==1){
                                      document.getElementById('rcWise').parentNode.MaterialCheckbox.check();
                    }
                    else
                        document.getElementById('rcWise').parentNode.MaterialCheckbox.uncheck();
           

                    if(ws.permissionletter!=null)
                        ;
                        //$("#permLetUploadFlag").html("<p>Already done</p>");
                    else
                       $("#permLetUploadFlag").html("");


                    if(ws.eligibility!=null)
                        ;
                        //$("#brochureUploadFlag").html("<p>Already done</p>");
                    else
                         $("#brochureUploadFlag").html("");


                    if(ws.mailcontentpath!=null)
                        ;
                        //$("#regSuccUploadFlag").html("<p>Already done</p>");
                    else
                        $("#regSuccUploadFlag").html("");


                    if(ws.schedulepath!=null)
                        ;
                        //$("#proSchedUploadFlag").html("<p>Already done</p>");
                    else
                        $("#proSchedUploadFlag").html("");

                   
                    enterTextField("res_path",ws.resourcepath);
                    enterTextField("ann_name",ws.announcement);

                    if(ws.accomodation_ifavailable==1){
                        document.getElementById('acomm_not_avail').parentNode.MaterialRadio.uncheck();
                        document.getElementById("acomm_avail").parentNode.MaterialRadio.check();
                    }
                

                    else{
                        
                        document.getElementById('acomm_not_avail').parentNode.MaterialRadio.check();
                        document.getElementById("acomm_avail").parentNode.MaterialRadio.uncheck();

                    }

                    if(ws.permission_letter_ifrequired==1){
                        document.getElementById('perm_letter_unreq').parentNode.MaterialRadio.uncheck();
                        document.getElementById("perm_letter_req").parentNode.MaterialRadio.check();
                    }
                

                    else{
                        
                        document.getElementById('perm_letter_unreq').parentNode.MaterialRadio.check();
                        document.getElementById("perm_letter_req").parentNode.MaterialRadio.uncheck();

                    }
                    if(ws.collegeidcard_ifrequired==1){
                        document.getElementById('coll_id_unreq').parentNode.MaterialRadio.uncheck();
                        document.getElementById("coll_id_req").parentNode.MaterialRadio.check();
                    }
                

                    else{
                        
                        document.getElementById('coll_id_unreq').parentNode.MaterialRadio.check();
                        document.getElementById("coll_id_req").parentNode.MaterialRadio.uncheck();

                    }

                    


                    if(ws.lms_moodle==1){
                                      document.getElementById('LMS_moodle').parentNode.MaterialCheckbox.check();
                                        $('#mood_course_div').show();
                                        enterTextField("mood_course_name",ws.moodle_coursename);
                    }
                    else{
                        document.getElementById('LMS_moodle').parentNode.MaterialCheckbox.uncheck();
                        $("#mood_course_div").hide();
                        $("#mood_course_name").parent().addClass("is-invalid");

                    }
           
                    
                   if(ws.lms_iitbx==1){
                        document.getElementById('LMS_iitbx').parentNode.MaterialCheckbox.check();
                        $("#iitbx_course_div").show();
                        enterTextField("iitbx_course_name",ws.iitbx_coursename);
                        $('#iitbx_course_name').parent().removeClass('is-invalid');
                        var splitStrings=ws.iitbx_coursekey.split("+");
                        //temporary workaround for workshops which didn't have this before
                        if(splitStrings.length==1)
                            ;
                        else{
                            var org=splitStrings[0];
                            var abbr=splitStrings[1];
                            var run=splitStrings[2];
                            enterTextField("iitbx_course_org",org);
                            $('#iitbx_course_org').parent().removeClass('is-invalid');
                            enterTextField("iitbx_course_abbr",abbr);
                            $('#iitbx_course_abbr').parent().removeClass('is-invalid');
                            enterTextField("iitbx_course_run",run);
                            $('#iitbx_course_run').parent().removeClass('is-invalid');
                        }
                    }
                    else{
                        document.getElementById('LMS_iitbx').parentNode.MaterialCheckbox.uncheck();
                        $("#iitbx_course_div").hide();
                        $("#iitbx_course_name").parent().addClass("is-invalid");
                        $("#iitbx_course_org").parent().addClass("is-invalid");
                        $("#iitbx_course_abbr").parent().addClass("is-invalid");
                        $("#iitbx_course_run").parent().addClass("is-invalid");
                        
                    }
                    

                   
                    
                    
                    


                    var cust_fields=data.custom_fields;
                    
                    $(outer_wrapper).html("");
                    for(i=1;i<=cust_fields.length;i++){

                        $(outer_wrapper).append('<div class="mdl-grid" id="cust_key_val_div'+i+'">\
                            <div class="mdl-cell mdl-cell--3-col mdl-cell--top">\
                            <div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label" id="cust_key_div'+i+'">\
                            <input class="mdl-textfield__input" type="text" id="cust_key'+i+'" name="cust_key'+i+'"  >\
                           <label  class="mdl-textfield__label" for="cust_key'+i+'">Field name</label>\
                             </div>\
                            </div>\
                            <div class="mdl-cell mdl-cell--3-col">\
                            <div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label" id="cust_val_div'+i+'">\
                            <textarea class="mdl-textfield__input" type="text" rows= "6" id="cust_val'+i+'" name="cust_val'+i+'" ></textarea>\
                           <label  class="mdl-textfield__label" for="cust_val'+i+'">Field content</label>  </div>\
                            </div>\
                            <div class="mdl-cell mdl-cell--4-col mdl-cell--middle">\
                           <button type="button" onclick="delete_cust_key('+i+')" class="mdl-button mdl-js-button mdl-button--raised mdl-button--colored"> Delete </button>\
                            <input type="checkbox" id="cust_is_active'+i+'" name="cust_is_active'+i+'" class="mdl-checkbox__input" style="display:none" checked>\
                             </div>\
                             </div>');
                            componentHandler.upgradeDom();
                            enterTextField("cust_key"+i,cust_fields[i-1].fields.key);
                            enterTextField("cust_val"+i,cust_fields[i-1].fields.value);
                            if(cust_fields[i-1].fields.is_displayed==1)
                                      document.getElementById("cust_is_active"+i).checked=true;
                   
                            else{
                                document.getElementById("cust_is_active"+i).checked=false;
                                $("#cust_key_val_div"+i).hide();

                            }

                    }
                        $('#fdp_name').parent().removeClass('is-invalid');
            $('#instr').parent().removeClass('is-invalid');
            $('#fee_amount').parent().removeClass('is-invalid');
            $('#reg_start_date').parent().removeClass('is-invalid');
            $('#reg_end_date').parent().removeClass('is-invalid');
            $('#ws_start_date').parent().removeClass('is-invalid');
        $('#ws_end_date').parent().removeClass('is-invalid');
            $('#ann_name').parent().removeClass('is-invalid');
        
                    
                    
                   
                   
            }
            });
        }

    });
     
   

     $(".readonly").keydown(function(e){
        e.preventDefault();
    });
     $('.readonly').bind("cut paste",function(e) {
     e.preventDefault();
 });
        //     $('#fdp_name').removeAttr('required');
        //     $('#instr').removeAttr('required');
        //     $('#fee_amount').removeAttr('required');
        //     $('#reg_start_date').removeAttr('required');
        //     $('#reg_end_date').removeAttr('required');
        //     $('#ws_start_date').removeAttr('required');
        // $('#ws_end_date').removeAttr('required');
        //     $('#ann_name').removeAttr('required');
        // $('#mood_course_name').removeAttr('required');
        //     $('#iitbx_course_name').removeAttr('required');


        $(this).find("textarea").on( "input change ", function() {

        $(".textarea_v").parent().addClass("is-invalid");
        var pattern = $( this ).attr( "pattern" );

        if(typeof pattern !== typeof undefined && pattern !== false)
        {
            var patternRegex = new RegExp( '^' + pattern +  '$', "g" );

            hasError = !$( this ).val().match( patternRegex );
            //console.log("entering");
            if(hasError){

                //$(this).parent().addClass('is-invalid');
                

                //console.log("error");
            }
            else
                $(this).parent().addClass('is-invalid');
        }

    });

});

