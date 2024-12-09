# NER.py
from flask import Flask, render_template, request
from collections import defaultdict
import spacy
import csv
import json
import vercel_blob

#app initialization
app = Flask(__name__, template_folder='./templates', static_folder='./static')

# global variables for data persistence across requests
model_input=""
model_output=""

# main index page route
@app.route('/')
def home():
    return render_template('ref.html', display_mode="none")

# route for prediction of NER model
@app.route('/predict', methods=['POST'])
def predict():

    # retrieve global variables to store input and output
    global model_input
    global model_output
    
    # get text from the incoming request (submitted on predict button click)
    data = request.form['input_text']

    # Create list of of references
    references = data.splitlines()

    # load model
    nlp = spacy.load("en_nerref_pipeline-1.0.0")

    # Rows list initialization
    rows = []

    # Iterate over list of references
    for index, ref in enumerate(references):

        # Variables for the NER categories
        typeofpublication = ""
        title = ""
        shorttitle = ""
        authorname = ""
        authorfirstname = ""
        publicationname = ""
        publicationyear = ""
        firstyearofpublication = ""
        month = ""
        volume = ""
        issue = ""
        number = ""
        pagerange = ""
        seriestitle = ""
        journalabbreviation = ""
        doi = ""
        isbn_iss = ""
        accesseddate = ""
        placeofpublication = ""
        publishinghouse = ""
        url = ""
        edition = ""
        publicationdate = ""
        editorname = ""
        editorfirstname = ""
        university = ""
        conference = ""
        database = ""
        infosupplementary = ""
        durationminutes = ""
        typeofwork = ""
        version = ""
        mediasupport = ""
        translatorfirstname = ""
        contributor1firstname = ""
        contributor2firstname = ""
        options = ""
        capacity = ""
        translatorname = ""
        numberofvolumes = ""
        multivolumenumber = ""
        seriesvolume = ""
        seriesnumber = ""
        contributor2name = ""
        book = ""
        mutivolumename = ""
        contributor1name = ""
        place = ""
        totalnumberofpages = ""
        deposityeartheses = ""
        scientificdiscipline = ""
        updateddate = ""

        # Apply model to each reference
        doc = nlp(ref)

        # Id number is set to index
        id = index

        # Initialize list
        list = []

        # For each entity discovered in the reference
        # attribute text to pertinent category variable
        for ent in doc.ents:
            
            match ent.label_:
                case 'TITLE':
                    title = ent.text
                case 'AUTHORNAME': 
                    authorname = ent.text   
                case 'AUTHORFIRSTNAME': 
                    authorfirstname = ent.text   
                case 'PUBLICATIONNAME': 
                    publicationname = ent.text   
                case 'PUBLICATIONYEAR': 
                    publicationyear = ent.text   
                case 'FIRSTYEAROFPUBLICATION': 
                    firstyearofpublication = ent.text   
                case 'MONTH': 
                    month = ent.text   
                case 'VOLUME': 
                    volume = ent.text   
                case 'ISSUE': 
                    issue = ent.text   
                case 'NUMBER': 
                    number = ent.text   
                case 'PAGERANGE': 
                    pagerange = ent.text   
                case 'SERIESTITLE': 
                    seriestitle = ent.text   
                case 'JOURNALABBREVIATION': 
                    journalabbreviation = ent.text   
                case 'DOI': 
                    doi = ent.text   
                case 'ISBN/ISS':  
                    isbn_iss = ent.text 
                case 'ACCESSEDDATE': 
                    accesseddate = ent.text   
                case 'PLACEOFPUBLICATION': 
                    placeofpublication = ent.text   
                case 'PUBLISHING HOUSE': 
                    publishinghouse = ent.text   
                case 'URL': 
                    url = ent.text   
                case 'EDITION': 
                    edition = ent.text   
                case 'PUBLICATIONDATE': 
                    publicationdate = ent.text   
                case 'EDITORNAME': 
                    editorname = ent.text   
                case 'EDITORFIRSTNAME': 
                    editorfirstname = ent.text   
                case 'UNIVERSITY': 
                    university = ent.text   
                case 'CONFERENCE': 
                    conference = ent.text   
                case 'DATABASE': 
                    database = ent.text   
                case 'INFOSUPPLEMENTARY': 
                    infosupplementary = ent.text   
                case 'DURATIONMINUTES': 
                    durationminutes = ent.text   
                case 'TYPEOFWORK': 
                    typeofwork = ent.text   
                case 'VERSION': 
                    version = ent.text   
                case 'MEDIASUPPORT': 
                    mediasupport = ent.text   
                case 'TRANSLATORFIRSTNAME': 
                    translatorfirstname = ent.text   
                case 'CONTRIBUTOR1FIRSTNAME': 
                    contributor1firstname = ent.text   
                case 'CONTRIBUTOR2FIRSTNAME': 
                    contributor2firstname = ent.text
                case 'TRANSLATORNAME': 
                    translatorname = ent.text   
                case 'NUMBEROFVOLUMES': 
                    numberofvolumes = ent.text   
                case 'MULTIVOLUMENUMBER': 
                    multivolumenumber = ent.text   
                case 'SERIESVOLUME': 
                    seriesvolume = ent.text   
                case 'SERIESNUMBER': 
                    seriesnumber = ent.text   
                case 'CONTRIBUTOR2NAME': 
                    contributor2name = ent.text   
                case 'BOOK': 
                    book = ent.text   
                case 'MUTIVOLUMENAME': 
                    mutivolumename = ent.text   
                case 'CONTRIBUTOR1NAME': 
                    contributor1name = ent.text   
                case 'PLACE': 
                    place = ent.text   
                case 'TOTALNUMBEROFPAGES': 
                    totalnumberofpages = ent.text   
                case 'DEPOSITYEARTHESES': 
                    deposityeartheses = ent.text   
                case 'SCIENTIFICDISCIPLINE': 
                    scientificdiscipline = ent.text   
                case 'UPDATEDDATE': 
                    updateddate = ent.text       

        # Type of publication is set to zero
        # Type of publication is not detected by model,
        # but can be modified later on
        typeofpublication = "0"

        # Short title is created from title or publication name
        if title != "":
            if " " in title:
                title_tokens = title.split(" ")
                shorttitle = title_tokens[0] + " " + title_tokens[1]
            else:
                shorttitle = title
        elif publicationname != "":
            if " " in publicationname:
                pub_tokens = publicationname.split(" ")
                shorttitle = pub_tokens[0] + " " + pub_tokens[1]
            else:
                shorttitle = publicationname

        # Create list of categories for the reference
        list = [id, typeofpublication, title, shorttitle, authorname, authorfirstname, publicationname, publicationyear, firstyearofpublication, month, volume, issue, number, pagerange, seriestitle, journalabbreviation, doi, isbn_iss, url, accesseddate, placeofpublication, publishinghouse, edition, publicationdate, editorname, editorfirstname, university, conference, database, infosupplementary, durationminutes, typeofwork, version, mediasupport, translatorfirstname, contributor1firstname, contributor2firstname, options, capacity, translatorname, numberofvolumes, multivolumenumber, seriesvolume, seriesnumber, contributor2name, book, mutivolumename, contributor1name, place, totalnumberofpages, deposityeartheses, scientificdiscipline, updateddate] 

        # List added to rows list
        rows.append(list)
    
    # store model input and output
    model_input = references
    model_output = rows

    # Open result template where modifications and corrections are possible
    return render_template('result.html', model_output = model_output, model_input = model_input)

