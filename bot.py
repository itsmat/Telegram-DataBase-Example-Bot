#Imports
import sqlite3
from pyrogram import Client, filters

#config tg 

api_hash = "123abc"                                                      #my.telegram.org
api_id = 1234                                                            #my.telegram.org
bot_token = "123:abc"                                                    #@botfather
app = Client('bot', api_id=api_id, api_hash=api_hash, bot_token=bot_token)

#config database
try:
    conn = sqlite3.connect("database.db")
    conn.cursor().execute("CREATE TABLE IF NOT EXISTS utenti_main(idutente INTEGER)")
    conn.commit()
except Exception as errore:
    print(f'[DATABASE ERROR] {errore}')

def cercautente(idutente): #searches for data relating to a user / cerca i dati inerenti ad un utente
    return conn.cursor().execute("SELECT * FROM utenti_main WHERE idutente = ?", (idutente,)).fetchall()

def nuovoutente(idutente): 
    if not cercautente(idutente): #check if a user exists in the database / controlla se un utente è presente nel database
        conn.cursor().execute("INSERT INTO utenti_main VALUES (?)", (idutente,)) #if the user is not in the database, he inserts it / se l'utente non è nel database lo inserisce
        conn.commit()

@app.on_message(filters.command("start") & filters.private)
async def cmdstart(client, message):
    nuovoutente(message.from_user.id) 

    await message.reply('github.com/itsmat')

app.run(print('Bot Started | github.com/itsmat'))