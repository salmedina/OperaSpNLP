import googlemaps


continents = ['américa', 'america', 'europa', 'áfrica', 'africa', 'asia', 'oceanía', 'oceania']
countries = ['afganistán', 'albania', 'alemania', 'andorra', 'angola', 'antigua y barbuda', 'arabia saudita', 'argelia', 'argentina', 'armenia', 'australia', 'austria', 'azerbaiyán', 'bahamas', 'bangladés', 'barbados', 'baréin', 'bélgica', 'belice', 'benín', 'bielorrusia', 'birmania', 'bolivia', 'bosnia y herzegovina', 'botsuana', 'brasil', 'brunéi', 'bulgaria', 'burkina faso', 'burundi', 'bután', 'cabo verde', 'camboya', 'camerún', 'canadá', 'catar', 'chad', 'chile', 'china', 'chipre', 'ciudad del vaticano', 'colombia', 'comoras', 'corea del norte', 'corea del sur', 'costa de marfil', 'costa rica', 'croacia', 'cuba', 'dinamarca', 'dominica', 'ecuador', 'egipto', 'el salvador', 'emiratos árabes unidos', 'eritrea', 'eslovaquia', 'eslovenia', 'españa', 'estados unidos', 'estonia', 'etiopía', 'filipinas', 'finlandia', 'fiyi', 'francia', 'gabón', 'gambia', 'georgia', 'ghana', 'granada', 'grecia', 'guatemala', 'guyana', 'guinea', 'guinea-bisáu', 'guinea ecuatorial', 'haití', 'honduras', 'hungría', 'india', 'indonesia', 'irak', 'irán', 'irlanda', 'islandia', 'islas marshall', 'islas salomón', 'israel', 'italia', 'jamaica', 'japón', 'jordania', 'kazajistán', 'kenia', 'kirguistán', 'kiribati', 'kuwait', 'laos', 'lesoto', 'letonia', 'líbano', 'liberia', 'libia', 'liechtenstein', 'lituania', 'luxemburgo', 'macedonia del norte', 'madagascar', 'malasia', 'malaui', 'maldivas', 'malí', 'malta', 'marruecos', 'mauricio', 'mauritania', 'méxico', 'micronesia', 'moldavia', 'mónaco', 'mongolia', 'montenegro', 'mozambique', 'namibia', 'nauru', 'nepal', 'nicaragua', 'níger', 'nigeria', 'noruega', 'nueva zelanda', 'omán', 'países bajos', 'pakistán', 'palaos', 'panamá', 'papúa nueva guinea', 'paraguay', 'perú', 'polonia', 'portugal', 'reino unido de gran bretaña e irlanda del norte', 'república centroafricana', 'república checa', 'república del congo', 'república democrática del congo', 'república dominicana', 'república sudafricana', 'ruanda', 'rumanía', 'rusia', 'samoa', 'san cristóbal y nieves', 'san marino', 'san vicente y las granadinas', 'santa lucía', 'santo tomé y príncipe', 'senegal', 'serbia', 'seychelles', 'sierra leona', 'singapur', 'siria', 'somalia', 'sri lanka', 'suazilandia', 'sudán', 'sudán del sur', 'suecia', 'suiza', 'surinam', 'tailandia', 'tanzania', 'tayikistán', 'timor oriental', 'togo', 'tonga', 'trinidad y tobago', 'túnez', 'turkmenistán', 'turquía', 'tuvalu', 'ucrania', 'uganda', 'uruguay', 'uzbekistán', 'vanuatu', 'venezuela', 'vietnam', 'yemen', 'yibuti', 'zambia', 'zimbabue']
cities = ['kabul', 'tirana', 'berlín', 'andorra la vieja', 'saint john’s', 'riad', 'argel', 'buenos aires', 'ereván', 'camberra', 'viena', 'bakú', 'nasáu', 'daca', 'bridgetown', 'manama', 'bruselas', 'belmopán', 'porto novo y cotonú', 'minsk', 'naipyidó', 'sucre', 'sarajevo', 'gaborone', 'brasilia', 'bandar seri begawan', 'sofía', 'uagadugú', 'gitega', 'timbu', 'praia', 'nom pen', 'yaundé', 'ottawa', 'doha', 'yamena', 'santiago de chile', 'pekín', 'nicosia', 'ciudad del vaticano', 'bogotá', 'moroni', 'pionyang', 'eúl', 'yamusukro', 'san josé', 'zagreb', 'la habana', 'copenhague', 'roseau', 'quito', 'el cairo', 'san salvador', 'abu dabi', 'asmara', 'bratislava', 'liubliana', 'madrid', 'washington d.c.', 'tallin', 'adís abeba', 'manila', 'helsinki', 'suva', 'parís', 'libreville', 'banjul', 'tiflis', 'acra', 'saint george', 'atenas', 'ciudad de guatemala', 'georgetown', 'conakri', 'bisáu', 'malabo', 'puerto príncipe', 'tegucigalpa', 'budapest', 'nueva delhi', 'yakarta', 'bagdad', 'teherán', 'dublín', 'reikiavik', 'majuro', 'honiara', 'jerusalén', 'roma', 'kingston', 'tokio', 'amán', 'astaná', 'nairobi', 'biskek', 'tarawa', 'kuwait', 'vientián', 'maseru', 'riga', 'beirut', 'monrovia', 'trípoli', 'vaduz', 'vilna', 'luxemburgo', 'skopie', 'antananarivo', 'kuala lumpur', 'lilongüe', 'malé', 'bamako', 'la valeta', 'rabat', 'port-louis', 'nuakchot', 'ciudad de méxico', 'palikir', 'chisináu', 'mónaco', 'ulán bator', 'podgorica', 'maputo', 'windhoek', 'yaren', 'katmandú', 'managua', 'niamey', 'abuya', 'oslo', 'wellington', 'mascate', 'ámsterdam', 'islamabad', 'melekeok', 'panamá', 'port moresby', 'asunción', 'lima', 'varsovia', 'lisboa', 'londres', 'bangui', 'praga', 'brazzaville', 'kinsasa', 'santo domingo', 'bloemfontein', 'ciudad del cabo y pretoria', 'kigali', 'bucarest', 'moscú', 'apia', 'basseterre', 'san marino', 'kingstown', 'castries', 'santo tomé', 'dakar', 'belgrado', 'victoria', 'freetown', 'singapur', 'damasco', 'mogadiscio', 'sri jayewardenepura', 'colombo', 'babane y lobamba', 'jartum', 'yuba', 'estocolmo', 'berna', 'paramaribo', 'bangkok', 'dodoma', 'dusambé', 'dili', 'lomé', 'nukualofa', 'puerto españa', 'túnez', 'asjabad', 'ankara', 'fongafale', 'kiev', 'kampala', 'montevideo', 'taskent', 'port vila', 'caracas', 'hanói', 'saná', 'yibuti', 'lusaka', 'harare']

def main():

    api_key = open('key.txt', 'r').read().strip()
    gmaps = googlemaps.Client(key=api_key)
    loc_path = 'locations.lst'

    parsed_locations = [l.strip() for l in open(loc_path, 'r').readlines()]
    print(f'There is a total of {len(parsed_locations)} locations.')

    city_country_count = 0
    coords_data = []
    for location in parsed_locations:
        print(f'Processing {location}')
        if location.lower() in continents or location.lower() in countries or location.lower() in cities:
            city_country_count += 1
            continue
        res = gmaps.geocode(location)
        if len(res) > 0:
            coords_data.append((location.replace('\t', ' '), res[0]['geometry']['location']['lat'], res[0]['geometry']['location']['lng']))

    print(f'There were {city_country_count} cities or countries mentioned')
    print(f'Only {len(coords_data)} had a geocode result')
    with open('geocode_data.csv', 'w') as fout:
        fout.write('\n'.join([f'{loc}\t{lat}\t{lng}' for loc, lat, lng in coords_data]))


if __name__ == '__main__':

    main()
