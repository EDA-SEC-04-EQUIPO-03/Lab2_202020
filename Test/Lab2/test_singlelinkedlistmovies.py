<<<<<<< HEAD
=======
"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
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
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

>>>>>>> origin/RamaGrupo3-j.lora
import pytest 
import config 
from DataStructures import singlelinkedlist as slt


<<<<<<< HEAD
def cmpfunction (element1, element2):
    if element1["movie_id"] == element2["movie_id"]:
        return 0
    elif element1["movie_id"] < element2["movie_id"]:
        return -1
    else:
        return 1

=======

def cmpfunction (element1, element2):
    if element1 == element2:
        return 0
>>>>>>> origin/RamaGrupo3-j.lora

@pytest.fixture
def lst ():
    lst = slt.newList(cmpfunction)
    return lst


@pytest.fixture
<<<<<<< HEAD
def movies ():
    movies = []
    movies.append({'movie_id':'1', 'movie_title':'Title 1'})
    movies.append({'movie_id':'2', 'movie_title':'Title 2'})
    movies.append({'movie_id':'3', 'movie_title':'Title 3'})
    movies.append({'movie_id':'4', 'movie_title':'Title 4'})
    movies.append({'movie_id':'5', 'movie_title':'Title 5'})
    print (movies[0])
    return movies


@pytest.fixture
def lstmovies(movies):
    lst = slt.newList(cmpfunction)
    for i in range(0,5):    
        slt.addLast(lst,movies[i])    
    return lst


=======
def books ():
    books = []
    books.append({'book_id':'1', 'book_title':'Title 1', 'author':'author 1'})
    books.append({'book_id':'2', 'book_title':'Title 2', 'author':'author 2'})
    books.append({'book_id':'3', 'book_title':'Title 3', 'author':'author 3'})
    books.append({'book_id':'4', 'book_title':'Title 4', 'author':'author 4'})
    books.append({'book_id':'5', 'book_title':'Title 5', 'author':'author 5'})
    print (books[0])
    return books


@pytest.fixture
def lstbooks(books):
    lst = slt.newList(cmpfunction)
    for i in range(0,5):    
        slt.addLast(lst,books[i])    
    return lst



>>>>>>> origin/RamaGrupo3-j.lora
def test_empty (lst):
    assert slt.isEmpty(lst) == True
    assert slt.size(lst) == 0


<<<<<<< HEAD
def test_addFirst (lst, movies):
    assert slt.isEmpty(lst) == True
    assert slt.size(lst) == 0
    slt.addFirst (lst, movies[1])
    assert slt.size(lst) == 1
    slt.addFirst (lst, movies[2])
    assert slt.size(lst) == 2
    movie = slt.firstElement(lst)
    assert movie == movies[2]
    

def test_addLast (lst, movies):
    assert slt.isEmpty(lst) == True
    assert slt.size(lst) == 0
    slt.addLast (lst, movies[1])
    assert slt.size(lst) == 1
    slt.addLast (lst, movies[2])
    assert slt.size(lst) == 2
    movie = slt.firstElement(lst)
    assert movie == movies[1]
    movie = slt.lastElement(lst)
    assert movie == movies[2]


def test_getElement(lstmovies, movies):
    book = slt.getElement(lstmovies, 1)
    assert book == movies[0]
    book = slt.getElement(lstmovies, 5)
    assert book == movies[4]


def test_removeFirst (lstmovies, movies):
    assert slt.size(lstmovies) == 5
    slt.removeFirst(lstmovies)
    assert slt.size(lstmovies) == 4
    movie = slt.getElement(lstmovies, 1)
    assert movie  == movies[1]

def test_removeLast (lstmovies, movies):
    assert slt.size(lstmovies) == 5
    slt.removeLast(lstmovies)
    assert slt.size(lstmovies) == 4
    movie = slt.getElement(lstmovies, 4)
    assert movie  == movies[3]



def test_insertElement (lst, movies):
    assert slt.isEmpty(lst) is True
    assert slt.size(lst) == 0
    slt.insertElement (lst, movies[0], 1)
    assert slt.size(lst) == 1
    slt.insertElement (lst, movies[1], 2)
    assert slt.size(lst) == 2
    slt.insertElement (lst, movies[2], 1)
    assert slt.size(lst) == 3
    movie = slt.getElement(lst, 1)
    assert movie == movies[2]
    movie = slt.getElement(lst, 2)
    assert movie == movies[0]



