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
        sql = ''' INSERT INTO parking(broj_parkinga,grad,ulica,zona,broj_mjesta)
                  VALUES(?,?,?,?,?) '''
        cur = conn.cursor()
        params = (parking.jed_br_parkinga,parking.grad,parking.ulica,parking.zona,parking.br_mjesta)
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

def delete_parking(conn,br_parkinga):
    try:
        sql='''DELETE FROM parking WHERE broj_parkinga="'''+str(br_parkinga)+'''";'''
        cur=conn.cursor()
        cur.execute(sql)
        conn.commit()
    except Error as e:
        print(e)

def delete_vlasnik(conn,jmbg):
    try:
        sql='''DELETE FROM vlasnik WHERE jmbg="'''+str(jmbg)+'''";'''
        cur=conn.cursor()
        cur.execute(sql)
        conn.commit()
    except Error as e:
        print(e)

def delete_automobil(conn,reg_oznaka):
    try:
        sql='''DELETE FROM automobil WHERE registarske_oznake="'''+str(reg_oznaka)+'''";'''
        cur=conn.cursor()
        cur.execute(sql)
        conn.commit()
    except Error as e:
        print(e)

def select_all_parking(conn):
    sql = ''' SELECT * FROM parking;'''
    cur = conn.cursor()
    cur.execute(sql)
    ans = cur.fetchall()
    return ans
def select_all_vlasnik(conn):
    sql = ''' SELECT * FROM vlasnik;'''
    cur = conn.cursor()
    cur.execute(sql)
    ans = cur.fetchall()
    return ans
def select_all_automobil(conn):
    sql = ''' SELECT * FROM automobil;'''
    cur = conn.cursor()
    cur.execute(sql)
    ans = cur.fetchall()
    return ans
def update_parking(conn,broj_parkinga,broj_mjesta):
    sql='''UPDATE parking SET broj_mjesta="'''+str(broj_mjesta)+'''" WHERE broj_parkinga="'''+str(broj_parkinga)+'''";'''
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
def update_vlasnik(conn,jmbg,ime):
    sql='''UPDATE vlasnik SET ime="'''+ime+'''" WHERE jmbg="'''+str(jmbg)+'''";'''
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
def update_automobil(conn,reg_oznake,boja):
    sql='''UPDATE automobil SET boja="'''+str(boja)+'''" WHERE registarske_oznake="'''+str(reg_oznake)+'''";'''
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()