gen_y_dict = {
            "CRINGE": "Aneh, memalukan atau tidak lucu",
            "LOL": "Singkatan dari laughing out loud, menyatakan sesuatu lucu",
            "ROFL": "Singkatan dari rolling on the floor, menyatakan sesuatu sangat teramat lucu",
            "SHEESH": "Tanggapan terhadap sesuatu yang mengejutkan",
            "CREEPY": "Menakutkan",
            "AGGRO": "Singkatan dari agresif"
            }
#Isi list bisa bertambah kapanpun

word = input("Ketik kata yang tidak Kamu mengerti: ").upper()

if word in gen_y_dict.keys():
    print(gen_y_dict[word])
else:
    print("Kata yang dimasukkan tidak ditemukan")
