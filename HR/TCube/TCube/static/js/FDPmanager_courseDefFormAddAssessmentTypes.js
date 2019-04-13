//already defined in FDPmanager_gradingPolicy.js
// function enterTextField(dom_id,value){
//         document.getElementById(dom_id).value=value;
//         $("#"+dom_id).parent().addClass("is-dirty");
        
        
//         document.getElementById(dom_id).classList.remove('is-invalid');
//     }
function get_grader_type_wrapper(){
    var category_code=document.getElementById("comp_category_code").value;
    var div_id;
    switch(category_code){
        case "1":
            div_id="online_grader_types_container";
            break;
        case "2":
            div_id="ftf_grader_types_container";
            break;
    }
    return div_id;

}
function delAssessType(i){
    var div_id=get_grader_type_wrapper();
    document.getElementById(div_id+'isActive'+i).checked = false;
    $('#'+div_id+'assessment_div'+i).hide();
}
function addAssessmentType(mode = "slow"){
    var div_id=get_grader_type_wrapper();
    var i=1;
    while(document.getElementById(div_id+"assessment_div"+i)){
        i++;
    }
    $('#'+div_id).append('\
        <div id="'+div_id+'assessment_div'+i+'" class="well">\
            <div class="mdl-grid">\
                <div class="mdl-cell mdl-cell--10-col" >\
                    <div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label">\
                        <input class="mdl-textfield__input" type="text" id="'+div_id+'Type'+i+'" name="'+div_id+'Type'+i+'"  pattern=".*[a-zA-Z0-9]+.*" required>\
                          <label  class="mdl-textfield__label" for="'+div_id+'Type'+i+'">Assessment Type</label>\
                    </div>\
                    <div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label">\
                        <input class="mdl-textfield__input" type="text" id="'+div_id+'Abbr'+i+'" name="'+div_id+'Abbr'+i+'" pattern="\\S*" >\
                          <label  class="mdl-textfield__label" for="'+div_id+'Abbr'+i+'">Assessment Abbreviation</label>\
                    </div>\
                </div>\
            </div>\
            <div class="mdl-grid">\
                <div class="mdl-cell mdl-cell--10-col" >\
                    <div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label">\
                        <input class="mdl-textfield__input" type="text" id="'+div_id+'MinCount'+i+'" name="'+div_id+'MinCount'+i+'" pattern="\\d+" required>\
                          <label  class="mdl-textfield__label" for="'+div_id+'MinCount'+i+'">Total Number</label>\
                    </div>\
                    <div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label">\
                        <input class="mdl-textfield__input" type="text" id="'+div_id+'DropCount'+i+'" name="'+div_id+'DropCount'+i+'" pattern="\\d+" required>\
                          <label  class="mdl-textfield__label" for="'+div_id+'DropCount'+i+'">Number of Droppable</label>\
                    </div>\
                </div>\
            </div>\
            <div class="mdl-grid">\
                <div class="mdl-cell mdl-cell--10-col" >\
                    <div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label">\
                        <input class="mdl-textfield__input" type="text" id="'+div_id+'MaxMarks'+i+'" name="'+div_id+'MaxMarks'+i+'" pattern="\\d+" required>\
                          <label  class="mdl-textfield__label" for="'+div_id+'MaxMarks'+i+'">Maximum Marks</label>\
                    </div>\
                    <div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label">\
                        <input class="mdl-textfield__input" type="text" id="'+div_id+'Weight'+i+'" name="'+div_id+'Weight'+i+'" pattern="\\d+" required>\
                          <label  class="mdl-textfield__label" for="'+div_id+'Weight'+i+'">Total Weightage</label>\
                    </div>\
                </div>\
            </div>\
            <div class="mdl-grid">\
                <div class="mdl-cell mdl-cell--10-col" >\
                    <input style="display:none" type="checkbox" id="'+div_id+'isActive'+i+'" name="'+div_id+'isActive'+i+'" checked>\
                    <button type="button" onclick="delAssessType('+i+')" class="mdl-button mdl-js-button mdl-button--raised mdl-button--accent">\
                        Delete\
                    </button>\
                </div>\
            </div>\
        </div>\
    ');
    if(mode=="slow"){
        componentHandler.upgradeDom();
    }
    
    
    
    return i;

}
function addDefaultAssessmentTypes(){
    $.ajax({
            type: "GET",
            url: "/fdp/getAssessTypes",
            success: function(data) {
                var div_id;
                //online category
                document.getElementById("comp_category_code").value="1";
                div_id=get_grader_type_wrapper();
                for(var i=0;i<data["assessTypes"].length;i++){
                    assess_name=data["assessTypes"][i]["fields"]["description"];
                    assess_abr=data["assessTypes"][i]["fields"]["code"];
                    var assessID=addAssessmentType("fast");
                    console.log(assessID);
                    enterTextField(div_id+'Type'+assessID,assess_name);
                    enterTextField(div_id+'Abbr'+assessID,assess_abr);

                }
                
                //ftf category
                document.getElementById("comp_category_code").value="2";
                div_id=get_grader_type_wrapper();
                for(var i=0;i<data["assessTypes"].length;i++){
                    assess_name=data["assessTypes"][i]["fields"]["description"];
                    assess_abr=data["assessTypes"][i]["fields"]["code"];
                    var assessID=addAssessmentType("fast");
                    console.log(assessID);
                    enterTextField(div_id+'Type'+assessID,assess_name);
                    enterTextField(div_id+'Abbr'+assessID,assess_abr);

                }


                componentHandler.upgradeDom();

                
            }
    });



}


