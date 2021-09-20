"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():

    catalog = {"artists": None,
               "artworks": None}
    catalog["artists"] = lt.newList()
    catalog["artworks"] = lt.newList()

    return catalog

# Funciones para agregar informacion al catalogo
def addArtist(catalog, artist):
    Autores=newArtist(artist["ConstituentID"],artist["DisplayName"],artist["ArtistBio"],artist["Nationality"],artist["Gender"],artist["BeginDate"],artist["EndDate"],artist["Wiki QID"],artist["ULAN"])
    lt.addLast(catalog["artists"], Autores)

def addArtwork(catalog, artwork):
    obras=newArtworks(artwork["ObjectID"],artwork["Title"],artwork["ConstituentID"],artwork["Date"],artwork["Medium"],artwork["Dimensions"],artwork["CreditLine"],artwork["AccessionNumber"],artwork["Classification"],artwork["Department"],artwork["DateAcquired"],artwork["Cataloged"],artwork["URL"],artwork["Circumference (cm)"],artwork["Depth (cm)"],artwork["Diameter (cm)"],artwork["Height (cm)"],artwork["Length (cm)"],artwork["Weight (kg)"],artwork["Width (cm)"],artwork["Seat Height (cm)"],artwork["Duration (sec.)"])  
    lt.addLast(catalog["artworks"], obras)


# Funciones para creacion de datos

def newArtist(ConstituentID,DisplayName,ArtistBio,Nationality,Gender,BeginDate,EndDate,WikiQID,ULAN):
    """
    Crea una nueva estructura para modelar los libros de
    un autor y su promedio de ratings
    """
    artist = {"ConstituentID": None, "DisplayName": "",  "ArtistBio": "", "Nationality": "", "Gender": "","BeginDate": None ,"EndDate": None,"WikiQID" : "" , "ULAN" : ""}
    artist['ConstituentID'] = int(ConstituentID)
    artist['DisplayName'] = DisplayName
    artist['ArtistBio'] = ArtistBio
    artist['Nationality'] = Nationality
    artist['Gender'] = Gender
    artist['BeginDate'] = int(BeginDate)
    artist['EndDate'] = int(EndDate)
    artist['WikiQID'] = WikiQID
    artist['ULAN'] = ULAN
    return artist 
#hacer esto mismo con artworks, pero con las columnas de artworks: ObjectID,Title,ConstituentID,Date,Medium,Dimensions,CreditLine,AccessionNumber,Classification,Department,DateAcquired,Cataloged,URL,Circumference (cm),Depth (cm),Diameter (cm),Height (cm),Length (cm),Weight (kg),Width (cm),Seat Height (cm),Duration (sec.)

def newArtworks(ObjectID,Title,ConstituentID,Date,Medium,Dimensions,CreditLine,AccessionNumber,Classification,Department,DateAcquired,Cataloged,URL,Circumference,Depth,Diameter,Height,Length,Weight,Width,SeatHeight,Duration):
    """
    Esta estructura almancena los tags utilizados para marcar libros.
    """
    artist = {"ObjectID": None, "Title": "",  "ConstituentID": "", "Date": "", "Medium": "","Dimensions": "" ,"CreditLine": "","AccessionNumber" : "" , "Classification" : "", "Department": "","DateAcquired":"","Cataloged":"","URL":"","Circumference":"","Depth":"","Diameter":"","Height":"","Length":"","Weight":"","Width":"","SeatHeight":"","Duration":"", }
    artist['ObjectID'] = int(ObjectID)
    artist['Title'] = Title
    artist['ConstituentID'] = ConstituentID
    artist['Date'] = Date
    artist['Medium'] = Medium
    artist['Dimensions'] = Dimensions
    artist['CreditLine'] = CreditLine
    artist['AccessionNumber'] = AccessionNumber
    artist['Classification'] = Classification
    artist['Department'] = Department
    artist['DateAcquired'] = DateAcquired
    artist['Cataloged'] = Cataloged
    artist['URL'] = URL
    artist['Circumference(cm)'] = Circumference
    artist['Depth'] = Depth
    artist['Diameter'] = Diameter
    artist['Height'] = Height
    artist['CLength'] = Length
    artist['Weight'] = Weight
    artist['Width'] = Width
    artist['SeatHeight'] = SeatHeight
    artist['Duration'] = Duration
    return artist 

"""def newBookTag(tag_id, ArtWorks_id):

    booktag = {'tag_id': tag_id, ' ArtWorks_id':  ArtWorks_id}
    return booktag
"""
# Funciones de consulta


# Funciones utilizadas para comparar elementos dentro de una lista

def cmpArtworkByDateAcquired(artwork1, artwork2):
    valores_artwork1 = artwork1["DateAquired"].split('-')
    valores_artwork2 = artwork2["DateAquired"].split('-')
    dias_1 = 0
    dias_2 = 0
    dias_1 += int(valores_artwork1[0]) * 360
    dias_1 += int(valores_artwork1[1]) * 30
    dias_1 += int(valores_artwork1[2])
    dias_2 += int(valores_artwork2[0]) * 360
    dias_2 += int(valores_artwork2[1]) * 30
    dias_2 += int(valores_artwork2[2])
    return dias_1 < dias_2

# Funciones de ordenamiento

def sortBooks(catalog, size):
    # TODO completar modificaciones para el laboratorio 4
    sub_list = lt.subList(catalog['books'], 1, size)
    sub_list = sub_list.copy()
    start_time = time.process_time()
    sorted_list=sa.sort(sub_list, compareratings)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list