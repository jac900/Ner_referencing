
function downloadFunc() {

	var element = document.createElement('a');
	element.setAttribute('href', process.cwd() + "/spacy_csv.csv");
	element.setAttribute('download', process.cwd() + "/spacy_csv.csv");
	document.body.appendChild(element);
	element.click();
	document.body.removeChild(element);

}
	
function downloadBase() {
	
	var element = document.createElement('a');
	element.setAttribute('href', process.cwd() + "/base_text.csv");
	element.setAttribute('download', process.cwd() + "/base_text.csv");
	document.body.appendChild(element);
	element.click();
	document.body.removeChild(element);

}