# route for incremental training of model
@app.route('/save_pred', methods=['POST'])
def save_pred():

    # retrieve global variables
    global model_input
    global model_output

    # Get input data from form
    model_input = request.form['input']

    # Initialize list
    csv_data = []

    # Get data modified or corrected from form
    out_data = request.form['save_re']

    # Convert string to json dictionary
    out_data = json.loads(out_data)

    # Add out_data values to csv_data (list of lists)
    for value in out_data.values():
        csv_data.append(value)

    # Get check box value from form   
    checked = request.form['hid']

    # Initialize dictionary
    save_dict = {}

    # If we are allowed to save the date to storage
    if checked == 'false':

        # Convert input string to json dictionary        
        m_input = json.loads(model_input)

        # Merge input dict and output dict to one dictionary		
        save_dict = defaultdict(list)
        for d in (m_input, out_data):
            for key, value in d.items():
                save_dict[key].append(value)

        # Convert dictionary to string		
        save_dict = json.dumps(save_dict)

        # Create temporary file
        with open('/tmp/save_dict.txt', 'w') as f:
            f.write(save_dict)

        # Write to blob storage
        with open('/tmp/save_dict.txt', 'rb') as f:
            resp = vercel_blob.put('save_ref.txt', f.read())

    # return download page
    return render_template('download.html', csv_data = csv_data, model_input = model_input, save_dict = save_dict)

if __name__ == "__main__":
    app.run(debug=True)