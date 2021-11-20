from datetime import date
import random
import pandas


# erro personalizado
class Error(Exception):
	pass


class DataInsertError(Error):
	def __init__(self, message):
		self.message = message


# Pity System: sistema de pena para garantir personagens exclusivos
class Pity:
	def __init__(self, pity4, banner4, pity5, banner5):
		self.pity4 = pity4
		self.banner4 = banner4
		self.pity5 = pity5
		self.banner5 = banner5

	def pity_reset(self):
		self.pity4 = 0
		self.banner4 = True
		self.pity5 = 0
		self.banner5 = True


# gacha
def gacha(date_entry, all_banners, base_banner, pity):

	# variável de validação: caso seja encontrado um banner
	banner = None
	is_banner = False

	date_year = int(date_entry[0:4])
	date_month = int(date_entry[5:7])
	date_day = int(date_entry[8:10])
	date_run = date(date_year, date_month, date_day)

	# validação: em qual banner se encontra a data
	for n in range(0, len(all_banners)):
		y = all_banners[n]
		y_i = y[0]
		y_f = y[1]
		if y_i <= date_run <= y_f:
			banner = y[2]
			is_banner = True

	# resultado do banner
	if is_banner:
		r = random.random() * 100
		if r < 0.6 or pity.pity5 >= 89:
			pity.pity4 += 1
			if pity.banner5:
				rr = random.random() * 100
				if rr <= 50:
					pity.pity5 = 0
					pity.banner5 = False
					return [banner, random.choice(banner['list_5'])]
				else:
					pity.pity5 = 0
					return [banner, banner['rate_up_5']]
			else:
				pity.pity5 = 0
				pity.banner5 = True
				return [banner, banner['rate_up_5']]
		elif 0.6 <= r < 5.7 or pity.pity4 >= 9:
			pity.pity5 += 1
			if pity.banner4:
				rr = random.random() * 100
				if rr <= 50:
					pity.pity4 = 0
					pity.banner4 = False
					return [banner, random.choice(banner['list_4w'])]
				else:
					rrr = random.random() * 100
					if rrr <= 50:
						pity.pity4 = 0
						pity.banner4 = False
						return [banner, random.choice(banner['list_4c'])]
					else:
						pity.pity4 = 0
						return [banner, random.choice(banner['rate_up_4'])]
			else:
				pity.pity4 = 0
				pity.banner4 = True
				return [banner, random.choice(banner['rate_up_4'])]
		else:
			pity.pity4 += 1
			pity.pity5 += 1
			return [banner, random.choice(banner['list_3'])]
	# wanderlust invocation, caso data não faça parte de nenhum banner
	else:
		r = random.random() * 100
		if r < 0.6 or pity.pity5 >= 89:
			pity.pity4 += 1
			pity.pity5 = 0
			return [banner, random.choice(base_banner['list_5'])]
		elif 0.6 <= r < 5.7 or pity.pity4 >= 9:
			pity.pity4 = 0
			pity.pity5 += 1
			r_wi = random.random()
			if r_wi <= 50:
				return [banner, random.choice(base_banner['list_4w'])]
			else:
				return [banner, random.choice(base_banner['list_4c'])]
		else:
			pity.pity4 += 1
			pity.pity5 += 1
			return [banner, random.choice(base_banner['list_3'])]


