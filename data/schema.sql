drop table if exists registroAlunni;
create table registroAlunni (
  numeroReg integer primary key,
  nome      text not null,
  cognome   text not null,
  annoNascita text not null,
);

/*
 Dizionario corrispondente alla schema
registroAlunni = { -1 : {"numeroReg" : '-1', "nome" : 'nome',
                "cognome" : 'cognome', "annoNascita"  : 'annoNascita'}}
*/