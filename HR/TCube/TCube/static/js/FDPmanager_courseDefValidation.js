function validateStep0(){
	if(document.getElementById("pilots").value=="-1"){
		$("#error").html("<p>Please choose a pilot FDP to continue</p>");
		return;
	}
	$("#error").html("");
	$("#step0").hide();
	$("#step1").show();

}
function validateStep1(){
	var validity=true;
	var table = document.getElementById("gradeTable");
	document.getElementById("gradeTableData").value=""
	//using below object as hashtable
	var GradeNameHashTable={};
	var error_message="";
	var lower_limits=[];
	var upper_limits=[];
	if(table.rows.length==2){
		validity=false;
		error_message="No grades defined";
	}
	for (var i = 2, row; (i<table.rows.length)&&(row = table.rows[i])&& validity; i++) {
	   //iterate through rows except the first row containing the headers
	   //rows would be accessed using the "row" variable assigned in the for loop
	   for (var j = 0, col; (col = row.cells[j]) && validity; j++) {
			//iterate through columns only upto j=3
			//columns would be accessed using the "col" variable assigned in the for loop
			if(j==4){
				//document.getElementById("gradeTableData").value=document.getElementById("gradeTableData").value+"##"
				break;				
			}
			//Grade Validation
			if(j==0){
				//make sure that there is no whitespace
				if(/\s/g.test(col.innerHTML ) ){
					validity=false;
					error_message="Grades should not contain a white-space character."
				}
				//make sure no # symbol
				if(col.innerHTML.indexOf('#')!=-1){
					validity=false;
					error_message="Grades cannot contain the symbol # in them."
				}
				//make sure no duplicate grade names
				if(validity&&GradeNameHashTable.hasOwnProperty(col.innerHTML.trim())){
					validity=false;
					error_message="Grades cannot be duplicate"
				}
				GradeNameHashTable[col.innerHTML.trim()]=1;//setting dummy value for attribute
			}
			//Lower limits
			if(j==1){
				var integer_pattern=/^\d+$/
				if(!integer_pattern.test(col.innerHTML.trim())){
 					validity=false;
 					error_message="Lower Limits have to be integers"; 
					break;
				}
				lower_limits.push(Number(col.innerHTML.trim()));

			}
			//Upper Limits
			if(j==2){
				var integer_pattern=/^\d+$/
				if(!integer_pattern.test(col.innerHTML.trim())){
 					validity=false;
 					error_message="Upper Limits have to be integers"; 
					break;
				}
				upper_limits.push(Number(col.innerHTML.trim()));

			}
			//Message should not contain #
			if(j==3){
				if(col.innerHTML.indexOf('#')!=-1){
					validity=false;
					error_message="Message cannot contain the symbol #."
				}

			}



			//document.getElementById("gradeTableData").value=document.getElementById("gradeTableData").value+col.innerHTML+"#";
			
			

	   }  
	}
	//check for upper limit and lower limit compatibility
	if(validity){
		//lower-limit not equal to upper-limit for a particular grade
		for(var i=0;i<lower_limits.length&&validity;i++){
			if(upper_limits[i]==lower_limits[i]){
				validity=false;
			}
		}
		lower_limits.sort(function(a, b){return a-b});
		upper_limits.sort(function(a, b){return a-b});
		if(lower_limits[0]!=0){
			validity=false;
			
		}
		if(upper_limits[upper_limits.length-1]!=100){
			validity=false;
			
		}
		for(var i=0;i<lower_limits.length-1&&validity;i++){
			if(upper_limits[i]!=lower_limits[i+1]){
				validity=false;
				
			}

		}
		if(!validity)
			error_message="Check grade upper limits and lower limits";
	}

	if(validity){
		$("#error").html("");
		//from editableTable.js
		convertTableData();
		//move to next step
		$("#step1").hide()
		$("#step2").show()

	}
	else{
		$("#error").html("<p>"+error_message+"</p>");
	}
}