# Personagens
# Personagens 4 estrelas
amber = {'type': 'char', 'name': 'Amber', 'rar': 4, 'elem': 'Pyro', 'wp': 'Bow', 'sex': 'F'}
barbara = {'type': 'char', 'name': 'Barbara', 'rar': 4, 'elem': 'Hydro', 'wp': 'Catalyst', 'sex': 'F'}
beidou = {'type': 'char', 'name': 'Beidou', 'rar': 4, 'elem': 'Electro', 'wp': 'Claymore', 'sex': 'F'}
bennett = {'type': 'char', 'name': 'Bennett', 'rar': 4, 'elem': 'Pyro', 'wp': 'Sword', 'sex': 'M'}
chongyun = {'type': 'char', 'name': 'Chongyun', 'rar': 4, 'elem': 'Cryo', 'wp': 'Claymore', 'sex': 'M'}
diona = {'type': 'char', 'name': 'Diona', 'rar': 4, 'elem': 'Cryo', 'wp': 'Bow', 'sex': 'F'}
fischl = {'type': 'char', 'name': 'Fischl', 'rar': 4, 'elem': 'Electro', 'wp': 'Bow', 'sex': 'F'}
kaeya = {'type': 'char', 'name': 'Kaeya', 'rar': 4, 'elem': 'Cryo', 'wp': 'Sword', 'sex': 'M'}
kujou_sara = {'type': 'char', 'name': 'Kujou Sara', 'rar': 4, 'elem': 'Electro', 'wp': 'Bow', 'sex': 'F'}
lisa = {'type': 'char', 'name': 'Lisa', 'rar': 4, 'elem': 'Electro', 'wp': 'Catalyst', 'sex': 'F'}
ningguang = {'type': 'char', 'name': 'Ningguang', 'rar': 4, 'elem': 'Geo', 'wp': 'Catalyst', 'sex': 'F'}
noelle = {'type': 'char', 'name': 'Noelle', 'rar': 4, 'elem': 'Geo', 'wp': 'Claymore', 'sex': 'F'}
razor = {'type': 'char', 'name': 'Razor', 'rar': 4, 'elem': 'Electro', 'wp': 'Claymore', 'sex': 'M'}
rosaria = {'type': 'char', 'name': 'Rosaria', 'rar': 4, 'elem': 'Cryo', 'wp': 'Polearm', 'sex': 'F'}
sayu = {'type': 'char', 'name': 'Sayu', 'rar': 4, 'elem': 'Anemo', 'wp': 'Claymore', 'sex': 'F'}
sucrose = {'type': 'char', 'name': 'Sucrose', 'rar': 4, 'elem': 'Anemo', 'wp': 'Catalyst', 'sex': 'F'}
thoma = {'type': 'char', 'name': 'Thoma', 'rar': 4, 'elem': 'Pyro', 'wp': 'Polearm', 'sex': 'M'}
xiangling = {'type': 'char', 'name': 'Xiangling', 'rar': 4, 'elem': 'Pyro', 'wp': 'Polearm', 'sex': 'F'}
xingqiu = {'type': 'char', 'name': 'Xingqiu', 'rar': 4, 'elem': 'Hydro', 'wp': 'Sword', 'sex': 'M'}
xinyan = {'type': 'char', 'name': 'Xinyan', 'rar': 4, 'elem': 'Pyro', 'wp': 'Claymore', 'sex': 'F'}
yanfei = {'type': 'char', 'name': 'Yanfei', 'rar': 4, 'elem': 'Pyro', 'wp': 'Catalyst', 'sex': 'F'}

# Personagens 5 estrelas comuns
diluc = {'type': 'char', 'name': 'Diluc', 'rar': 5, 'elem': 'Pyro', 'wp': 'Claymore', 'sex': 'M'}
jean = {'type': 'char', 'name': 'Jean', 'rar': 5, 'elem': 'Anemo', 'wp': 'Sword', 'sex': 'F'}
keqing = {'type': 'char', 'name': 'Keqing', 'rar': 5, 'elem': 'Electro', 'wp': 'Sword', 'sex': 'F'}
mona = {'type': 'char', 'name': 'Mona', 'rar': 5, 'elem': 'Hydro', 'wp': 'Catalyst', 'sex': 'F'}
qiqi = {'type': 'char', 'name': 'Qiqi', 'rar': 5, 'elem': 'Cryo', 'wp': 'Sword', 'sex': 'F'}

# Personagens 5 estrelas especiais
albedo = {'type': 'char', 'name': 'Albedo', 'rar': 5, 'elem': 'Geo', 'wp': 'Sword', 'sex': 'M'}
eula = {'type': 'char', 'name': 'Eula', 'rar': 5, 'elem': 'Cryo', 'wp': 'Claymore', 'sex': 'F'}
ganyu = {'type': 'char', 'name': 'Ganyu', 'rar': 5, 'elem': 'Cryo', 'wp': 'Bow', 'sex': 'F'}
hu_tao = {'type': 'char', 'name': 'Hu Tao', 'rar': 5, 'elem': 'Pyro', 'wp': 'Polearm', 'sex': 'F'}
kazuha = {'type': 'char', 'name': 'Kaedehara Kazuha', 'rar': 5, 'elem': 'Anemo', 'wp': 'Sword', 'sex': 'M'}
ayaka = {'type': 'char', 'name': 'Kamisato Ayaka', 'rar': 5, 'elem': 'Cryo', 'wp': 'Sword', 'sex': 'F'}
klee = {'type': 'char', 'name': 'Klee', 'rar': 5, 'elem': 'Pyro', 'wp': 'Catalyst', 'sex': 'F'}
shogun = {'type': 'char', 'name': 'Raiden Shogun', 'rar': 5, 'elem': 'Electro', 'wp': 'Polearm', 'sex': 'F'}
kokomi = {'type': 'char', 'name': 'Sangonomiya Kokomi', 'rar': 5, 'elem': 'Hydro', 'wp': 'Catalyst', 'sex': 'F'}
childe = {'type': 'char', 'name': 'Tartaglia', 'rar': 5, 'elem': 'Hydro', 'wp': 'Bow', 'sex': 'M'}
venti = {'type': 'char', 'name': 'Venti', 'rar': 5, 'elem': 'Anemo', 'wp': 'Bow', 'sex': 'M'}
xiao = {'type': 'char', 'name': 'Xiao', 'rar': 5, 'elem': 'Anemo', 'wp': 'Polearm', 'sex': 'M'}
yoimiya = {'type': 'char', 'name': 'Yoimiya', 'rar': 5, 'elem': 'Pyro', 'wp': 'Bow', 'sex': 'F'}
zhongli = {'type': 'char', 'name': 'Zhongli', 'rar': 5, 'elem': 'Geo', 'wp': 'Polearm', 'sex': 'M'}

