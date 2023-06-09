import random

jadwalKereta = [
    {'No': 1, 'Kereta': 'Argo Lawu', 'Tujuan': 'Jakarta', 'Keberangkatan': '06:30', 'Tiba': '14:00'},
    {'No': 1, 'Kereta': 'Argo Lawu', 'Tujuan': 'Jakarta', 'Keberangkatan': '06:30', 'Tiba': '14:00'},
    {'No': 2, 'Kereta': 'Bogowonto', 'Tujuan': 'Jakarta', 'Keberangkatan': '07:30', 'Tiba': '15:15'},
    {'No': 3, 'Kereta': 'Malioboro', 'Tujuan': 'Bandung', 'Keberangkatan': '08:30', 'Tiba': '16:45'},
    {'No': 4, 'Kereta': 'Gajayana', 'Tujuan': 'Malang', 'Keberangkatan': '09:45', 'Tiba': '18:15'},
    {'No': 5, 'Kereta': 'Senja Utama', 'Tujuan': 'Surabaya', 'Keberangkatan': '11:15', 'Tiba': '19:45'},
    {'No': 6, 'Kereta': 'Prambanan', 'Tujuan': 'Solo', 'Keberangkatan': '12:30', 'Tiba': '20:40'},
    {'No': 7, 'Kereta': 'Progo', 'Tujuan': 'Semarang', 'Keberangkatan': '13:45', 'Tiba': '22:00'},
    {'No': 8, 'Kereta': 'Mataram', 'Tujuan': 'Surabaya', 'Keberangkatan': '15:00', 'Tiba': '23:30'},
    {'No': 9, 'Kereta': 'Bogowonto', 'Tujuan': 'Jakarta', 'Keberangkatan': '16:30', 'Tiba': '01:15'},
    {'No': 10, 'Kereta': 'Taksaka Malam', 'Tujuan': 'Gambir', 'Keberangkatan': '20:00', 'Tiba': '05:23'},
    {'No': 11, 'Kereta': 'Kertajaya', 'Tujuan': 'Surabaya', 'Keberangkatan': '04:00', 'Tiba': '11:30'},
    {'No': 12, 'Kereta': 'Argo Muria', 'Tujuan': 'Semarang', 'Keberangkatan': '05:30', 'Tiba': '13:15'},
    {'No': 13, 'Kereta': 'Sancaka', 'Tujuan': 'Yogyakarta', 'Keberangkatan': '07:00', 'Tiba': '15:20'},
    {'No': 14, 'Kereta': 'Serayu', 'Tujuan': 'Purwokerto', 'Keberangkatan': '08:15', 'Tiba': '16:45'},
    {'No': 15, 'Kereta': 'Bangunkarta', 'Tujuan': 'Surabaya', 'Keberangkatan': '09:30', 'Tiba': '17:55'},
    {'No': 16, 'Kereta': 'Sembrani', 'Tujuan': 'Gambir', 'Keberangkatan': '10:45', 'Tiba': '19:10'},
    {'No': 17, 'Kereta': 'Gumarang', 'Tujuan': 'Cirebon', 'Keberangkatan': '12:00', 'Tiba': '20:25'},
    {'No': 18, 'Kereta': 'Argo Dwipangga', 'Tujuan': 'Solo', 'Keberangkatan': '13:15', 'Tiba': '21:40'},
    {'No': 19, 'Kereta': 'Ranggajati', 'Tujuan': 'Cirebon', 'Keberangkatan': '14:30', 'Tiba': '22:55'},
    {'No': 20, 'Kereta': 'Argo Wilis', 'Tujuan': 'Surabaya', 'Keberangkatan': '15:45', 'Tiba': '00:10'},
    {'No': 21, 'Kereta': 'Gajahwong', 'Tujuan': 'Yogyakarta', 'Keberangkatan': '17:00', 'Tiba': '01:20'},
    {'No': 22, 'Kereta': 'Bima', 'Tujuan': 'Malang', 'Keberangkatan': '18:15', 'Tiba': '02:40'},
    {'No': 23, 'Kereta': 'Jayakarta', 'Tujuan': 'Gambir', 'Keberangkatan': '19:30', 'Tiba': '04:00'},
    {'No': 24, 'Kereta': 'Mutiara Selatan', 'Tujuan': 'Surabaya', 'Keberangkatan': '21:00', 'Tiba': '06:20'},
]

kelas_options = ['Ekonomi', 'Bisnis']

for jadwal in jadwalKereta:
    jadwal['Kelas'] = random.choice(kelas_options)


