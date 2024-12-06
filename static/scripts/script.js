import fs from 'fs';
import path from 'path';


function downloadFunc() {
	
	#vercel_blob.download_file(spacy_csv, '/tmp/spacy_csv.csv')
	
	var element = document.createElement('a');
	element.setAttribute('href', '/tmp/spacy_csv.csv');
	element.setAttribute('download', '/tmp/spacy_csv.csv');
	document.body.appendChild(element);
	element.click();
	document.body.removeChild(element);

}
	
function downloadBase() {
	
    #vercel_blob.download_file(base_text, '/tmp/base_text.csv')
	
	var element = document.createElement('a');
	element.setAttribute('href', '/tmp/base_text.csv');
	element.setAttribute('download', '/tmp/base_text.csv');
	document.body.appendChild(element);
	element.click();
	document.body.removeChild(element);

}




