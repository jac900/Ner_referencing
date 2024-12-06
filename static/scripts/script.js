import fs from 'fs';
import path from 'path';


function downloadFunc() {
	
	#vercel_blob.download_file(spacy_csv, '/tmp/spacy_csv.csv')
	
	let csvContent = ''
    data = {{ csv_data|tojson }}

	data.forEach(row => {
	csvContent += row.join(',') + '\n'
	})

    const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8,' })
	const objUrl = URL.createObjectURL(blob)
	
	const link = document.createElement('a')
    link.setAttribute('href', objUrl)
    link.setAttribute('download', 'File.csv')
    link.textContent = 'Click to Download'
	
	

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




