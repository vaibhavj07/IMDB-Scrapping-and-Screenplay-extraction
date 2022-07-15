from bs4 import BeautifulSoup as Soup
import requests
import imdb
import pandas as pd
url = "https://www.imdb.com/list/ls055592025/"
page = requests.get(url)
response = page.text
soup_data = Soup(response,'html.parser')
movies = soup_data.findAll('div',{'class':'lister-item mode-detail'})
Movie_Name = []
Metascore = []
for i in movies:
    Movie_Name.append(i.find('h3',{'class':'lister-item-header'}).a.text)
    try:
        Metascore.append(i.find('div',{'class':'inline-block ratings-metascore'}).span.text.strip())
    except:
        Metascore.append('NA')

moviesDB = imdb.IMDb()
Year = []
Rating = []
Directors = []
Cast = []
Genre = []
Description = []
Gross = []
Duration = []
Countries = []
Certificates = []
Votes = []
Writers = []
Language = []
Composers = []
Producers = []
Cinematographers = []
Editors = []
Casting_direc = []
Air_date = []
imdbid = []
edit_dept = []
Prod_designers = []
Art_directors = []
Costume_Design = []
Prod_Manager = []
Ass_Direc = []
Sound_dept = []
Camera_dept = []
Music_dept = []
Production_Companies = []


i = 1
for movie in Movie_Name:
    print(str(i) + ")"+"Getting Meta deta: ", movie)
    movies = moviesDB.search_movie(movie)
    if(movies):
        id = movies[0].getID()
        m = moviesDB.get_movie(id)
    try:
        date = m['year']
    except:
        date = 'NA'
    try:
        rating = m['rating']
    except:
        rating = 'NA'
    try:
        directors = m['directors']
        director = ', '.join(map(str,directors))
    except:
        director = 'NA'
    try:
        casting = m['cast']
        actors = ", ".join(map(str, casting[0:5]))
    except:
        actors = 'NA'
    try:
        genre = m['genre']
    except:
        genre = 'NA'
    try:
        duration = m['runtime']
    except:
        duration = 'NA'
    try:
        description = m['plot outline']
    except:
        description = 'NA'
    try:
        gross = m['box office']
    except:
        gross = 'NA'
    try:
        countries = m['countries']
    except:
        countries = 'NA'
    try:
        certificates = m['certificates']
    except:
        certificates = 'NA'
    try:
        votes = m['votes']
    except:
        votes = 'NA'
    try:
        writer = m['writer']
        writers = ", ".join(map(str, writer))
    except:
        writers = 'NA'
    try:
        language = m['language']
    except:
        language = 'NA'
    try:
        composer = m['composers']
        composers = ", ".join(map(str, composer))
    except:
        composers = 'NA'
    try:
        producer = m['producers']
        producers = ", ".join(map(str, producer))
    except:
        producers = 'NA'
    try:
        cinematographer = m['cinematographers']
        cinematographers = ", ".join(map(str, cinematographer))
    except:
        cinematographers = 'NA'
    try:
        editor = m['editors']
        editors = ", ".join(map(str, editor))
    except:
        editors = 'NA'
    try:
        cdirec = m['casting directors']
        cdirect = ", ".join(map(str, cdirec))
    except:
        cdirect = 'NA'
    try:
        airdate = m['original air date']
    except:
        airdate = 'NA'
    try:
        imdb_id = m['imdbID']
    except:
        imdb_id = 'NA'
    try:
        edept = m['editorial department']
        edpts = ", ".join(map(str, edept))
    except:
        edpts = 'NA'
    try:
        p_design = m['production designers']
        p_designs = ", ".join(map(str, p_design))
    except:
        p_designs = 'NA'
    try:
        a_direc = m['art directors']
        a_direcs = ", ".join(map(str, a_direc))
    except:
        a_direcs = 'NA'
    try:
        cdesign = m['costume designers']
        cdesigns = ", ".join(map(str, cdesign))
    except:
        cdesigns = 'NA'
    try:
        pm = m['production managers']
        pms = ", ".join(map(str, pm))
    except:
        pms = 'NA'
    try:
        ad = m['assistant directors']
        ads = ", ".join(map(str, ad))
    except:
        ads = 'NA'
    try:
        sd = m['sound department']
        sds = ", ".join(map(str, sd))
    except:
        sds = 'NA'
    try:
        cd = m['camera department']
        cds = ", ".join(map(str, cd))
    except:
        cds = 'NA'
    try:
        md = m['music department']
        mds = ", ".join(map(str, md))
    except:
        mds = 'NA'
    try:
        pc = m['production companies']
        pcs = ", ".join(map(str, pc))
    except:
        pcs = 'NA'








    Year.append(date)
    Rating.append(rating)
    Directors.append(director)
    Cast.append(actors)
    Genre.append(genre)
    Description.append(description)
    Gross.append(gross)
    Duration.append(duration)
    Countries.append(countries)
    Certificates.append(certificates)
    Votes.append(votes)
    Writers.append(writers)
    Language.append(language)
    Composers.append(composers)
    Producers.append(producers)
    Cinematographers.append(cinematographers)
    Editors.append(editors)
    Casting_direc.append(cdirect)
    Air_date.append(airdate)
    imdbid.append(imdb_id)
    edit_dept.append(edpts)
    Prod_designers.append(p_designs)
    Art_directors.append(a_direcs)
    Costume_Design.append(cdesigns)
    Prod_Manager.append(pms)
    Ass_Direc.append(ads)
    Sound_dept.append(sds)
    Camera_dept.append(cds)
    Music_dept.append(mds)
    Production_Companies.append(pcs)





    i+=1

data = list(zip(Movie_Name,Year,Rating,Metascore,Directors,Cast,Genre,Description,Gross,Duration,Countries,Certificates,Votes,Writers,Language,Composers,Producers,Cinematographers,
                Editors,Casting_direc,Air_date,imdbid,edit_dept,Prod_designers,Art_directors,Costume_Design,Prod_Manager,Ass_Direc,Sound_dept,Camera_dept,Music_dept,
                Production_Companies))
df = pd.DataFrame(data,columns=["Name","Year","Rating","Metascore","Directors","Cast","Genre","Description","Gross","Duration","Countries","Certificates","Votes",
                                "Writers","Language","Composers","Producers","Cinematographer","Editors","Casting Director","Orig_Airdate","IMDBid","Editorial Dept",
                                "Production Designers","Art Directors","Costume Designers","Production Manager","Assistant Director","Sound Department",
                                "Camera Department","Music Department","Production Companies"])
df.to_csv('Metadata.csv')

    