def test_isPresent (lstmovies, movies):
    movie = {'movie_id':'10', 'movie_title':'Title 10'}
    print(slt.isPresent (lstmovies, movies[2]))
    assert slt.isPresent (lstmovies, movies[2]) > 0
    assert slt.isPresent (lstmovies, movie) == 0
    


def test_deleteElement (lstmovies, movies):
    pos = slt.isPresent (lstmovies, movies[2])
    assert pos > 0
    movie = slt.getElement(lstmovies, pos)
    assert movie == movies[2]
    slt.deleteElement (lstmovies, pos)
    assert slt.size(lstmovies) == 4
    movie = slt.getElement(lstmovies, pos)
    assert movie == movies[3]


def test_changeInfo (lstmovies):
    movie10 = {'movie_id':'10', 'movie_title':'Title 10'}
    slt.changeInfo (lstmovies, 1, movie10)
    movie = slt.getElement(lstmovies, 1)
    assert movie10 == movie


def test_exchange (lstmovies, movies):
    movie1 = slt.getElement(lstmovies, 1)
    movie5 = slt.getElement(lstmovies, 5)
    slt.exchange (lstmovies, 1, 5)
    assert slt.getElement(lstmovies, 1) == movie5
    assert slt.getElement(lstmovies, 5) == movie1
=======


def test_addFirst (lst, books):
    assert slt.isEmpty(lst) == True
    assert slt.size(lst) == 0
    slt.addFirst (lst, books[1])
    assert slt.size(lst) == 1
    slt.addFirst (lst, books[2])
    assert slt.size(lst) == 2
    book = slt.firstElement(lst)
    assert book == books[2]




def test_addLast (lst, books):
    assert slt.isEmpty(lst) == True
    assert slt.size(lst) == 0
    slt.addLast (lst, books[1])
    assert slt.size(lst) == 1
    slt.addLast (lst, books[2])
    assert slt.size(lst) == 2
    book = slt.firstElement(lst)
    assert book == books[1]
    book = slt.lastElement(lst)
    assert book == books[2]




def test_getElement(lstbooks, books):
    book = slt.getElement(lstbooks, 1)
    assert book == books[0]
    book = slt.getElement(lstbooks, 5)
    assert book == books[4]





def test_removeFirst (lstbooks, books):
    assert slt.size(lstbooks) == 5
    slt.removeFirst(lstbooks)
    assert slt.size(lstbooks) == 4
    book = slt.getElement(lstbooks, 1)
    assert book  == books[1]



def test_removeLast (lstbooks, books):
    assert slt.size(lstbooks) == 5
    slt.removeLast(lstbooks)
    assert slt.size(lstbooks) == 4
    book = slt.getElement(lstbooks, 4)
    assert book  == books[3]



def test_insertElement (lst, books):
    assert slt.isEmpty(lst) is True
    assert slt.size(lst) == 0
    slt.insertElement (lst, books[0], 1)
    assert slt.size(lst) == 1
    slt.insertElement (lst, books[1], 2)
    assert slt.size(lst) == 2
    slt.insertElement (lst, books[2], 1)
    assert slt.size(lst) == 3
    book = slt.getElement(lst, 1)
    assert book == books[2]
    book = slt.getElement(lst, 2)
    assert book == books[0]



def test_isPresent (lstbooks, books):
    book = {'book_id':'10', 'book_title':'Title 10', 'author':'author 10'}
    assert slt.isPresent (lstbooks, books[2]) > 0
    assert slt.isPresent (lstbooks, book) == 0
    


def test_deleteElement (lstbooks, books):
    pos = slt.isPresent (lstbooks, books[2])
    assert pos > 0
    book = slt.getElement(lstbooks, pos)
    assert book == books[2]
    slt.deleteElement (lstbooks, pos)
    assert slt.size(lstbooks) == 4
    book = slt.getElement(lstbooks, pos)
    assert book == books[3]


def test_changeInfo (lstbooks):
    book10 = {'book_id':'10', 'book_title':'Title 10', 'author':'author 10'}
    slt.changeInfo (lstbooks, 1, book10)
    book = slt.getElement(lstbooks, 1)
    assert book10 == book


def test_exchange (lstbooks, books):
    book1 = slt.getElement(lstbooks, 1)
    book5 = slt.getElement(lstbooks, 5)
    slt.exchange (lstbooks, 1, 5)
    assert slt.getElement(lstbooks, 1) == book5
    assert slt.getElement(lstbooks, 5) == book1
>>>>>>> origin/RamaGrupo3-j.lora