# Armas 3 estrelas
w301 = {'type': 'weapon', 'name': 'Slingshot', 'rar': 3, 'wp_type': 'Bow'}
w302 = {'type': 'weapon', 'name': 'Sharpshooter\'s Oath', 'rar': 3, 'wp_type': 'Bow'}
w303 = {'type': 'weapon', 'name': 'Raven Bow', 'rar': 3, 'wp_type': 'Bow'}
w304 = {'type': 'weapon', 'name': 'Emerald Orb', 'rar': 3, 'wp_type': 'Catalyst'}
w305 = {'type': 'weapon', 'name': 'Thrilling Tales of Dragon Slayers', 'rar': 3, 'wp_type': 'Catalyst'}
w306 = {'type': 'weapon', 'name': 'Magic Guide', 'rar': 3, 'wp_type': 'Catalyst'}
w307 = {'type': 'weapon', 'name': 'Debate Club', 'rar': 3, 'wp_type': 'Claymore'}
w308 = {'type': 'weapon', 'name': 'Bloodtainted Greatsword', 'rar': 3, 'wp_type': 'Claymore'}
w309 = {'type': 'weapon', 'name': 'Ferrous Shadow', 'rar': 3, 'wp_type': 'Claymore'}
w310 = {'type': 'weapon', 'name': 'Black Tassel', 'rar': 3, 'wp_type': 'Polearm'}
w311 = {'type': 'weapon', 'name': 'Skyrider Sword', 'rar': 3, 'wp_type': 'Sword'}
w312 = {'type': 'weapon', 'name': 'Harbinger of Dawn', 'rar': 3, 'wp_type': 'Sword'}
w313 = {'type': 'weapon', 'name': 'Cool Steel', 'rar': 3, 'wp_type': 'Sword'}

# Armas 4 estrelas
w401 = {'type': 'weapon', 'name': 'Favonius Warbow', 'rar': 4, 'wp_type': 'Bow'}
w402 = {'type': 'weapon', 'name': 'Sacrificial Bow', 'rar': 4, 'wp_type': 'Bow'}
w403 = {'type': 'weapon', 'name': 'The Stringless', 'rar': 4, 'wp_type': 'Bow'}
w404 = {'type': 'weapon', 'name': 'Rust', 'rar': 4, 'wp_type': 'Bow'}
w405 = {'type': 'weapon', 'name': 'Favonius Codex', 'rar': 4, 'wp_type': 'Catalyst'}
w406 = {'type': 'weapon', 'name': 'Sacrificial Fragments', 'rar': 4, 'wp_type': 'Catalyst'}
w407 = {'type': 'weapon', 'name': 'The Widsith', 'rar': 4, 'wp_type': 'Catalyst'}
w408 = {'type': 'weapon', 'name': 'Eye of Perception', 'rar': 4, 'wp_type': 'Catalyst'}
w409 = {'type': 'weapon', 'name': 'Favonius Greatsword', 'rar': 4, 'wp_type': 'Claymore'}
w410 = {'type': 'weapon', 'name': 'Sacrificial Greatsword', 'rar': 4, 'wp_type': 'Claymore'}
w411 = {'type': 'weapon', 'name': 'The Bell', 'rar': 4, 'wp_type': 'Claymore'}
w412 = {'type': 'weapon', 'name': 'Rainslasher', 'rar': 4, 'wp_type': 'Claymore'}
w413 = {'type': 'weapon', 'name': 'Favonius Lance', 'rar': 4, 'wp_type': 'Polearm'}
w414 = {'type': 'weapon', 'name': 'Dragon\'s Bane', 'rar': 4, 'wp_type': 'Polearm'}
w415 = {'type': 'weapon', 'name': 'Favonius Sword', 'rar': 4, 'wp_type': 'Sword'}
w416 = {'type': 'weapon', 'name': 'Sacrificial Sword', 'rar': 4, 'wp_type': 'Sword'}
w417 = {'type': 'weapon', 'name': 'The Flute', 'rar': 4, 'wp_type': 'Sword'}
w418 = {'type': 'weapon', 'name': 'Lion\'s Roar', 'rar': 4, 'wp_type': 'Sword'}

