var assessTypesSingleton={}
var selectOptOrder={}



function resetAssessTypes(){
	for (var prop in assessTypesSingleton) { 
		if (assessTypesSingleton.hasOwnProperty(prop)) {
			delete assessTypesSingleton[prop]; 
		} 
	}
	for (var prop in selectOptOrder) { 
		if (selectOptOrder.hasOwnProperty(prop)) {
			delete selectOptOrder[prop]; 
		} 
	}
}
function initialiseAssessTypes(){
	resetAssessTypes();
	//clear select input
	var selectMenu = document.getElementById("assessTypesTrackerSelect");

    for(var i = selectMenu.options.length - 1 ; i >= 0 ; i--)
    {
        selectMenu.remove(i);
    }
    
	var div_id=get_grader_type_wrapper();
	for(var i=1;document.getElementById(div_id+"assessment_div"+i);i++){
    		if(!(document.getElementById(div_id+'isActive'+i).checked))
    			continue;
    		var assessType=document.getElementById(div_id+'Type'+i).value;
    		var minCount=document.getElementById(div_id+'MinCount'+i).value;
    		assessTypesSingleton[assessType]=Number(minCount);
    }
    //Considering prior existence of assessment instances
    var comp_wrapper=get_category_comp_wrapper();
	var comp_id=1;
	var assess_id=1;
	while(document.getElementById(comp_wrapper+"comp_div"+comp_id)){
		
        if(document.getElementById(comp_wrapper+'comp_active'+comp_id).checked){
        	
        	assess_id=1;
        	while(document.getElementById(comp_wrapper+'comp_div'+comp_id+'assess'+assess_id)){
        		
        		if(document.getElementById(comp_wrapper+'comp_div'+comp_id+'assessActive'+assess_id).checked){
        			
        			assessType=document.getElementById(comp_wrapper+'comp_div'+comp_id+'assessType'+assess_id).value;
        			
        			if(assessTypesSingleton.hasOwnProperty(assessType)){
        				
        				assessTypesSingleton[assessType]-=1;
        			}
        		}
        		assess_id++;
        	}
        }
        comp_id++;
    }
    //Creating new select options
   	var default_opt=document.createElement('option');
   	default_opt.value="_";
   	default_opt.innerHTML="Choose the type";
   	selectMenu.appendChild(default_opt);
   	var i=1;
    for (var prop in assessTypesSingleton){
	    if (assessTypesSingleton.hasOwnProperty(prop)) {
		   	var opt = document.createElement('option');
		    opt.value = prop;
		    if(assessTypesSingleton[prop]>=0){
		    	opt.innerHTML = prop+" - "+assessTypesSingleton[prop];
		    }
		    else{
		    	opt.innerHTML=prop+"-"+"Too many instances";
		    }
		    selectMenu.appendChild(opt);
		   	if(assessTypesSingleton[prop]<=0){
		   		selectMenu.options[i].disabled=true;
		   	}
		    selectOptOrder[prop]=i;
		    i++;
		}
	}

	selectMenu.value="_";
}
function updateAssessTypesCount(AssessType,mode){
	var selectMenu = document.getElementById("assessTypesTrackerSelect");
	if(mode=="sub"){
		assessTypesSingleton[AssessType]-=1;
		if(assessTypesSingleton[AssessType]==0){
			selectMenu.options[selectOptOrder[AssessType]].disabled=true;
		}

	}
	else if(mode=="add"){
		assessTypesSingleton[AssessType]+=1;
		if(assessTypesSingleton[AssessType]==1){
			selectMenu.options[selectOptOrder[AssessType]].disabled=false;
		}
	}
	
	if(assessTypesSingleton[AssessType]>=0){
		for (var prop in selectOptOrder){
		    if (selectOptOrder.hasOwnProperty(prop)) {
			  
			   console.log(prop);
			}
		}
		console.log(AssessType);
		selectMenu.options[selectOptOrder[AssessType]].innerHTML = AssessType+" - "+assessTypesSingleton[AssessType];
	}
	else{
		selectMenu.options[selectOptOrder[AssessType]].innerHTML = AssessType+" - "+"Too many instances";
	}
	
	selectMenu.value="_";

}