function validateStep2(){
	var validity=true;
	var integer_pattern=/^\d+$/;
	var total_weight;
	var online_weight=document.getElementById("online_weight").value;
	var ftf_weight=document.getElementById("ftf_weight").value;
	if(!(integer_pattern.test(online_weight)) || !(integer_pattern.test(ftf_weight) ) ){
		validity=false;
		error_message="Weights have to be non negative integers";
	}
	else if((online_weight.length>3)||(ftf_weight.length>3)||(total=Number(online_weight)+Number(ftf_weight))!=100){
		
		validity=false;
		error_message="Weights have to sum upto 100";
		
	}

	if(validity){
		//next step
		$("#error").html("");
		enterTextField("online_weight_copy",document.getElementById("online_weight").value);
		$("#step2").hide();
		//initialising category code for online category
		document.getElementById("comp_category_code").value="1"
		$("#step3").show();
	}
	else{
		$("#error").html("<p>"+error_message+"</p>");

	}


}

function validateAssessTypes(){
	var validity=true;
	var error_message="";
	div_id=get_grader_type_wrapper();
	var assessTypeCount=0;
	var TypeNameHashTable={};
	var totalWeightAssess=0;
	var i=1;
	while(document.getElementById(div_id+"assessment_div"+i)){
        if(document.getElementById(div_id+'isActive'+i).checked)
        	assessTypeCount++;
        i++;
    }
    
    if(assessTypeCount>0){
    	for(i=1;(document.getElementById(div_id+"assessment_div"+i))&&validity;i++){
    		if(!(document.getElementById(div_id+'isActive'+i).checked))
    			continue;

    		//checking Assessment Types
    		console.log(div_id+'Type'+i);
    		var assessType=document.getElementById(div_id+'Type'+i).value;
    		var numoralpharegex=/^.*[a-zA-Z0-9]+.*$/
    		if(!numoralpharegex.test(assessType) ){
            	validity=false;
            	error_message="Assessment Type must have at least one alphabet or number"
            }
            //make sure no duplicate grade names
			if(validity&&TypeNameHashTable.hasOwnProperty(assessType)){
				validity=false;
				error_message="Type names cannot be duplicate"
			}
			TypeNameHashTable[assessType]=1;

			//checking Abbreviation 
    		var assessAbr=document.getElementById(div_id+'Abbr'+i).value;

    		//make sure that there is no whitespace
			if(/\s/g.test(assessAbr) ){
				validity=false;
				error_message="Abbreviation should not contain a white-space character."
			}

    		var minCount=document.getElementById(div_id+'MinCount'+i).value;
    		var integer_pattern=/^\d+$/
			if(!integer_pattern.test(minCount) ){
					validity=false;
					error_message="Count of Assessments has to be a positive integer"; 
			}
			else if(!(Number(minCount)>0)){
					validity=false;
					error_message="Count of Assessments has to be a positive integer"; 
			}



    		
    		var dropCount=document.getElementById(div_id+'DropCount'+i).value;
    		if(!integer_pattern.test(dropCount) ){
					validity=false;
					error_message="Dropabble Count of Assessments has to be a non negative integer"; 
			}
			else if(!(Number(dropCount)>=0)){
					validity=false;
					error_message="Dropabble Count of Assessments has to be a non negative integer"; 
			}

			//making sure dropCount<minCount
			if(validity&&Number(dropCount)>=Number(minCount)){
				validity=false;
				error_message="Droppable number of Assignments has to be less then total number";
			}



    		
    		var maxMarks=document.getElementById(div_id+'MaxMarks'+i).value;
    		if(!integer_pattern.test(maxMarks) ){
					validity=false;
					error_message="Maximum Marks has to be a positive integer"; 
			}
			else if(!(Number(maxMarks)>0)){
					validity=false;
					error_message="Maximum Marks has to be a positive integer"; 
			}

    		div_id+'Weight'+i
    		var totalWeight=document.getElementById(div_id+'Weight'+i).value;
    		if(!integer_pattern.test(totalWeight) ){
					validity=false;
					error_message="Total Weightage has to be a positive integer"; 
			}
			else if(!(Number(totalWeight)>0)){
					validity=false;
					error_message="Total Weightage has to be a positive integer"; 
			}
			else{
				totalWeightAssess+=Number(totalWeight);
			}
    	}
    	if(validity&&document.getElementById("comp_category_code").value=="1"&&totalWeightAssess!=Number(document.getElementById("online_weight").value)){
    		validity=false;
    		error_message="Sums of weights not equal to total weightage for online category";
    	}
    	if(validity&&document.getElementById("comp_category_code").value=="2"&&totalWeightAssess!=Number(document.getElementById("ftf_weight").value)){
    		validity=false;
    		error_message="Sums of weights not equal to total weightage for face-to-face category";
    	}

    }
    else if(document.getElementById("comp_category_code").value=="1"&&Number(document.getElementById("online_weight").value)!=0){
    	validity=false;	
    	error_message="With positive weight of online category,at least one assessment type required";
    }
    else if(document.getElementById("comp_category_code").value=="2"&&Number(document.getElementById("ftf_weight").value)!=0){
    	validity=false;
    	error_message="With positive weight of face-to-face category,at least one assessment type required";
    }
    return error_message;

}