# wi = Wanderlust Invocation; banner base para o de eventos
# wi itens 3 estrelas
wi_3 = [w301, w302, w303, w304, w305, w306, w307, w308, w309, w310, w311, w312, w313]

# wi itens 4 estrelas
wi_4w = [  # armas
	w401, w402, w403, w404, w405, w406, w407, w408, w409, w410, w411, w412, w413, w414, w415, w416, w417, w418
]
wi_4c = [  # personagens
	amber, barbara, beidou, bennett, chongyun, fischl, kaeya,
	lisa, ningguang, noelle, razor, sucrose, xiangling, xingqiu
]

# wi 5 estrelas
wi_5 = [diluc, jean, keqing, mona, qiqi]

# Banner base: Wanderlust invocation
wi = {
	'name': 'Wanderlust Invocation',
	'list_3': wi_3,
	'list_4w': wi_4w,
	'list_4c': wi_4c,
	'list_5': wi_5,
}

# Banners especiais
ballad = {
	'name': 'Ballad in Goblets',
	'list_3': wi_3,
	'list_4w': wi_4w,
	'list_4c': wi_4c,
	'list_5': wi_5,
	'rate_up_4': [barbara, fischl, xiangling],
	'rate_up_5': venti
}

spark = {
	'name': 'Sparkling Steps',
	'list_3': wi_3,
	'list_4w': wi_4w,
	'list_4c': wi_4c,
	'list_5': wi_5,
	'rate_up_4': [noelle, sucrose, xingqiu],
	'rate_up_5': klee
}

snezhnaya = {
	'name': 'Farewell of Snezhnaya',
	'list_3': wi_3,
	'list_4w': wi_4w,
	'list_4c': wi_4c,
	'list_5': wi_5,
	'rate_up_4': [beidou, diona, ningguang],
	'rate_up_5': childe
}

gentry = {
	'name': 'Gentry of Hermitage',
	'list_3': wi_3,
	'list_4w': wi_4w,
	'list_4c': wi_4c,
	'list_5': wi_5,
	'rate_up_4': [chongyun, razor, xinyan],
	'rate_up_5': zhongli
}

secretum = {
	'name': 'Secretum Secretorum',
	'list_3': wi_3,
	'list_4w': wi_4w,
	'list_4c': wi_4c + [xinyan, diona],
	'list_5': wi_5,
	'rate_up_4': [bennett, fischl, sucrose],
	'rate_up_5': albedo
}

harbor = {
	'name': 'Adrift in the Harbor',
	'list_3': wi_3,
	'list_4w': wi_4w,
	'list_4c': wi_4c + [diona, xinyan],
	'list_5': wi_5,
	'rate_up_4': [noelle, xiangling, xingqiu],
	'rate_up_5': ganyu
}

invitation = {
	'name': 'Invitation to Mundane Life',
	'list_3': wi_3,
	'list_4w': wi_4w,
	'list_4c': wi_4c + [diona, xinyan],
	'list_5': wi_5,
	'rate_up_4': [beidou, diona, xinyan],
	'rate_up_5': xiao
}

lanterns = {
	'name': 'Dance of Lanterns',
	'list_3': wi_3,
	'list_4w': wi_4w,
	'list_4c': wi_4c + [diona, xinyan],
	'list_5': wi_5,
	'rate_up_4': [barbara, bennett, ningguang],
	'rate_up_5': keqing
}

bloom = {
	'name': 'Moment of Bloom',
	'list_3': wi_3,
	'list_4w': wi_4w,
	'list_4c': wi_4c + [diona, xinyan],
	'list_5': wi_5,
	'rate_up_4': [chongyun, xiangling, xingqiu],
	'rate_up_5': hu_tao
}

