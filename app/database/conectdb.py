"""Esse modulo faz a conexão com o Banco de Dados"""
import os

import dotenv
import psycopg2

dotenv.load_dotenv(dotenv.find_dotenv())


def conectar():
    """Função que faz a conexão com o Banco de Dados"""
    con = psycopg2.connect(
        host=os.getenv("HOST"),
        database=os.getenv("DATABASE"),
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
    )

    return con


def cursor(query):
    """Função que cria o cursor"""
    vcon = conectar()
    c = vcon.cursor()
    c.execute(query)
    vcon.commit()
    vcon.close()
    return cursor


def cursormany(query, data):
    """Função que cria o cursor"""
    vcon = conectar()
    c = vcon.cursor()
    c.executemany(query, data)
    vcon.commit()
    vcon.close()
    return cursormany


def selectdata(query):
    """Função que faz o select"""
    vcon = conectar()
    c = vcon.cursor()
    c.execute(query)
    rows = c.fetchall()
    vcon.commit()
    vcon.close()
    return rows


def deletar(query):
    """Função que faz o delete"""
    vcon = conectar()
    c = vcon.cursor()
    c.execute(query)
    vcon.commit()
    vcon.close()
    return deletar
