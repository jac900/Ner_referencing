function downloadFunc() {

	var element = document.createElement('a');
	element.setAttribute('href', "/tmp/spacy_csv.csv");
	element.setAttribute('download', "/tmp/spacy_csv.csv");
	document.body.appendChild(element);
	element.click();
	document.body.removeChild(element);

}
	
function downloadBase() {
	
	var element = document.createElement('a');
	element.setAttribute('href', "/tmp/base_text.csv");
	element.setAttribute('download', "/tmp/base_text.csv");
	document.body.appendChild(element);
	element.click();
	document.body.removeChild(element);

}