ballad2 = {
	'name': 'Ballad in Goblets',
	'list_3': wi_3,
	'list_4w': wi_4w,
	'list_4c': wi_4c + [diona, xinyan],
	'list_5': wi_5,
	'rate_up_4': [noelle, razor, sucrose],
	'rate_up_5': venti
}

snezhnaya2 = {
	'name': 'Farewell to Snezhnaya',
	'list_3': wi_3,
	'list_4w': wi_4w,
	'list_4c': wi_4c + [diona, xinyan],
	'list_5': wi_5,
	'rate_up_4': [barbara, fischl, rosaria],
	'rate_up_5': childe
}

gentry2 = {
	'name': 'Gentry of Hermitage',
	'list_3': wi_3,
	'list_4w': wi_4w,
	'list_4c': wi_4c + [diona, rosaria, xinyan],
	'list_5': wi_5,
	'rate_up_4': [diona, noelle, yanfei],
	'rate_up_5': zhongli
}

ocean = {
	'name': 'Born of Ocean Swell',
	'list_3': wi_3,
	'list_4w': wi_4w,
	'list_4c': wi_4c + [diona, rosaria, xinyan],
	'list_5': wi_5,
	'rate_up_4': [beidou, xingqiu, xinyan],
	'rate_up_5': eula
}

spark2 = {
	'name': 'Sparkling Steps',
	'list_3': wi_3,
	'list_4w': wi_4w,
	'list_4c': wi_4c + [diona, rosaria, xinyan, yanfei],
	'list_5': wi_5,
	'rate_up_4': [barbara, fischl, sucrose],
	'rate_up_5': klee
}

leaves = {
	'name': 'Leaves in the Wind',
	'list_3': wi_3,
	'list_4w': wi_4w,
	'list_4c': wi_4c + [diona, rosaria, xinyan, yanfei],
	'list_5': wi_5,
	'rate_up_4': [bennett, razor, rosaria],
	'rate_up_5': kazuha
}

heron = {
	'name': 'The Heron\'s Court',
	'list_3': wi_3,
	'list_4w': wi_4w,
	'list_4c': wi_4c + [diona, rosaria, xinyan, yanfei],
	'list_5': wi_5,
	'rate_up_4': [chongyun, ningguang, yanfei],
	'rate_up_5': ayaka
}

tapestry = {
	'name': 'Tapestry of Golden Flames',
	'list_3': wi_3,
	'list_4w': wi_4w,
	'list_4c': wi_4c + [diona, rosaria, xinyan, yanfei],
	'list_5': wi_5,
	'rate_up_4': [diona, sayu, xinyan],
	'rate_up_5': yoimiya
}

reign = {
	'name': 'Reign of Serenity',
	'list_3': wi_3,
	'list_4w': wi_4w,
	'list_4c': wi_4c + [diona, rosaria, sayu, xinyan, yanfei],
	'list_5': wi_5,
	'rate_up_4': [kujou_sara, sucrose, xiangling],
	'rate_up_5': shogun
}

lumi = {
	'name': 'Drifting Luminescence',
	'list_3': wi_3,
	'list_4w': wi_4w,
	'list_4c': wi_4c + [diona, rosaria, sayu, xinyan, yanfei],
	'list_5': wi_5,
	'rate_up_4': [beidou, rosaria, xingqiu],
	'rate_up_5': kokomi
}

snezhnaya3 = {
	'name': 'Farewell of Snezhnaya',
	'list_3': wi_3,
	'list_4w': wi_4w,
	'list_4c': wi_4c + [diona, kujou_sara, rosaria, sayu, xinyan, yanfei],
	'list_5': wi_5,
	'rate_up_4': [chongyun, ningguang, yanfei],
	'rate_up_5': childe
}

bloom2 = {
	'name': 'Moment of Bloom',
	'list_3': wi_3,
	'list_4w': wi_4w,
	'list_4c': wi_4c + [diona, kujou_sara, rosaria, sayu, xinyan, yanfei],
	'list_5': wi_5,
	'rate_up_4': [diona, sayu, thoma],
	'rate_up_5': hu_tao
}

