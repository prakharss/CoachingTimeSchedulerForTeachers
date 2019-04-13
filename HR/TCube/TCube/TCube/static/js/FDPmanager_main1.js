$(document).ready(function() {
        var selected_ws_id=document.getElementById("pilots").value;
        if(selected_ws_id!="-1"){   //only if user chooses valid worskhop then only ajax request sent
            $.ajax({
                type: "GET",
                url: "getInstanceData",
                data: {"ws_id":selected_ws_id},
                dataType:'json',
                success: function(data) {
                    console.log(data["dummy"]);
                    
                    var ws=data.selected_ws[0].fields;
                    // document.getElementById("fdp_name").value=ws.workshopname;
                    // $("#fdp_name").parent().addClass("is-dirty");
                    enterTextField("fdp_id",data.selected_ws[0].pk);
                    enterTextField("fdp_name",ws.workshopname);
                    
                    document.getElementById("face_to_face_intr").checked=ws.facetofaceintrif_available;
                   

                   
                    document.getElementById("online_course").checked=ws.online_course_activityif_available;
                   

                    if(ws.categorycode==5)
                        $("#no_pay").prop("checked", true);
                    else if(ws.categorycode==8){
                        $("#iitb_pay").prop("checked",true);
                        $("fee_amount_div").show();
                    }
                    else if(ws.categorycode==7)
                        $("#rc_pay").prop("checked",true);
                    
                    enterTextField("fee_amount",ws.feeamount);
                    enterTextField("instr",ws.instructions);







                    enterTextField("reg_start_date",reverseDateFormat(ws.startdateofappli));
                    enterTextField("reg_end_date",reverseDateFormat(ws.lastdateforappli));
                    enterTextField("ws_start_date",reverseDateFormat(ws.startdate));
                    enterTextField("ws_end_date",reverseDateFormat(ws.enddate));

                    
                    document.getElementById("date_display").checked=ws.dateif_tobedisplayed;

                    if(ws.coursewarestatus=="Available Soon")
                        document.getElementById("aval_soon").checked=true;

                    else if(ws.coursewarestatus=="View/Download")
                        document.getElementById("view_down").checked=true;

                    if(ws.certificatepath!=null)
                        $("#certUploadFlag").html("<p>Already done</p>");
                    else
                        $("#certUploadFlag").html("");


                    
                    document.getElementById("instWise").checked=ws.certificate_institute_wise;
                   

                    
                    document.getElementById("rcWise").checked=ws.certificate_rc_wise;
           

                    if(ws.permissionletter!=null)
                        $("#permLetUploadFlag").html("<p>Already done</p>");
                    else
                       $("#permLetUploadFlag").html("");


                    if(ws.eligibility!=null)
                        $("#brochureUploadFlag").html("<p>Already done</p>");
                    else
                         $("#brochureUploadFlag").html("");


                    if(ws.mailcontentpath!=null)
                        $("#regSuccUploadFlag").html("<p>Already done</p>");
                    else
                        $("#regSuccUploadFlag").html("");


                    if(ws.schedulepath!=null)
                        $("#proSchedUploadFlag").html("<p>Already done</p>");
                    else
                        $("#proSchedUploadFlag").html("");

                    document.getElementById("res_path").value=ws.resourcepath;

                    document.getElementById("ann_name").value=ws.announcement;

                    if(ws.accomodation_ifavailable==1)
                        document.getElementById("acomm_avail").checked=true;
                    else
                        document.getElementById("acomm_not_avail").checked=true;

                    if(ws.permission_letter_ifrequired==1)
                        document.getElementById("perm_letter_req").checked=true;
                    else
                        document.getElementById("perm_letter_unreq").checked=true;

                    if(ws.collegeidcard_ifrequired==1)
                        document.getElementById("coll_id_req").checked=true;
                    else
                        document.getElementById("coll_id_unreq").checked=true;

                    
                    document.getElementById("LMS_moodle").checked=ws.lms_moodle;
                
                
                    document.getElementById("LMS_iitbx").checked=ws.lms_iitbx;
                    enterTextField("mood_course_name",ws.moodle_coursename);
                    enterTextField("iitbx_course_name",ws.iitbx_coursename);


                    var cust_fields=data.custom_fields;
                    
                    $(outer_wrapper).html("");
                    for(i=1;i<=cust_fields.length;i++){

                        $(outer_wrapper).append('<div class="mdl-grid">\
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
                           <label class="mdl-checkbox mdl-js-checkbox" for="cust_is_active'+i+'">\
                                <input type="checkbox" id="cust_is_active'+i+'" name="cust_is_active'+i+'" class="mdl-checkbox__input" checked>\
                                  <span class="mdl-checkbox__label">To be displayed</span>\
                            </label>\
                             </div>\
                             </div>');
                            componentHandler.upgradeDom();
                            enterTextField("cust_key"+i,cust_fields[i-1].fields.key);
                            enterTextField("cust_val"+i,cust_fields[i-1].fields.value);
                            document.getElementById("cust_is_active"+i).checked=cust_fields[i-1].fields.is_displayed;

                    }                   
            }
            });
        }

    });
    
