class Musica:
    nome = ''
    artista = ''
    duracao = int

musica_cola_comigo = Musica()
musica_cola_comigo.nome = 'Cola Comigo'
musica_cola_comigo.artista = 'Luthuli'
musica_cola_comigo.duracao = 241

musica_coisas_que_eu_sei = Musica()
musica_coisas_que_eu_sei.nome = 'Coisas que eu sei'
musica_coisas_que_eu_sei.artista = 'Danni Carlos'
musica_coisas_que_eu_sei.duracao = 233

musica_deus_e_eu = Musica()
musica_deus_e_eu.nome = 'Deus e eu'
musica_deus_e_eu.artista = 'Victor e Leo'
musica_deus_e_eu.duracao = 245

print(vars(musica_deus_e_eu))