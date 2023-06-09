import random
from jadwal_kereta import jadwalKereta
from tabulate import tabulate


def display_jadwal_kereta_malam(jadwal):
    header = ["No", "Kereta", "Tujuan", "Keberangkatan", "Tiba", "Kelas"]
    table = []
    for j in jadwal:
        jam_keberangkatan = int(j['Keberangkatan'].split(':')[0])
        if jam_keberangkatan >= 20 or jam_keberangkatan <= 5:
            row = [j['No'], j['Kereta'], j['Tujuan'],
                   j['Keberangkatan'], j['Tiba'], j.get('Kelas', '-')]
            table.append(row)
    print(tabulate(table, headers=header, tablefmt="fancy_grid"))


def display_jadwal_kereta(jadwal):
    header = ["No", "Kereta", "Tujuan", "Keberangkatan", "Tiba", "Kelas"]
    table = []
    for j in jadwal:
        row = [j['No'], j['Kereta'], j['Tujuan'],
               j['Keberangkatan'], j['Tiba'], j.get('Kelas', '-')]
        table.append(row)
    print(tabulate(table, headers=header, tablefmt="fancy_grid"))


def filter_jadwal_tujuan(jadwal, tujuan):
    return [j for j in jadwal if j['Tujuan'] == tujuan]


def filter_jadwal_keberangkatan(jadwal, keberangkatan):
    return [j for j in jadwal if j['Keberangkatan'] == keberangkatan]


def berikan_rekomendasi(keberangkatan, tujuan):
    jadwal_filtered = [j for j in jadwalKereta if j['Keberangkatan']
                       >= keberangkatan and j['Tujuan'] == tujuan]

    if len(jadwal_filtered) == 0:
        return "Maaf, tidak ditemukan jadwal kereta yang sesuai dengan permintaan Anda."

    jadwal_sorted = sorted(jadwal_filtered, key=lambda j: j['Keberangkatan'])

    rekomendasi = []
    for jadwal in jadwal_sorted:
        rekomendasi.append(jadwal)
    return rekomendasi


def handle_question(pertanyaan):
    if pertanyaan == "Tampilkan Jadwal Yang Tersedia:" or pertanyaan == "1":
        display_jadwal_kereta(jadwalKereta)
        return ""
    else:
        return "Pertanyaan tidak valid."


def forward_chaining():
    knowledge_base = []
    tujuan_kereta = [jadwal['Tujuan'] for jadwal in jadwalKereta]

    while True:
        print("\nSilakan pilih nomor yang tersedia untuk melihat jadwalnya:")
        for i, pertanyaan in enumerate(daftar_pertanyaan, 1):
            print(f"{i}. {pertanyaan}")

        while True:
            pilihan_pertanyaan = input("\nPilihan: ")
            if pilihan_pertanyaan.isdigit():
                pilihan_pertanyaan = int(pilihan_pertanyaan)
                if 1 <= pilihan_pertanyaan <= len(daftar_pertanyaan):
                    break
            print("Pilihan tidak valid. Silakan pilih nomor yang tersedia.")

        pertanyaan_terpilih = daftar_pertanyaan[pilihan_pertanyaan - 1]

        jawaban = handle_question(pertanyaan_terpilih)
        print(f"\nPertanyaan: {pertanyaan_terpilih}")
        print(f"Jawaban: {jawaban}")

        knowledge_base.append((pertanyaan_terpilih, jawaban))

        if pertanyaan_terpilih == "Tampilkan Jadwal Yang Tersedia:" or pertanyaan_terpilih == "1":
            pilihan_tujuan = input("\nPilih tujuan kereta: ")

            while pilihan_tujuan not in tujuan_kereta:
                print("Masukkan jadwal tujuan yang valid.")
                pilihan_tujuan = input("Pilih tujuan kereta: ")

            jadwal_tujuan = filter_jadwal_tujuan(jadwalKereta, pilihan_tujuan)
            display_jadwal_kereta(jadwal_tujuan)

            while True:
                pilihan_keberangkatan = input(
                    "\nPilih jam keberangkatan (hh:mm): ")

                jadwal_keberangkatan = filter_jadwal_keberangkatan(
                    jadwal_tujuan, pilihan_keberangkatan)
                if len(jadwal_keberangkatan) > 0:
                    rekomendasi = berikan_rekomendasi(
                        pilihan_keberangkatan, pilihan_tujuan)

                    if len(rekomendasi) == 0:
                        print(
                            "Tidak ditemukan jadwal kereta yang sesuai dengan permintaan Anda.")
                    else:
                        print(
                            "\nRekomendasi jadwal kereta yang mendekati jam keberangkatan yang Anda pilih:")
                        display_jadwal_kereta(rekomendasi)
                    break
                else:
                    print(
                        "Maaf, jam keberangkatan tidak tersedia atau tidak valid. Silakan masukkan jam keberangkatan yang valid.")

        pilihan_lanjut = input(
            "\nApakah Anda ingin bertanya lagi? (ya/tidak): ")
        if pilihan_lanjut.lower() != "ya":
            break

    return knowledge_base


daftar_pertanyaan = [
    "Tampilkan Jadwal Yang Tersedia:"
]

knowledge_base = forward_chaining()
print("Terima kasih!")
