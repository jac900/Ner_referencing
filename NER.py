# app.py
from flask import Flask, render_template, request
import spacy
import csv
import json
import io

#app initialization
app = Flask(__name__, template_folder='./templates', static_folder='./static')

# global variables for data persistence across requests
model_input=""
model_output=""

# main index page route
@app.route('/')
def home():
    return render_template('ref.html', display_mode="none")

# route for prediction of sentiment analysis model and classifier
@app.route('/predict', methods=['POST'])
def predict():
    # retrieve global variables to store input and output
    global model_input
    global model_output
    
    # get text from the incoming request (submitted on predict button click)
    data = request.form['input_text']

    references = data.splitlines()

    #print(references)
    # load model
    nlp = spacy.load("en_nerref_pipeline-1.0.0")

    rows = []

    for index, ref in enumerate(references):

        print(index, ref)

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
        
        doc = nlp(ref)
        id = index
        
        list = []
        
        for ent in doc.ents:
            
            #print(ent.text, ent.label_)
            
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

        typeofpublication = "0"

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

        list = [id, typeofpublication, title, shorttitle, authorname, authorfirstname, publicationname, publicationyear, firstyearofpublication, month, volume, issue, number, pagerange, seriestitle, journalabbreviation, doi, isbn_iss, url, accesseddate, placeofpublication, publishinghouse, edition, publicationdate, editorname, editorfirstname, university, conference, database, infosupplementary, durationminutes, typeofwork, version, mediasupport, translatorfirstname, contributor1firstname, contributor2firstname, options, capacity, translatorname, numberofvolumes, multivolumenumber, seriesvolume, seriesnumber, contributor2name, book, mutivolumename, contributor1name, place, totalnumberofpages, deposityeartheses, scientificdiscipline, updateddate] 
        #print(list)
        rows.append(list)
        
    #print(rows)
    
    # store model input and output
    model_input = references
    model_output = rows
    return render_template('result.html', model_output = model_output, model_input = model_input)

# route for incremental training of model
@app.route('/save_pred', methods=['POST'])
def save_pred():
    # retrieve global variables
    global model_input
    global model_output
    csv_data = []
    
    out_data = request.form['save_re']

    out_data = json.loads(out_data)
    
    for value in out_data.values():
        csv_data.append(value)

    print("csv_data:", csv_data)

    # field names 
    fields = ['ID', 'TYPEOFPUBLICATION', 'TITLE', 'SHORTTITLE', 'AUTHORNAME', 'AUTHORFIRSTNAME', 'PUBLICATIONNAME', 'PUBLICATIONYEAR', 'FIRSTYEAROFPUBLICATION', 'MONTH', 'VOLUME', 'ISSUE', 'NUMBER', 'PAGERANGE', 'SERIESTITLE', 'JOURNALABBREVIATION', 'DOI', 'ISBN/ISSN', 'URL', 'ACCESSEDDATE', 'PLACEOFPUBLICATION', 'PUBLISHINGHOUSE', 'EDITION', 'PUBLICATIONDATE', 'EDITORNAME', 'EDITORFIRSTNAME', 'UNIVERSITY', 'CONFERENCE', 'DATABASE', 'INFOSUPPLEMENTARY', 'DURATIONMINUTES', 'TYPEOFWORK', 'VERSION', 'MEDIASUPPORT', 'TRANSLATORFIRSTNAME', 'CONTRIBUTOR1FIRSTNAME', 'CONTRIBUTOR2FIRSTNAME', 'OPTIONS', 'CAPACITY', 'TRANSLATORNAME', 'NUMBEROFVOLUMES', 'MULTIVOLUMENUMBER', 'SERIESVOLUME', 'SERIESNUMBER', 'CONTRIBUTOR2NAME', 'BOOK', 'MUTIVOLUMENAME', 'CONTRIBUTOR1NAME', 'PLACE', 'TOTALNUMBEROFPAGES', 'DEPOSITYEARTHESES', 'SCIENTIFICDISCIPLINE', 'UPDATEDDATE'] 
    """
    spacy_csv = io.StringIO()
            
    # using csv.writer method from CSV package
    write = csv.writer(spacy_csv)
         
    write.writerow(fields)
    write.writerows(csv_data) 

    file1 = request.files[spacy_csv]
    #print(file.filename)
    vercel_blob.put(file.filename, file.read(), {})

    #########################

    btext = []
    for string in model_input:
        btext.append([string])

    base_text = io.StringIO()

    # using csv.writer method from CSV package
    write = csv.writer(base_text)
         
    write.writerow(["Base_Text"])
    write.writerows(btext)

    file = request.files[base_text]
    #print(file.filename)
    vercel_blob.put(file.filename, file.read(), {})
    """


    with open('/tmp/spacy_csv.csv', 'w', newline='') as f:
         
        # using csv.writer method from CSV package
        write = csv.writer(f)
         
        write.writerow(fields)
        write.writerows(csv_data) 

    file1 = request.files['/tmp/spacy_csv.csv']
    print(file1.filename)
    vercel_blob.put(file1.filename, file1.read(), {})

    btext = []
    for string in model_input:
        btext.append([string])

    print(btext)

    with open('/tmp/base_text.csv', 'w', newline='') as fb:
         
        # using csv.writer method from CSV package
        write = csv.writer(fb)
         
        write.writerow(["Base_Text"])
        write.writerows(btext)

    file2 = request.files['/tmp/base_text.csv']
    print(file2.filename)
    vercel_blob.put(file2.filename, file2.read(), {})



    """
    checked = request.form['hid']

    print(checked)

    if checked == 'false':

        with open('./static/output/spacy_csv_acc.csv', 'a', newline='') as file:
            write = csv.writer(file)
            write.writerow(fields)
            write.writerows(csv_data)

        with open('./static/output/base_text_acc.csv', 'a', newline='') as fileb:
            write = csv.writer(fileb)
            write.writerow("Base Text")
            write.writerows(model_input)
    """
    # return download page
    return render_template('download.html')

if __name__ == "__main__":
    app.run(debug=True)