function showform(url){
	$("#myModalContent").load(url);
};
function deleteform(url){
	$("#myModalContent").load(url, function() {window.location.reload();});
}
