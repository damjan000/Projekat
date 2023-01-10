import parking
import automobil
import vlasnik
import baza
import sqlite3

conn=baza.create_connection("database.db")
sql_create_parking_table = """ CREATE TABLE IF NOT EXISTS parking (
                            broj_parkinga INTEGER,
                            grad VARCHAR(20),
                            ulica VARCHAR(30),
                            zona INTEGER,
                            broj_mjesta INTEGER
                            ); """
sql_create_vlasnik_table = """ CREATE TABLE IF NOT EXISTS vlasnik (
                            ime VARCHAR(15),
                            prezime VARCHAR(20),
                            pol CHAR(1),
                            jmbg INTEGER(13)
                            ); """
sql_create_automobil_table = """ CREATE TABLE IF NOT EXISTS automobil (
                            marka VARCHAR(15),
                            model VARCHAR(15),
                            broj_sjedista INTEGER,
                            boja VARCHAR(15),
                            registarske_oznake VARCHAR(7)
                            ); """
if conn is not None:
    baza.create_table(conn,sql_create_parking_table)
    baza.create_table(conn, sql_create_vlasnik_table)
    baza.create_table(conn, sql_create_automobil_table)

    while True:
        izbor=int(input("Za kraj programa unesite 0,\n"
                        "za unos parkinga 1,\n"
                        "za unos vlasnika 2,\n"
                        "za unos automobila 3,\n"
                        "za brisanje parkinga 4,\n"
                        "za brisanje vlasnika 5,\n"
                        "za brisanje automobila 6,\n"
                        "Unesite izbor: "
                        ""))
        if izbor==0:
            break
        elif izbor==1:
            br_parkinga=int(input("Unesite jedinstveni broj parkinga: "))
            grad=input("Unesite grad gdje je parking: ")
            ulica=input("Unesite ulicu parkinga: ")
            zona=int(input("Unesite zonu parkinga: "))
            br_mjesta=int(input("Unesite broj mjesta parkinga: "))
            parking1=parking.Parking(br_parkinga,grad,ulica,zona,br_mjesta)
            print(parking1)
            baza.insert_parking(conn,parking1)
        elif izbor==2:
            ime=input("Unesite ime vlasnika: ")
            prezime=input("Unesite prezime vlasnika: ")
            pol=input("Unesite pol vlasnika (m/z): ")
            jmbg=int(input("Unesite maticni broj: "))
            vlasnik1=vlasnik.Vlasnik(ime,prezime,pol,jmbg)
            print(vlasnik1)
            baza.insert_vlasnik(conn,vlasnik1)
        elif izbor==3:
            marka=input("Unesite marku automobila: ")
            model=input("Unesi model automobila: ")
            br_sjedista=int(input("Unesite broj sjedista: "))
            boja=input("Unesite boja automobila: ")
            reg_oznake=input("Unesite rigistarske oznake automobila: ")
            automobil1=automobil.Automobil(marka,model,br_sjedista,boja,reg_oznake)
            print(automobil1)
            baza.insert_automobil(conn,automobil1)
        elif izbor==4:
            broj_parkinga=int(input("Unesite broj parkinga: "))
            baza.delete_parking(conn,broj_parkinga)
        elif izbor==5:
            jmbg=int(input("Unesite jmbg vlasnika: "))
            baza.delete_vlasnik(conn,jmbg)
        elif izbor==6:
            reg_oznake=input("Unesite registarske oznake: ")
            baza.delete_automobil(conn,reg_oznake)