function validateStep3(){
	
	var error_message=validateAssessTypes();

    if(!error_message){
    	//next step;
    	$("#error").html("");
    	$("#step3").hide();
    	initialiseAssessTypes()
    	$("#step4").show();
    }
    else{
    	$("#error").html("<p>"+error_message+"</p>");

    }
}
function validateComp(){
	validity=true;
	var error_message="";
	//making sure all assessments have been instantiated
	for (var prop in assessTypesSingleton) { 
		if (assessTypesSingleton.hasOwnProperty(prop)) {
			if(assessTypesSingleton[prop]>0){
				validity=false;
				error_message="Not all assessments have been instantiated yet";
			}
			if(assessTypesSingleton[prop]<0){
				validity=false;
				error_message="Some assessments have count more than specified";
			}
		} 
	}
	//all component names should have at least one non-whitespace character
	comp_wrapper=get_category_comp_wrapper();
	var comp_id=1;
	var assess_id=1;
	while(validity&&document.getElementById(comp_wrapper+"comp_div"+comp_id)){
        if(document.getElementById(comp_wrapper+'comp_active'+comp_id).checked){
        	if(!(document.getElementById(comp_wrapper+'comp_name'+comp_id).value.trim())){
	        	validity=false;
	        	error_message="Component title cannot be blank";
        	}
        	assess_id=1;
        	while(validity&&document.getElementById(comp_wrapper+'comp_div'+comp_id+'assess'+assess_id)){
        		if(document.getElementById(comp_wrapper+'comp_div'+comp_id+'assessActive'+assess_id).checked){
        			if(!(document.getElementById(comp_wrapper+'comp_div'+comp_id+'assessName'+assess_id).value.trim())){
	        			validity=false;
	        			error_message="Assessment title cannot be blank";
        			}
        			var assessType=document.getElementById(comp_wrapper+'comp_div'+comp_id+'assessType'+assess_id).value;
        			if(!assessTypesSingleton.hasOwnProperty(assessType)){
        				validity=false;
        				error_message="Assessment type is not well defined in one of the instances";
        			}
        		}
        		assess_id++;
        	}
        }
        comp_id++;
    }
    return error_message;
}
function validateStep4(){

	var error_message=validateComp();
    
	if(!error_message){
		//next step
		$("#error").html("");
		enterTextField("ftf_weight_copy",document.getElementById("ftf_weight").value);
		$("#step4").hide();
		
		//initialising category code for face-to-face category
		document.getElementById("comp_category_code").value="2"
		$("#step5").show();
	}
	else{
		$("#error").html("<p>"+error_message+"</p>");

	}

    

}

function validateStep5(){
	
	var error_message=validateAssessTypes();

    if(!error_message){
    	//next step;
    	$("#error").html("");
    	$("#step5").hide();
    	initialiseAssessTypes()
    	$("#step6").show();
    }
    else{
    	$("#error").html("<p>"+error_message+"</p>");

    }
}

function validateStep6(){
	var error_message=validateComp();
    
	if(!error_message){
		//next step
		$("#error").html("");
		$("#step6").hide();
		$("#step7").show();
	}
	else{
		$("#error").html("<p>"+error_message+"</p>");

	}
}
function formSubmit(){
	document.getElementById("grading_policy").submit();
}



