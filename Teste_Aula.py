print('Diagnosticando o Coronavírus')
print('Digite o número correspondente da informação que você deseja saber mais: ')
print('\n')
print('1. Quais os sintomas do Coronavírus?''\n'
      '2. Como se prevenir do Coronavírus?' '\n'
      '3. Links úteis sobre o Coronavírus?' '\n'
      '4. Simulador de sintomas de Coronavírus' '\n'
      '5. Sair')

numero = int(input('Digite o número correspondente da informação: '))
if numero == 1:
    print('O Coronavírus pode afetar de maneira diferente cada indivíduo. Entretanto alguns '
          'dos sintomas entre pessoas infectadas são:' '\n' '\n'
          'Casos assintomáticos: ' '\n'
          'são caracterizados por teste laboratorial positivo para Covid-19 e ausência de sintomas; ' '\n' '\n'
          'Casos leves: ' '\n'
          'caracterizados a partir da presença de sintomas não específicos, como: ''\n'
          '- Tosse; ''\n'
          '- Dor de garganta ou coriza, seguido, ou não, de perda de olfato e paladar; ''\n'
          '- Diarreia; ''\n'
          '- Dor abdominal; ''\n'
          '- Febre, calafrios, mialgia, fadiga e / ou cefaleia. ' '\n' '\n'
          'Casos moderados: ''\n'
          'os sintomas mais frequentes podem incluir desde sinais leves da doença, como tosse ''\n'
          'persistente e febre persistente diária, até sinais de agravamento dos outros ''\n'
          'sintomas relacionados à covid-19, como: ' '\n'
          '- Fraqueza; ' '\n'
          '- Prostração; ' '\n'
          '- Falta de apetite; ' '\n'
          '- Diarreia.''\n'
          'Além da presença de pneumonia em qualquer estágio.' '\n' '\n'
          'Casos graves: ''\n'
          'Síndrome Respiratória Aguda Grave (Síndrome Gripal), que apresente:  ''\n'
          '- Dificuldade de respirar; ''\n'
          '- Desconforto respiratório ou pressão persistente no tórax; ''\n'
          '- Saturação de oxigênio menor que 95 % em ar ambiente; ''\n'
          '- Coloração azulada de lábios ou rosto.''\n' '\n'
          'OBSERVAÇÃO: Para crianças, os sintomas incluem: ''\n'
          '- Aceleração o ritmo respiratório; ''\n'
          '- Baixa saturação de oxigenação no sangue; ''\n'
          '- Desconforto respiratório; ''\n'
          '- Alteração da consciência; ''\n'
          '- Desidratação; ''\n'
          '- Dificuldade para se alimentar; ''\n'
          '- Coloração azulada; ''\n'
          '- Letargia; ''\n'
          '- Convulsões; ''\n'
          '- Recusa alimentar.' '\n' '\n'
          'Casos críticos: ''\n'
          'Os principais sintomas em casos críticos são: ''\n'
          '- Sepse; ''\n'
          '- Síndrome do desconforto respiratório agudo; ''\n'
          '- Síndrome do desconforto respiratório agudo; ''\n'
          '- Insuficiência respiratória grave; ''\n'
          '- Disfunção de múltiplos órgãos; ''\n'
          '- Pneumonia grave; ''\n'
          '- Necessidade de suporte respiratório e internações em unidades de terapia intensiva.'
          '\n'
          'Todas estas informações foram retiradas do site e aplicativo do governo federal: CORONAVÍRUS SUS.''\n'
          'Para mais informações acesse o link: https://coronavirus-app.saude.gov.br/app/inicio')
