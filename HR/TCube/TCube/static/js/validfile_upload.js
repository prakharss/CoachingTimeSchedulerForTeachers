function validateContent(id) {
        var value = 0;
        var inputid="mailContent"+id;
        var error="cotentFileError"+id;
        var mailcontent = document.getElementById(inputid).value;
        if (!(mailcontent == "" || mailcontent == null)) {
            var val = validateContentFile(mailcontent)
            if (val == false) {
                document.getElementById(error).innerHTML = "";
                document.getElementById(error).style.display = "inline";
                document.getElementById(error).innerHTML = "only upload html file";
                value++;
             }else{
                 document.getElementById(error).style.display = "none";
                 document.getElementById(error).value = ""; 
             }
        } else {
            document.getElementById(error).style.display = "inline";
            document.getElementById(error).innerHTML = "No file is Selected";
            value++;
        }
        
        if(value > 0){
           return false;
        }else{
            return true;
        }
    }

    function validateContentFile(content)
    {
        var result = false;
        var filext = (getExt(content)).toLowerCase();
        result = ((content != null) && (content != "") && (filext == "html"));
        return result;
    }

    function getExt(filename) {
        var dot_pos = filename.lastIndexOf(".");
        if (dot_pos == -1)
            return "";
        return filename.substr(dot_pos + 1).toLowerCase();
    }
    
    function clearError(){
        document.getElementById("cotentFileError1").style.display = "none";
        document.getElementById("cotentFileError1").value = "";
        document.getElementById("cotentFileError2").style.display = "none";
        document.getElementById("cotentFileError2").value = "";
    }