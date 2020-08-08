from flask import Flask, render_template 
import pandas as pd
import requests
from bs4 import BeautifulSoup 
from io import BytesIO
import base64
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')


app = Flask(__name__) #don't change this code

def scrap(url):
    #This is fuction for scrapping
    url_get = requests.get('https://www.imdb.com/search/title/?release_date=2019-01-01,2019-12-31')
    soup = BeautifulSoup(url_get.content,"html.parser")
    
    #Find the key to get the information
    table = soup.find_all('div', attrs={'class':'lister-item-content'}) 

    temp = [] #initiating a tuple

    for a in table:
        judul = a.find('a').text
        rating = a.find('div', attrs={'class':'inline-block ratings-imdb-rating'}).text.strip() 
        votes = a.find('span', attrs={'name':'nv'}).text.strip()
        metascore = a.find('span',attrs={'class':'metascore favorable'})
        if metascore != None:
            metascore = metascore.text.strip()

        temp.append((judul,rating,metascore,votes))
    temp
        #use the key to take information here
        #name_of_object = row.find_all(...)[0].text

    df = pd.DataFrame(temp, columns = ('judul','rating','metascore','votes')) #creating the dataframe
   #data wranggling -  try to change the data type to right data type

    df['rating'] = df['rating'].astype('float64')
    df['metascore'] = pd.to_numeric(df['metascore'], errors='coerce')
    df['votes'] = df['votes'].str.replace(',','').str.replace(',','.').astype(float)

    df = df.sort_values(by='rating',ascending=False).reset_index().drop(columns='index')

   #end of data wranggling

    return df

@app.route("/")
def index():
    df = scrap('https://www.imdb.com/search/title/?release_date=2019-01-01,2019-12-31') #insert url here

    print(df)
    #This part for rendering matplotlib
    fig = plt.figure(figsize=(3,2),dpi=300)
    df[['judul','rating']].set_index('judul').head(7).sort_values(by='rating',ascending=True).plot(kind='barh',title='Top 7 Movies by Rating')
    plt.tight_layout()
    #Do not change this part
    plt.savefig('plot1',bbox_inches="tight") 
    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue())
    result = str(figdata_png)[2:-1]
    #This part for rendering matplotlib

    #this is for rendering the table
    df = df.to_html(classes=["table table-bordered table-striped table-dark table-condensed"])

    return render_template("index.html", table=df, result=result)


if __name__ == "__main__": 
    app.run()