elif numero == 2:
    print('\n')
    print('Formas de prevenção do Coronavírus:''\n'
          'Na atual conjuntura em que vivemos, a prevenção é essencial. Para isso é muito ''\n'
          'importante que você siga as orientações da OMS, do Ministério da Saúde e dos governos''\n'
          'estaduais e municipais.''\n''\n'
          'Entre elas: ''\n'
          '- Lavar as mãos sempre que possível;''\n'
          '- Se não tiver água e sabão para fazer a higiene, usar álcool 70% (líquido ou gel); ''\n'
          '- Evitar tocar nos olhos, o nariz, antes de higienizar as mãos;''\n'
          '- Cobrir o nariz e a boca ao espirrar;''\n'
          '- Não compartilhar objetos de uso pessoal, como talheres, pratos, copos ou garrafas;''\n'
          '- Manter os ambientes bem ventilados;''\n'
          '- Evitar contato com pessoas que não estejam no seu convívio muito próximo;''\n'
          '- Se possível, evite sair de casa;''\n'
          '- Se precisar sair, usar sempre máscara e não participar de aglomerações;''\n'
          '- Evitar locais de aglomeração sempre.''\n''\n'
          'Informações retiradas do portal da Fiocruz,' '\n'
          'Para saber mais, acesse: https://portal.fiocruz.br/pergunta/como-se-prevenir-contra-o-coronavirus')
elif numero == 3:
    print('Links úteis para obter mais informações e atualizações sobre o Coronavírus:''\n'
          '- Organização Mundial da Saúde: https://www.who.int/emergencies/diseases/novel-coronavirus-2019/advice-for-public''\n'
          '- Painel governamental brasileiro sobre o Coronavírus: https://covid.saude.gov.br''\n'
          '- Portal da Fiocruz: https://portal.fiocruz.br/Covid19''\n'
          '- Site do ministério da Saúde: https://www.gov.br/saude/pt-br/vacinacao/''\n'
          '- Portal da Agência Nacional de Vigilância Sanitária: https://www.gov.br/anvisa/pt-br')
elif numero == 4:
    print('Simulador de sintomas de Coronavírus')
    print('Gostaríamos de sinalizar que este teste não possuí validade médica alguma e existe''\n'
          'apenas para nível de informação.')
    sintomas = str(input('Você possuí algum dos sintomas do Coronavírus? (Sim/Não): '))
    print('Caso não conheça os sintomas, acesse o o primeiro ítem!')
    print('\n')
    sintomas = sintomas.upper()
    if sintomas == 'SIM':
        print('Os sinais de alerta são:''\n'
              '- Febre por mais de 48 horas''\n'
              '- Falta de ar''\n'
              '- Esforço para respirar''\n'
              '- Pele pálida ou azulada''\n'
              '- Náuseas e Vômitos''\n'
              '- Idade acima de 80 anos''\n'
              '- Criança com muita sonolência ')
        alarme = str(input('Você possui um ou mais dos SINAIS DE ALERTA? (Sim/Não): '))
        alarme = alarme.upper()
        if alarme == 'SIM':
            print('Existe a probabilidade da presença do Coronavírus em seu organismo, ''\n'
                  'o caso deve ser avaliado por uma equipe de saúde especializada para''\n'
                  'informações mais completas.')
        elif alarme == 'NÃO':
            print('Existe a probabilidade da presença do Coronavírus no seu organismo,''\n'
                  'você deve tomar os cuidados necessários e cuidar o aparecimento de novos sintomas.')
        else:
            print('OPÇÃO INVÁLIDA')
    elif sintomas == 'NÃO':
        print('Os sinais de alerta são:''\n'
              '- Febre por mais de 48 horas''\n'
              '- Falta de ar''\n'
              '- Esforço para respirar''\n'
              '- Pele pálida ou azulada''\n'
              '- Náuseas e Vômitos''\n'
              '- Idade acima de 80 anos''\n'
              '- Criança com muita sonolência ')
        alarme = str(input('Você possui um ou mais dos SINAIS DE ALERTA? (Sim/Não): '))
        alarme = alarme.upper()
        if alarme == 'SIM':
            print('Existe a probabilidade da presença do Coronavírus no seu organismo.')
        elif alarme == 'NÃO':
            print('Aparentemente não existe a presença do Coronavírus no seu organismo, ''\n'
                 'ou pode se tratar de um caso assintomático')
        else:
            print('OPÇÃO INVÁLIDA')
    else:
        print('OPÇÃO INVÁLIDA')
elif numero == 5:
    print('Saindo...')
else:
    print('OPÇÃO INVÁLIDA')