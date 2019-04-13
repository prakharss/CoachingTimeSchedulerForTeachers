function get_category_comp_wrapper(){
    var category_code=document.getElementById("comp_category_code").value;
    var comp_wrapper;
    switch(category_code){
        case "1":
            comp_wrapper="online_comp_container";
            break;
        case "2":
            comp_wrapper="ftf_comp_container";
            break;
    }
    return comp_wrapper;
}
function addComponent(){
	
    var comp_wrapper=get_category_comp_wrapper();
	var i=1;
    while(document.getElementById(comp_wrapper+"comp_div"+i)){
        i++;
    }
    $('#'+comp_wrapper).append('\
    	<div id="'+comp_wrapper+'comp_div'+i+'" class="well">\
			<div class="mdl-grid">\
				<div class="mdl-cell mdl-cell--10-col">\
				    <div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label">\
				        <input class="mdl-textfield__input" type="text" id="'+comp_wrapper+'comp_name'+i+'" name="'+comp_wrapper+'comp_name'+i+'" pattern=".*\\S+.*" required>\
				        <label  class="mdl-textfield__label" for="'+comp_wrapper+'comp_name'+i+'">Component Title</label>\
				    </div> \
				</div>\
			</div>\
			<div id="'+comp_wrapper+'assessInst_div'+i+'">\
			</div>\
			<div class="mdl-grid">\
	            <div class="mdl-cell mdl-cell--12-col ">\
	                 <button type="button" class="mdl-button--fab mdl-js-button mdl-button--raised" onclick="display_modal('+i+')" ><i class="material-icons">add</i></button>\
	                     <p style="display:inline">Add assessments</p>\
	            </div>\
         	</div>\
            <div class="mdl-grid">\
                <div class="mdl-cell mdl-cell--6-col" ></div>\
                <div class="mdl-cell mdl-cell--6-col ">\
                    <input style="display:none" type="checkbox" id="'+comp_wrapper+'comp_active'+i+'" name="'+comp_wrapper+'comp_active'+i+'" checked>\
                    <button type="button" onclick="delComponent('+i+')" class="mdl-button mdl-js-button mdl-button--raised mdl-button--accent">\
                        Delete Component\
                    </button>\
                </div>\
            </div>\
    	</div>\
    ');
    componentHandler.upgradeDom();

}
function delComponent(comp_id){
    var comp_wrapper=get_category_comp_wrapper();
    $("#"+comp_wrapper+'comp_div'+comp_id).hide();
    document.getElementById(comp_wrapper+'comp_active'+comp_id).checked=false;
    //now delete assessment within component and keep track
    var i=1;
    while(document.getElementById(comp_wrapper+'comp_div'+comp_id+'assess'+i)){
        if(document.getElementById(comp_wrapper+'comp_div'+comp_id+'assessActive'+i).checked){
            var assessType=document.getElementById(comp_wrapper+'comp_div'+comp_id+'assessType'+i).value;
            updateAssessTypesCount(assessType,"add");
        }
        i++;
    }

}

function addAssessInstances(comp_id){
    var comp_wrapper=get_category_comp_wrapper();
	assess_inst_wrapper=comp_wrapper+'assessInst_div'+comp_id;
	var i=1;
    while(document.getElementById(comp_wrapper+'comp_div'+comp_id+'assess'+i)){
        i++;
    }
    $('#'+assess_inst_wrapper).append('\
    	<div id="'+comp_wrapper+'comp_div'+comp_id+'assess'+i+'">\
    		<div class="mdl-grid">\
                <div class="mdl-cell mdl-cell--10-col" >\
                    <div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label">\
                        <input class="mdl-textfield__input" type="text" id="'+comp_wrapper+'comp_div'+comp_id+'assessName'+i+'" name="'+comp_wrapper+'comp_div'+comp_id+'assessName'+i+'" pattern=".*\\S+.*" required>\
                          <label  class="mdl-textfield__label" for="'+comp_wrapper+'comp_div'+comp_id+'assessName'+i+'">Title</label>\
                    </div>\
                    <div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label">\
                        <input class="mdl-textfield__input" type="text" id="'+comp_wrapper+'comp_div'+comp_id+'assessType'+i+'" name="'+comp_wrapper+'comp_div'+comp_id+'assessType'+i+'" pattern="\\d+" readonly>\
                          <label  class="mdl-textfield__label" for="'+comp_wrapper+'comp_div'+comp_id+'assessType'+i+'">Type</label>\
                    </div>\
                    <input style="display:none" type="checkbox" id="'+comp_wrapper+'comp_div'+comp_id+'assessActive'+i+'" name="'+comp_wrapper+'comp_div'+comp_id+'assessActive'+i+'" checked>\
                    <button type="button" onclick="delAssessInst('+comp_id+','+i+')" class="mdl-button mdl-js-button mdl-button--raised mdl-button--accent">\
                        Delete\
                    </button>\
                </div>\
            </div>\
    	</div>\
    	');
    componentHandler.upgradeDom();
    return i;

}

function delAssessInst(comp_id,assess_inst_id){
	var comp_wrapper=get_category_comp_wrapper();
	document.getElementById(comp_wrapper+'comp_div'+comp_id+'assessActive'+assess_inst_id).checked=false;	
	$('#'+comp_wrapper+'comp_div'+comp_id+'assess'+assess_inst_id).hide();
    console.log('#'+comp_wrapper+'comp_div'+comp_id+'assess'+assess_inst_id);
    updateAssessTypesCount(document.getElementById(comp_wrapper+'comp_div'+comp_id+'assessType'+assess_inst_id).value,"add");
}





// $(document).ready(function(){

//  $("#add_comp_button").click(function(e){ //on add input button click
//         e.preventDefault();
//         var x = 0; //initlal text box count
//         x++;
//         while(document.getElementById("component_div"+x)){
//             x++;
//         }
        

        
            
//         $("#outer_comp_div").append('<div  class="component" id="component_div'+x+'">\
//         <div class="mdl-grid" >\
//             <div class="mdl-cell mdl-cell--6-col ">\
//             </div>\
//         </div>\
//         <div class="mdl-grid">\
//             <div class="mdl-cell mdl-cell--6-col ">\
//                 <div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label" >\
//                     <input class="mdl-textfield__input" type="text" id="comp_name'+x+'" name="comp_name'+x+'"  required>\
//                     <label  class="mdl-textfield__label" for="comp_name'+x+'">Component Name</label>\
//                 </div>\
//             </div>\
//         </div>\
//         <div class="mdl-grid">\
//             <div class="mdl-cell mdl-cell--6-col ">\
//                 <div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label" >\
//                     <input class="mdl-textfield__input" type="text" id="comp_totalweightage'+x+'" name="comp_totalweightage'+x+'"  required>\
//                     <label  class="mdl-textfield__label" for="comp_totalweightage'+x+'">Overall Weightage</label>\
//                 </div>\
//             </div>\
//         </div>\
//         <div id="outer_assessment_div'+x+'">\
//         </div>\
//         <div class="mdl-grid">\
//             <div class="mdl-cell mdl-cell--6-col ">\
//                 <button type="button" class="mdl-button--fab mdl-js-button mdl-button--raised" onclick="addAssessments('+x+')" ><i class="material-icons">add</i></button>\
//                     <p style="display:inline">Add assessments</p>\
//             </div>\
//         </div>\
//         </div>\
//         ');
//         componentHandler.upgradeDom();
//         //componentHandler.upgradeAllRegistered(); 

        
//         //$(wrapper).append('<a href="#" class="remove_field">Remove</a></div>'); //add input box
//         x++; //text box increment
       
//     });
// });