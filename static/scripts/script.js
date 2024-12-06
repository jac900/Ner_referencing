import fs from 'fs';
import path from 'path';

export function GET(request) {
  let usersPath = path.join(process.cwd(), request);
  let file = fs.readFileSync(usersPath);
  return new Response(file);
}


function downloadFunc() {
	
	file = GET('/tmp/spacy_csv.csv')
	
	var element = document.createElement('a');
	element.setAttribute('href', file);
	element.setAttribute('download', file);
	document.body.appendChild(element);
	element.click();
	document.body.removeChild(element);

}
	
function downloadBase() {
	
	let usersPath = path.join(process.cwd(), '/tmp/base_text.csv');
    let file = fs.readFileSync(usersPath);

	
	var element = document.createElement('a');
	element.setAttribute('href', file);
	element.setAttribute('download', file);
	document.body.appendChild(element);
	element.click();
	document.body.removeChild(element);

}