# Todos os banners especiais
special_banners = [
	[date(2020, 9, 28), date(2020, 10, 18), ballad],
	[date(2020, 10, 20), date(2020, 11, 9), spark],
	[date(2020, 11, 11), date(2020, 11, 30), snezhnaya],
	[date(2020, 12, 1), date(2020, 12, 22), gentry],
	[date(2020, 12, 23), date(2021, 1, 11), secretum],
	[date(2021, 1, 12), date(2021, 2, 2), harbor],
	[date(2021, 2, 3), date(2021, 2, 16), invitation],
	[date(2021, 2, 17), date(2021, 3, 1), lanterns],
	[date(2021, 3, 2), date(2021, 3, 16), bloom],
	[date(2021, 3, 17), date(2021, 4, 5), ballad2],
	[date(2021, 4, 6), date(2021, 4, 27), snezhnaya2],
	[date(2021, 4, 28), date(2021, 5, 17), gentry2],
	[date(2021, 5, 18), date(2021, 6, 8), ocean],
	[date(2021, 6, 9), date(2021, 6, 28), spark2],
	[date(2021, 6, 29), date(2021, 7, 20), leaves],
	[date(2021, 7, 21), date(2021, 8, 9), heron],
	[date(2021, 8, 10), date(2021, 8, 31), tapestry],
	[date(2021, 9, 1), date(2021, 9, 20), reign],
	[date(2021, 9, 21), date(2021, 10, 12), lumi],
	[date(2021, 10, 13), date(2021, 11, 1), snezhnaya3],
	[date(2021, 11, 2), date(2021, 11, 22), bloom2]
]

# Criar pity e variável genérica
pity_system = Pity(0, True, 0, True)
pity_system.pity_reset()

banner_entry = None
df_base_dict = {
		'date': [],
		'running_banner': [],
		'type': [],
		'wish': [],
		'rarity': [],
		'weapon': [],
		'element': [],
		'sex': []
	}

print('''
	- --- --- --- --- --- --- GIG for DSP --- --- --- --- --- --- --- -
	Genshin Impact Generator - Wishes Results for Data Science Projects
	latest update: 08/11/2021 - Moment of Bloom Rerun Banner
	coded by samuelfarrus
''')

while True:
	try:
		banner_entry = input('Type a date (YYYY-MM-DD) to run a banner. Otherwise, insert -1 to finish: ')

		if banner_entry == '-1':
			break
		# error DataInsertError
		elif banner_entry != '-1':
			if '-' not in banner_entry or len(banner_entry) < 10:
				raise DataInsertError('!!!ERROR: wrong date format, please insert new value!!!')
		elif bool(banner_entry) is False:
			raise DataInsertError('!!!ERROR: no date inserted, please insert new value!!!')

		wish_amount = input('Insert Wishes amount or leave empty for just 1: ')

		if bool(wish_amount) is False:
			wish_amount = 1
		elif wish_amount.isalpha() is True and wish_amount.isnumeric() is False:
			raise DataInsertError('!!!ERROR: wishes must numeric, please insert new value!!!')

	except DataInsertError as er:
		print(er)
	else:
		# gera dados do gacha
		wish_amount = int(wish_amount)

		for x in range(0, wish_amount):
			gacha_run = gacha(banner_entry, special_banners, wi, pity_system)
			gacha_banner = gacha_run[0]
			result = gacha_run[1]

			if result['type'] == 'weapon':
				df_base_dict['date'].append(banner_entry)
				df_base_dict['running_banner'].append(gacha_banner['name'])
				df_base_dict['type'].append(result['type'])
				df_base_dict['wish'].append(result['name'])
				df_base_dict['rarity'].append(result['rar'])
				df_base_dict['weapon'].append(result['wp_type'])
				df_base_dict['element'].append('None')
				df_base_dict['sex'].append('None')
			else:  # resultado do gacha é um character
				df_base_dict['date'].append(banner_entry)
				df_base_dict['running_banner'].append(gacha_banner['name'])
				df_base_dict['type'].append(result['type'])
				df_base_dict['wish'].append(result['name'])
				df_base_dict['rarity'].append(result['rar'])
				df_base_dict['weapon'].append(result['wp'])
				df_base_dict['element'].append(result['elem'])
				df_base_dict['sex'].append(result['sex'])

# save csv
print('Proccess finished. Generated {} wish(es).'.format(len(df_base_dict['date'])))
csv_name = input('Enter the name of the file to be generated. If empty, default name: \'genshin_dataset\': ')

if bool(csv_name) is False:
	csv_name = 'genshin_dataset.csv'
elif '.csv' not in csv_name:
	csv_name = csv_name + '.csv'

df = pandas.DataFrame(df_base_dict)

df.to_csv(csv_name)
