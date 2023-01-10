import parking
import automobil
import vlasnik
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
    except Error as e:
        print(e)

def insert_parking(conn, parking):
    try:
        sql = ''' INSERT INTO parking(grad,ulica,zona,broj_mjesta)
                  VALUES(?,?,?,?) '''
        cur = conn.cursor()
        params = (parking.grad,parking.ulica,parking.zona,parking.br_mjesta)
        cur.execute(sql, params)
        conn.commit()
    except Error as e:
        print(e)

def insert_automobil(conn, automobil):
    try:
        sql = ''' INSERT INTO automobil(marka,model,broj_sjedista,boja,registarske_oznake)
                  VALUES(?,?,?,?,?) '''
        cur = conn.cursor()
        params = (automobil.marka,automobil.model,automobil.br_sjedista,automobil.boja,automobil.reg_oznake)
        cur.execute(sql, params)
        conn.commit()
    except Error as e:
        print(e)

def insert_vlasnik(conn, vlasnik):
    try:
        sql = ''' INSERT INTO vlasnik(ime,prezime,pol,jmbg)
                  VALUES(?,?,?,?) '''
        cur = conn.cursor()
        params = (vlasnik.ime,vlasnik.prezime,vlasnik.pol,vlasnik.jmbg)
        cur.execute(sql, params)
        conn.commit()
    except Error as e:
        print(e)