/*
function customAssessName(compID,x){
    $("#comp"+compID+"assess_type_div"+x).hide();
    $("#comp"+compID+"assess_abr"+x).prop("readonly", false);
    $("#comp"+compID+"assess_name"+x).prop("readonly", false); 
    document.getElementById("comp"+compID+'assess_name'+x).required = true;
    document.getElementById("comp"+compID+'assess_abr'+x).required = true;


}
function insertDefinedAssessment(dropdown,compID,x){
    $( "#comp"+compID+'assess_name'+x ).prop("pattern", '.*\\w+.*');
    $( "#comp"+compID+'assess_abr'+x ).prop("pattern", '.*\\w+.*');

    enterTextField("comp"+compID+'assess_name'+x,dropdown.value);
    enterTextField("comp"+compID+'assess_abr'+x,dropdown.options[dropdown.selectedIndex].text);



}
function addOption(selectbox, text, value) {
    var optn = document.createElement("OPTION");
    optn.text = text;
    optn.value = value;
    selectbox.options.add(optn);  
}

function deleteAssessments(compID,assessID){
    $("#comp"+compID+"assessment_div"+assessID).hide();
    document.getElementById("comp"+compID+"isactive"+assessID).checked=false;
}

function addAssessments(compID){
	var x = 0; //initlal text box count
        x++;
        while(document.getElementById("comp"+compID+"assessment_div"+x)){
            x++;
        }
        

        
            
        $("#outer_assessment_div"+compID).append('<div  class="assessment" id="comp'+compID+'assessment_div'+x+'">\
        <div class="mdl-grid" id="comp'+compID+'assess_type_div'+x+'">\
            <div class="mdl-cell mdl-cell--1-col"></div>\
            <div class="mdl-cell mdl-cell--3-col ">\
                <select id="comp'+compID+'assessTypes'+x+'" onchange="insertDefinedAssessment(this,'+compID+','+x+')">\
                </select>\
            </div>\
            <div class="mdl-cell mdl-cell--1-col"></div>\
            <div class="mdl-cell mdl-cell--3-col ">\
                <button class="mdl-button mdl-js-button mdl-button--raised mdl-button--colored" type="button" onclick="customAssessName('+compID+','+x+')"> Custom Name </button>\
            </div>\
        </div>\
        <div class="mdl-grid">\
            <div class="mdl-cell mdl-cell--1-col"></div>\
            <div class="mdl-cell mdl-cell--3-col ">\
                <div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label" >\
                    <input class="mdl-textfield__input" type="text" id="comp'+compID+'assess_name'+x+'" name="comp'+compID+'assess_name'+x+'"  readonly>\
                    <label  class="mdl-textfield__label" for="comp'+compID+'assess_name'+x+'">Assessment Name</label>\
                </div>\
            </div>\
            <div class="mdl-cell mdl-cell--1-col"></div>\
            <div class="mdl-cell mdl-cell--3-col ">\
                <div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label" >\
                    <input class="mdl-textfield__input" type="text" id="comp'+compID+'assess_abr'+x+'" name="comp'+compID+'assess_abr'+x+'"  readonly>\
                    <label  class="mdl-textfield__label" for="comp'+compID+'assess_abr'+x+'">Assessment Abbreviation</label>\
                </div>\
            </div>\
        </div>\
        <div class="mdl-grid">\
            <div class="mdl-cell mdl-cell--1-col"></div>\
            <div class="mdl-cell mdl-cell--3-col ">\
                <div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label" >\
                    <input class="mdl-textfield__input" type="text" id="comp'+compID+'totNum'+x+'" name="comp'+compID+'totNum'+x+'"  pattern="^\\d+$" required>\
                    <label  class="mdl-textfield__label" for="comp'+compID+'totNum'+x+'">Total Number</label>\
            </div>\
            </div>\
            <div class="mdl-cell mdl-cell--1-col"></div>\
            <div class="mdl-cell mdl-cell--3-col ">\
                <div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label" >\
                    <input class="mdl-textfield__input" type="text" id="comp'+compID+'dropNum'+x+'" name="comp'+compID+'dropNum'+x+'"  pattern="^\\d+$" required>\
                    <label  class="mdl-textfield__label" for="comp'+compID+'dropNum'+x+'">Number Droppable</label>\
                </div>\
            </div>\
        </div>\
        <div class="mdl-grid">\
            <div class="mdl-cell mdl-cell--1-col"></div>\
            <div class="mdl-cell mdl-cell--3-col ">\
                <div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label" >\
                    <input class="mdl-textfield__input" type="text" id="comp'+compID+'maxMarks'+x+'" name="comp'+compID+'maxMarks'+x+'"  pattern="^\\d+$" required>\
                    <label  class="mdl-textfield__label" for="comp'+compID+'maxMarks'+x+'">Maximum Marks</label>\
                </div>\
            </div>\
            <div class="mdl-cell mdl-cell--1-col"></div>\
            <div class="mdl-cell mdl-cell--3-col ">\
                <div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label" >\
                    <input class="mdl-textfield__input" type="text" id="comp'+compID+'totWeight'+x+'" name="comp'+compID+'totWeight'+x+'"  pattern="^\\d+$" required>\
                    <label  class="mdl-textfield__label" for="comp'+compID+'totWeight'+x+'">Total Weightage</label>\
                </div>\
            </div>\
        </div>\
        <div class="mdl-grid">\
            <div class="mdl-cell mdl-cell--5-col"></div>\
            <div class="mdl-cell mdl-cell--3-col ">\
                                <button class="mdl-button mdl-js-button mdl-button--raised mdl-button--accent" type="button" onclick="deleteAssessments('+compID+','+x+')"> Delete </button>\
            </div>\
        </div>\
        <input type="checkbox" style="display:none" id="comp'+compID+'isactive'+x+'"  name="comp'+compID+'isactive'+x+'" checked>\
    </div>\
        ');
        componentHandler.upgradeDom();
        var assess_name,assess_abr;
        

        $.ajax({
            type: "GET",
            url: "/fdp/getAssessTypes",
            success: function(data) {
                
                
                var dropdown = document.getElementById("comp"+compID+"assessTypes"+x);
                assess_name=data["assessTypes"][0]["fields"]["description"];
                assess_abr=data["assessTypes"][0]["fields"]["code"];
                for (var i=0; i < data["assessTypes"].length;++i){    
                    addOption(dropdown, data["assessTypes"][i]["fields"]["description"],data["assessTypes"][i]["fields"]["code"] );
                
                }
                enterTextField('comp'+compID+'assess_name'+x,assess_name);
                enterTextField('comp'+compID+'assess_abr'+x,assess_abr);
                


                
            }
            });
        $("#comp"+compID+"totNum"+x).parent().removeClass('is-invalid');
        document.getElementById("comp"+compID+"totNum"+x).required = true;

        

}
*/