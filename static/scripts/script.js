
function downloadFunc() {

	var element = document.createElement('a');
	element.setAttribute('href', process.cwd() + "/tmp/spacy_csv.csv");
	element.setAttribute('download', process.cwd() + "/tmp/spacy_csv.csv");
	document.body.appendChild(element);
	element.click();
	document.body.removeChild(element);

}
	
function downloadBase() {
	
	var element = document.createElement('a');
	element.setAttribute('href', process.cwd() + "/tmp/base_text.csv");
	element.setAttribute('download', process.cwd() + "/tmp/base_text.csv");
	document.body.appendChild(element);
	element.click();
	document.body.removeChild(element);

}




