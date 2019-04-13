function check_radio(form_name){
     var radios = document.getElementsByName(form_name);

     for (var i = 0, len = radios.length; i < len; i++) {
          if (radios[i].checked) {
              return true;
          }
     }

     return false;
 }
function  pilotFormValidation(){
                        
                        if(document.getElementById("fdp_name").value.trim()==''){
                            alert("FDP name cannot be blank")
                            return;   
                        }
                        
                        //user doesn't choose any workshop while managing workshops
                        if(document.getElementById("fdp_id").value=="0" && document.getElementById("manage").checked){
                           
                            alert("Please choose a pilot FDP to manage before submitting.")
                            return;
                        }
                        if(document.getElementById("instr").value.trim()==''){
                            alert("Instruction cannot be blank")
                        }
                        var i=1;
                        while($('#cust_key'+i).length != 0){
                            if(document.getElementById("cust_key"+i).value.trim()==''){
                                 alert("Custom field names is blank");
                                 return ;
                             }
                             if(document.getElementById("cust_val"+i).value.trim()==''){
                                alert("Custom field content is blank");
                                return;
                             }
                             



                            i++;
                        }

                        if(document.getElementById("pay_iitb").checked&&document.getElementById("fee_amount").value.trim()==''){
                                alert("Fee amount cannot be blank for IITB payment mode");
                                return;
                        }
                        if(document.getElementById("reg_start_date").value.trim()==''){
                               alert("Registration start date has to be filled");
                               return;
                        }
                        if(document.getElementById("reg_end_date").value.trim()==''){
                               alert("Registration end  date has to be filled");
                               return;
                        }
                        if(document.getElementById("ws_start_date").value.trim()==''){
                                alert("Workshop start date has to be filled");
                                return;
                        }
                        if(document.getElementById("ws_end_date").value.trim()==''){
                                alert("Workshop end date has to filled ");
                                return;
                        }

                        if(document.getElementById("ann_name").value.trim()==''){
                                alert("Announcement name cannot be blank " );
                                return;
                            
                        }
                        if(document.getElementById("face_to_face_intr").checked&&!check_radio("acomm_availability")){
                                alert("Accomodation details have not been specified");
                                return;
                        }

                        if(!check_radio("perm_letter")){
                                alert("Permission letter requirements have not been specified");
                                return;
                        }

                        if(!check_radio("coll_id")){
                                alert("College id requirements have not been specified");
                                return;
                        }

                        if(document.getElementById("LMS_moodle").checked&&document.getElementById("mood_course_name").value.trim()==''){
                                alert("Moodle course name has to be filled");
                                return;
                        }
                        if(document.getElementById("LMS_iitbx").checked){
                                if(document.getElementById("iitbx_course_name").value.trim()==''){
                                  alert("IITBx course display name cannot be blank");
                                  return;
                                }
                                var withoutSpecialChar=/[a-zA-Z0-9]+/
                                if(!withoutSpecialChar.test(document.getElementById("iitbx_course_abbr").value )){
                                  alert("No special characters in course abbreviation");
                                  return;
                                }
                                if(!withoutSpecialChar.test(document.getElementById("iitbx_course_org").value )){
                                  alert("No special characters in course organisation");
                                  return;
                                }
                                if(!withoutSpecialChar.test(document.getElementById("iitbx_course_run").value )){
                                  alert("No special characters in course run");
                                  return;
                                }
                                
                                
                        }                       

                        document.getElementById("fdp_form").submit();
                    }